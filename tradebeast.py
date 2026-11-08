#!/usr/bin/env python3
"""TradeBeast — the ultimate crypto trading MCP server.

One MCP server that fuses many crypto MCP sub-servers into a single
stdio endpoint, so any MCP client (Claude Desktop, Muse, …) gets the
whole arsenal through one connection:

    ccxt (public market data, 100+ exchanges)  ·  trading-signals (Binance TA)
    LiquidVision (derivatives intel, hosted)   ·  smc (Smart Money Concepts)
    tradefloor (Hyperliquid candles)           ·  microstructure (Binance vision)
    rsi-divergence                             ·  technical-analysis (69 tools)
    crypto-indicators (78 indicators)          ·  Bitget (official, opt-in)
    funding-rates (cross-exchange funding)     ·  TradingView (screener + TA)
    Kronos (local 4h ML forecast, opt-in)

Design
------
* Every sub-server is spawned as a long-lived MCP client session and its
  tools are re-exposed under a short source prefix
  (``ccxt_get_tickers``, ``bitget_futures_get_positions``,
  ``tv_get_technical_analysis``, ``funding_compare_funding_rates``,
  ``kronos_forecast`` …). Tool calls are routed to the owning
  sub-server and the result is returned unchanged.
* A dead sub-server never kills the beast: startup connects with
  per-server timeouts and logs failures to stderr, then keeps serving
  the rest. A failed call reconnects its sub-server once and retries
  once (read-only tools only — order-placement tools are never
  retried blindly, so a lost response can never double-execute).
* Safety is inherited from the sub-servers' own allowlists: only
  read-only tools plus Bitget spot/futures order place/cancel are ever
  exposed. Withdrawals, transfers, margin trading, copy-follow,
  convert execution, broker writes, leverage changes and earn actions
  are blocked and never appear in the tool list.
* Credentials: TradeBeast never bundles, logs or transmits any API
  key, secret or password. Bitget is an optional sub-server that only
  starts when BITGET_API_KEY / BITGET_SECRET_KEY / BITGET_PASSPHRASE
  are present in the environment. Kronos only starts when the local
  forecast server answers its /health endpoint.

Usage
-----
    python tradebeast.py [--config config.json] [--dump-tools]

    --dump-tools   connect to all sub-servers, print the aggregated
                   tool catalog as JSON, and exit (used by docs/TOOLS.md).

Configure which sub-servers run in config.json (see config.example.json)
or with TRADEBEAST_DISABLE_<name>=1 environment variables.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import sys
from contextlib import AsyncExitStack
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import httpx
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamable_http_client
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp import types

__version__ = "1.0.0"

log = logging.getLogger("tradebeast")
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s tradebeast %(levelname)s %(message)s",
    stream=sys.stderr,
)

HOME = Path.home()
CONNECTORS = HOME / "workspace" / "custom-connectors"
SHARED_VENV_PY = str(CONNECTORS / "_shared-venv" / "bin" / "python")
TV_VENV_BIN = HOME / "workspace" / "tradingview-mcp" / ".venv" / "bin"

# Env vars forwarded to every stdio child. The MCP SDK only inherits a
# small allowlisted env, so the sandbox egress proxy vars must be passed
# explicitly or the children cannot reach the internet (and Node children
# fail TLS without the MITM CA bundle).
PROXY_ENV_KEYS = (
    "HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy",
    "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE",
    "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NO_PROXY", "no_proxy",
)

# Bitget order tools are never auto-retried: a call whose response was
# lost may already have executed on the exchange.
BITGET_WRITE_TOOLS = {
    "spot_place_order", "spot_cancel_orders", "spot_place_plan_order",
    "spot_cancel_plan_orders", "spot_modify_order",
    "futures_place_order", "futures_cancel_orders",
}

# ---------------------------------------------------------------------------
# Sub-server catalogue.
# command/args may use ~ and $VAR. allowlist=None means "expose every tool
# the sub-server lists" (used only for the read-only TradingView server).
# ---------------------------------------------------------------------------


@dataclass
class SubServerSpec:
    key: str
    prefix: str
    title: str
    kind: str  # "stdio" | "http" | "native"
    command: str = ""
    args: list[str] = field(default_factory=list)
    env: dict[str, str] = field(default_factory=dict)
    cwd: str = ""
    url: str = ""
    allowlist: set[str] | None = None
    connect_timeout: float = 60.0
    requires_env: tuple[str, ...] = ()
    requires_health_url: str = ""


def _proxy_env(extra: dict[str, str] | None = None) -> dict[str, str]:
    env = {k: os.environ[k] for k in PROXY_ENV_KEYS if k in os.environ}
    env["NODE_USE_ENV_PROXY"] = "1"
    if extra:
        env.update(extra)
    return env


def _default_specs() -> dict[str, SubServerSpec]:
    ccxt = CONNECTORS / "custom.ccxt-mcp"
    signals = CONNECTORS / "custom.trading-signals-mcp"
    lv = CONNECTORS / "custom.liquidvision"
    smc = CONNECTORS / "custom.smc-mcp"
    tf = CONNECTORS / "custom.tradefloor-mcp"
    micro = CONNECTORS / "custom.microstructure-mcp"
    rsi = CONNECTORS / "custom.rsi-divergence"
    ta = CONNECTORS / "custom.technical-analysis"
    ind = CONNECTORS / "custom.crypto-indicators-mcp"
    bitget = CONNECTORS / "custom.bitget"
    funding = CONNECTORS / "custom.funding-rates-mcp"
    return {
        "ccxt": SubServerSpec(
            key="ccxt", prefix="ccxt", title="CCXT (100+ exchanges, public market data)",
            kind="stdio", command="node",
            args=[str(ccxt / "node" / "node_modules" / "ccxt-mcp" / "js" / "server.js")],
            env=_proxy_env(),
            allowlist={
                "list_exchanges", "describe_exchange", "describe_method",
                "search_markets", "get_tickers", "get_orderbook", "get_ohlcv",
                "get_trades", "search_events", "call_read_method",
                "call_implicit_get", "get_safety_status",
            }),
        "signals": SubServerSpec(
            key="signals", prefix="signals", title="Trading Signals (Binance TA)",
            kind="stdio", command="node",
            args=[str(signals / "server-src" / "build" / "index.mjs")],
            env=_proxy_env(),
            allowlist={
                "fetchBookData", "fetchFifteenMinuteCandleHistory",
                "fetchHourCandleHistory", "fetchLongTermSignals",
                "fetchMicroTermSignals", "fetchOneMinuteCandleHistory",
                "fetchShortTermSignals", "fetchSlopeData",
                "fetchSwingTermSignals", "fetchThirtyMinuteCandleHistory",
                "fetchVolumeData",
            }),
        "liquidvision": SubServerSpec(
            key="liquidvision", prefix="lv",
            title="LiquidVision (derivatives intel, hosted)",
            kind="http", url="https://liquidvision.app/mcp",
            allowlist={
                "ask", "explain_market", "get_accuracy",
                "get_arbitrum_perps", "get_cash_flows", "get_cvd",
                "get_detective_events", "get_footprint",
                "get_funding_arbitrage", "get_funding_dispersion",
                "get_funding_history", "get_funding_rates",
                "get_funding_settlements", "get_hip3_markets",
                "get_hl_account", "get_hl_builder_markets",
                "get_hl_liquidation_map", "get_hl_whales",
                "get_lighter_liquidation_map", "get_lighter_whales",
                "get_liquidation_cascades", "get_liquidation_heatmap",
                "get_liquidation_map", "get_liquidations",
                "get_liquidations_summary", "get_long_short_ratio",
                "get_market_brief", "get_microstructure", "get_oi_board",
                "get_open_interest", "get_open_interest_history",
                "get_orderbook_heatmap", "get_positioning_regime",
                "get_precedents", "get_spoofing", "get_stocks",
                "get_token_unlocks", "get_tokenized_stocks",
                "get_top_traders", "list_history_packages", "list_markets",
            }),
        "smc": SubServerSpec(
            key="smc", prefix="smc", title="SMC (Smart Money Concepts, Yahoo OHLCV)",
            kind="stdio", command=SHARED_VENV_PY, args=["-m", "smc_mcp"],
            env=_proxy_env({"PYTHONPATH": str(smc / "server-src" / "src")}),
            cwd=str(smc / "server-src"),
            allowlist={
                "smc_find_fair_value_gaps", "smc_find_liquidity_sweeps",
                "smc_find_order_blocks", "smc_full_analysis",
                "smc_get_market_structure",
            }),
        "tradefloor": SubServerSpec(
            key="tradefloor", prefix="tradefloor",
            title="TradeFloor (Hyperliquid candles)",
            kind="stdio", command=SHARED_VENV_PY, args=["-m", "tradefloor_mcp"],
            env=_proxy_env({"PYTHONPATH": str(tf / "server-src")}),
            allowlist={"analyze_structure", "find_blocks", "find_liquidity_sweeps"}),
        "microstructure": SubServerSpec(
            key="microstructure", prefix="micro",
            title="Microstructure (Binance vision spot klines)",
            kind="stdio", command=SHARED_VENV_PY,
            args=["-m", "microstructure_mcp.server"],
            env=_proxy_env({"PYTHONPATH": str(micro / "server-src" / "src")}),
            allowlist={
                "get_fair_value_gaps", "get_liquidity_zones",
                "get_market_structure", "get_order_blocks", "get_snapshot",
            }),
        "rsi": SubServerSpec(
            key="rsi", prefix="rsi", title="RSI Divergence Detector",
            kind="stdio", command=SHARED_VENV_PY,
            args=[str(rsi / "server" / "server.py")],
            env=_proxy_env(),
            allowlist={"detect_rsi_divergence", "scan_rsi_divergences"}),
        "technical_analysis": SubServerSpec(
            key="technical_analysis", prefix="ta",
            title="Technical Analysis (GearTrade, 54 tools)",
            kind="stdio", command="node",
            args=[str(ta / "server-src" / "stdio-shim.mjs")],
            env=_proxy_env(),
            allowlist={
                "accelerator_oscillator", "awesome_oscillator",
                "calculate_position_setup", "calculate_risk_management",
                "chande_momentum", "channels", "coppock_curve",
                "detrended_price", "double_ema", "elder_ray",
                "fisher_transform", "gator_oscillator", "get_External_data",
                "get_Multitimeframe", "get_candlestick_patterns",
                "get_correlation_analysis", "get_divergence",
                "get_indicators", "get_liquidation_levels",
                "get_long_short_ratio", "get_market_regime",
                "get_market_sentiment", "get_market_structure",
                "get_orderbook_depth", "get_price", "get_tier_classification",
                "get_volume_analysis", "get_volume_profile",
                "get_whale_position", "hull_ma", "kaufman_adaptive_ma",
                "know_sure_thing", "ma_envelope", "mcginley_dynamic",
                "momentum", "patterns", "percentage_price_oscillator",
                "pivot_points", "rainbow_ma", "rate_of_change",
                "relative_vigor_index", "schaff_trend_cycle", "smoothed_ma",
                "stochastic_rsi", "strength_indicators", "trend_indicators",
                "triple_ema", "trix", "true_strength_index",
                "ultimate_oscillator", "volatility_indicators",
                "volume_indicators", "vwma", "weighted_ma",
            }),
        "crypto_indicators": SubServerSpec(
            key="crypto_indicators", prefix="ind",
            title="Crypto Indicators (78 indicators)",
            kind="stdio", command="node",
            args=[str(ind / "server-src" / "index.js")],
            env=_proxy_env(),
            allowlist={
                "calculate_absolute_price_oscillator",
                "calculate_absolute_price_oscillator_strategy",
                "calculate_acceleration_bands",
                "calculate_acceleration_bands_strategy",
                "calculate_accumulation_distribution", "calculate_aroon",
                "calculate_aroon_strategy", "calculate_average_true_range",
                "calculate_awesome_oscillator",
                "calculate_awesome_oscillator_strategy",
                "calculate_balance_of_power",
                "calculate_balance_of_power_strategy",
                "calculate_bollinger_bands",
                "calculate_bollinger_bands_strategy",
                "calculate_bollinger_bands_width",
                "calculate_chaikin_money_flow",
                "calculate_chaikin_money_flow_strategy",
                "calculate_chaikin_oscillator",
                "calculate_chande_forecast_oscillator",
                "calculate_chande_forecast_oscillator_strategy",
                "calculate_chandelier_exit",
                "calculate_commodity_channel_index",
                "calculate_donchian_channel",
                "calculate_double_exponential_moving_average",
                "calculate_ease_of_movement",
                "calculate_ease_of_movement_strategy",
                "calculate_exponential_moving_average",
                "calculate_force_index", "calculate_force_index_strategy",
                "calculate_ichimoku_cloud",
                "calculate_ichimoku_cloud_strategy", "calculate_kdj",
                "calculate_kdj_strategy", "calculate_keltner_channel",
                "calculate_macd_strategy", "calculate_mass_index",
                "calculate_momentum_strategy", "calculate_money_flow_index",
                "calculate_money_flow_index_strategy",
                "calculate_moving_average_convergence_divergence",
                "calculate_moving_max", "calculate_moving_min",
                "calculate_moving_standard_deviation",
                "calculate_moving_sum", "calculate_negative_volume_index",
                "calculate_negative_volume_index_strategy",
                "calculate_on_balance_volume", "calculate_parabolic_sar",
                "calculate_parabolic_sar_strategy",
                "calculate_percentage_price_oscillator",
                "calculate_percentage_volume_oscillator",
                "calculate_price_rate_of_change",
                "calculate_projection_oscillator",
                "calculate_projection_oscillator_strategy",
                "calculate_qstick", "calculate_relative_strength_index",
                "calculate_rolling_moving_average",
                "calculate_rsi2_strategy",
                "calculate_simple_moving_average", "calculate_since_change",
                "calculate_stochastic_oscillator",
                "calculate_stochastic_oscillator_strategy",
                "calculate_triangular_moving_average",
                "calculate_triple_exponential_average",
                "calculate_triple_exponential_moving_average",
                "calculate_true_range", "calculate_typical_price",
                "calculate_typical_price_strategy", "calculate_ulcer_index",
                "calculate_volume_price_trend",
                "calculate_volume_weighted_average_price",
                "calculate_volume_weighted_average_price_strategy",
                "calculate_volume_weighted_moving_average",
                "calculate_volume_weighted_moving_average_strategy",
                "calculate_vortex", "calculate_vortex_strategy",
                "calculate_williams_r",
                "calculate_williams_r_strategy",
            }),
        "bitget": SubServerSpec(
            key="bitget", prefix="bitget",
            title="Bitget (official, reads + order place/cancel)",
            kind="stdio", command="node",
            args=[str(bitget / "node" / "node_modules" / "bitget-mcp-server"
                      / "dist" / "index.js"), "--modules", "all"],
            env=_proxy_env(),
            allowlist={
                "system_get_capabilities",
                "spot_get_ticker", "spot_get_symbols", "spot_get_depth",
                "spot_get_candles", "spot_get_trades", "spot_get_orders",
                "spot_get_fills", "spot_get_plan_orders",
                "spot_place_order", "spot_cancel_orders",
                "spot_place_plan_order", "spot_cancel_plan_orders",
                "spot_modify_order",
                "futures_get_ticker", "futures_get_contracts",
                "futures_get_depth", "futures_get_candles",
                "futures_get_trades", "futures_get_positions",
                "futures_get_orders", "futures_get_fills",
                "futures_get_open_interest", "futures_get_funding_rate",
                "futures_place_order", "futures_cancel_orders",
                "get_account_assets", "get_account_bills",
                "get_transaction_records", "get_deposit_address",
                "margin_get_assets", "margin_get_orders",
                "margin_get_records",
                "copy_get_traders", "copy_get_positions", "copy_get_orders",
                "convert_get_quote", "convert_get_history",
                "p2p_get_merchants", "p2p_get_orders",
                "broker_get_info",
            },
            requires_env=("BITGET_API_KEY", "BITGET_SECRET_KEY",
                          "BITGET_PASSPHRASE")),
        "funding": SubServerSpec(
            key="funding", prefix="funding",
            title="Funding Rates (cross-exchange funding comparison)",
            kind="stdio",
            command=str(funding / ".venv" / "bin" / "funding-rates-mcp"),
            args=[], env=_proxy_env(),
            allowlist={"compare_funding_rates"}),
        "tradingview": SubServerSpec(
            key="tradingview", prefix="tv",
            title="TradingView (screener, technicals, backtests)",
            kind="stdio",
            command=str(TV_VENV_BIN / "tradingview-mcp"), args=["stdio"],
            env=_proxy_env(), allowlist=None,
            connect_timeout=90.0),
        "kronos": SubServerSpec(
            key="kronos", prefix="kronos",
            title="Kronos (local 4h ML forecast)",
            kind="native", url="http://127.0.0.1:8901",
            requires_health_url="http://127.0.0.1:8901/health"),
    }


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------


def _expand(value: Any) -> Any:
    if isinstance(value, str):
        return os.path.expandvars(os.path.expanduser(value))
    if isinstance(value, list):
        return [_expand(v) for v in value]
    if isinstance(value, dict):
        return {k: _expand(v) for k, v in value.items()}
    return value


def load_config(path: str | None) -> dict[str, Any]:
    cfg: dict[str, Any] = {}
    candidates = []
    if path:
        candidates.append(Path(path))
    elif os.environ.get("TRADEBEAST_CONFIG"):
        candidates.append(Path(os.environ["TRADEBEAST_CONFIG"]))
    else:
        candidates.append(Path(__file__).resolve().parent / "config.json")
    for candidate in candidates:
        if candidate.is_file():
            try:
                cfg = json.loads(candidate.read_text(encoding="utf-8"))
                log.info("loaded config from %s", candidate)
            except Exception as exc:  # noqa: BLE001 - config errors are fatal-ish
                log.warning("could not read config %s: %s", candidate, exc)
            break
    return _expand(cfg)


def _env_flag(name: str) -> bool | None:
    val = os.environ.get(f"TRADEBEAST_DISABLE_{name.upper()}")
    if val == "1":
        return False
    val = os.environ.get(f"TRADEBEAST_ENABLE_{name.upper()}")
    if val == "1":
        return True
    if val == "0":
        return False
    return None


def resolve_specs(cfg: dict[str, Any]) -> list[SubServerSpec]:
    """Apply config.json + env overrides to the default catalogue."""
    defaults = _default_specs()
    cfg_servers = cfg.get("servers", {}) or {}
    kronos_url = cfg.get("kronos_url") or os.environ.get(
        "TRADEBEAST_KRONOS_URL") or "http://127.0.0.1:8901"
    specs: list[SubServerSpec] = []
    for key, spec in defaults.items():
        override = cfg_servers.get(key, {}) or {}
        if "enabled" in override:
            spec_enabled = bool(override["enabled"])
        else:
            spec_enabled = True
        flag = _env_flag(key)
        if flag is not None:
            spec_enabled = flag
        if not spec_enabled:
            log.info("sub-server %s disabled by config", key)
            continue
        if override.get("command"):
            spec.command = override["command"]
        if override.get("args") is not None:
            spec.args = list(override["args"])
        if override.get("cwd"):
            spec.cwd = override["cwd"]
        if override.get("url"):
            spec.url = override["url"]
        if override.get("env"):
            merged = dict(spec.env)
            merged.update(override["env"])
            spec.env = merged
        if key == "kronos":
            spec.url = kronos_url
            spec.requires_health_url = kronos_url.rstrip("/") + "/health"
        if key == "bitget":
            # Credentials come from the environment only. Never from a file.
            missing = [v for v in spec.requires_env if not os.environ.get(v)]
            if missing:
                log.info(
                    "sub-server bitget disabled: missing env vars %s", missing)
                continue
            spec.env = dict(spec.env)
            for var in spec.requires_env:
                spec.env[var] = os.environ[var]
        specs.append(spec)
    return specs


# ---------------------------------------------------------------------------
# Aggregator
# ---------------------------------------------------------------------------


@dataclass
class Connection:
    spec: SubServerSpec
    stack: AsyncExitStack | None = None
    session: ClientSession | None = None
    tools: list[types.Tool] = field(default_factory=list)
    up: bool = False
    error: str = ""
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)


class TradeBeast:
    def __init__(self, specs: list[SubServerSpec]) -> None:
        self.specs = {s.key: s for s in specs}
        self.connections: dict[str, Connection] = {
            s.key: Connection(spec=s) for s in specs}
        # aggregated name -> (server key, original tool name)
        self.routes: dict[str, tuple[str, str]] = {}
        self.tools: list[types.Tool] = []
        # trust_env=False: the sandbox NO_PROXY contains bracketed IPv6
        # entries ([::1], [fd8b:...]) that httpx's env parser rejects with
        # InvalidURL. Kronos is localhost anyway, so no proxy is needed.
        self._http = httpx.AsyncClient(timeout=30.0, trust_env=False)
        self._status_tools()

    # -- native tools ----------------------------------------------------
    def _status_tools(self) -> None:
        self.tools.append(types.Tool(
            name="tradebeast_status",
            description=(
                "[tradebeast] Health of the beast: which sub-servers are "
                "up, how many tools each exposes, and the total tool count."
            ),
            input_schema={"type": "object", "properties": {}},
        ))

    def _kronos_tools(self) -> list[types.Tool]:
        return [
            types.Tool(
                name="kronos_forecast",
                description=(
                    "[kronos] 4h close-price forecast from the local Kronos "
                    "ML model. Arguments: {\"symbol\": \"IDOL/USDT\"}. "
                    "Takes up to ~3 minutes (the model runs in a worker)."
                ),
                input_schema={
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Symbol like IDOL/USDT",
                        },
                    },
                    "required": ["symbol"],
                },
            ),
            types.Tool(
                name="kronos_health",
                description="[kronos] Health check of the local Kronos forecast server.",
                input_schema={"type": "object", "properties": {}},
            ),
        ]

    # -- startup ---------------------------------------------------------
    async def start(self) -> None:
        await asyncio.gather(
            *(self._connect(key) for key in self.connections))
        self._rebuild_tool_list()
        up = sum(1 for c in self.connections.values() if c.up)
        log.info("tradebeast up: %d/%d sub-servers, %d tools",
                 up, len(self.connections), len(self.tools))

    async def stop(self) -> None:
        for conn in self.connections.values():
            if conn.stack is not None:
                try:
                    await conn.stack.aclose()
                except Exception:  # noqa: BLE001 - shutdown must not hang
                    pass
                conn.stack = None
                conn.session = None
                conn.up = False
        try:
            await self._http.aclose()
        except Exception:  # noqa: BLE001
            pass

    async def _connect(self, key: str) -> None:
        conn = self.connections[key]
        spec = conn.spec
        try:
            if spec.kind == "native":
                await self._connect_kronos(conn)
                return
            await asyncio.wait_for(
                self._connect_session(conn), timeout=spec.connect_timeout)
        except Exception as exc:  # noqa: BLE001 - one dead server must not kill the beast
            conn.up = False
            conn.error = f"{type(exc).__name__}: {exc}"[:300]
            log.warning("sub-server %s failed to start: %s", key, conn.error)

    async def _connect_kronos(self, conn: Connection) -> None:
        spec = conn.spec
        try:
            resp = await self._http.get(spec.requires_health_url, timeout=5.0)
            if resp.status_code != 200:
                raise RuntimeError(f"health HTTP {resp.status_code}")
        except Exception as exc:  # noqa: BLE001
            conn.up = False
            conn.error = f"unreachable: {exc}"[:300]
            log.info("sub-server kronos disabled: %s", conn.error)
            return
        conn.up = True
        conn.tools = self._kronos_tools()
        log.info("sub-server kronos up (native, %d tools)", len(conn.tools))

    async def _connect_session(self, conn: Connection) -> None:
        spec = conn.spec
        stack = AsyncExitStack()
        try:
            if spec.kind == "http":
                read, write = await stack.enter_async_context(
                    streamable_http_client(spec.url))
            else:
                params = StdioServerParameters(
                    command=spec.command, args=spec.args, env=spec.env,
                    cwd=spec.cwd or None)
                read, write = await stack.enter_async_context(
                    stdio_client(params))
            session = await stack.enter_async_context(
                ClientSession(read, write))
            await session.initialize()
            result = await session.list_tools()
            tools = self._filter_tools(spec, result.tools)
            conn.stack = stack
            conn.session = session
            conn.tools = tools
            conn.up = True
            conn.error = ""
            log.info("sub-server %s up (%d tools)", spec.key, len(tools))
        except Exception:
            await stack.aclose()
            raise

    @staticmethod
    def _filter_tools(spec: SubServerSpec,
                      listed: list[types.Tool]) -> list[types.Tool]:
        out: list[types.Tool] = []
        for tool in listed:
            if spec.allowlist is not None and tool.name not in spec.allowlist:
                continue
            out.append(types.Tool(
                name=f"{spec.prefix}_{tool.name}",
                description=f"[{spec.key}] {tool.description or ''}".strip(),
                input_schema=dict(tool.input_schema or {"type": "object"}),
            ))
        if spec.allowlist is not None:
            listed_names = {t.name for t in listed}
            missing = sorted(spec.allowlist - listed_names)
            if missing:
                log.warning("sub-server %s did not list allowlisted tools: %s",
                            spec.key, missing)
        return out

    def _rebuild_tool_list(self) -> None:
        self.tools = [t for t in self.tools
                      if t.name == "tradebeast_status"]
        self.routes = {}
        for key, conn in self.connections.items():
            if not conn.up:
                continue
            for tool in conn.tools:
                if tool.name in ("kronos_forecast", "kronos_health"):
                    self.routes[tool.name] = ("kronos", tool.name)
                else:
                    original = tool.name[len(conn.spec.prefix) + 1:]
                    self.routes[tool.name] = (key, original)
                self.tools.append(tool)
        self.tools.sort(key=lambda t: t.name)

    # -- calls -----------------------------------------------------------
    async def call(self, name: str, arguments: dict[str, Any]) -> types.CallToolResult:
        if name == "tradebeast_status":
            return types.CallToolResult(content=[
                types.TextContent(type="text",
                                  text=json.dumps(self.status(), indent=2))])
        route = self.routes.get(name)
        if route is None:
            return types.CallToolResult(
                is_error=True,
                content=[types.TextContent(
                    type="text",
                    text=f"Unknown tool: {name}. Use tradebeast_status to "
                         f"see the {len(self.tools)} available tools.")])
        key, original = route
        if key == "kronos":
            return await self._call_kronos(name, arguments)
        conn = self.connections[key]
        is_write = original in BITGET_WRITE_TOOLS
        try:
            return await self._call_session(conn, original, arguments)
        except Exception as exc:  # noqa: BLE001 - reconnect once, then report
            log.warning("call %s failed on %s (%s); reconnecting once",
                        name, key, exc)
            await self._reconnect(key)
            if is_write:
                return types.CallToolResult(
                    is_error=True,
                    content=[types.TextContent(
                        type="text",
                        text=f"{name} failed with {type(exc).__name__}: {exc}. "
                             f"The {key} sub-server was reconnected, but the "
                             f"call was NOT retried: it may already have "
                             f"executed. Check positions/orders before "
                             f"retrying.")])
            try:
                return await self._call_session(conn, original, arguments)
            except Exception as exc2:  # noqa: BLE001
                return types.CallToolResult(
                    is_error=True,
                    content=[types.TextContent(
                        type="text",
                        text=f"{name} failed after reconnect: "
                             f"{type(exc2).__name__}: {exc2}")])

    async def _call_session(self, conn: Connection, original: str,
                            arguments: dict[str, Any]) -> types.CallToolResult:
        if conn.session is None:
            raise RuntimeError(f"sub-server {conn.spec.key} is not connected")
        timeout = 240.0 if conn.spec.key == "kronos" else 120.0
        async with conn.lock:
            result = await asyncio.wait_for(
                conn.session.call_tool(original, arguments or {}),
                timeout=timeout)
        return types.CallToolResult(content=list(result.content),
                                    is_error=bool(result.is_error))

    async def _reconnect(self, key: str) -> None:
        conn = self.connections[key]
        conn.up = False
        if conn.stack is not None:
            try:
                await conn.stack.aclose()
            except Exception:  # noqa: BLE001
                pass
            conn.stack = None
            conn.session = None
        await self._connect(key)
        self._rebuild_tool_list()

    async def _call_kronos(self, name: str,
                           arguments: dict[str, Any]) -> types.CallToolResult:
        conn = self.connections["kronos"]
        base = conn.spec.url.rstrip("/")
        try:
            if name == "kronos_health":
                resp = await self._http.get(base + "/health", timeout=10.0)
                return types.CallToolResult(content=[
                    types.TextContent(type="text",
                                      text=json.dumps(resp.json(), indent=2))])
            symbol = str(arguments.get("symbol", "")).strip().upper()
            if not symbol:
                raise ValueError("kronos_forecast needs a symbol, e.g. IDOL/USDT")
            resp = await self._http.get(
                base + "/forecast", params={"symbol": symbol}, timeout=220.0)
            body = resp.text
            try:
                body = json.dumps(resp.json(), indent=2)
            except Exception:  # noqa: BLE001 - keep raw text if not JSON
                pass
            return types.CallToolResult(
                is_error=resp.status_code >= 400,
                content=[types.TextContent(type="text", text=body)])
        except Exception as exc:  # noqa: BLE001
            return types.CallToolResult(
                is_error=True,
                content=[types.TextContent(
                    type="text",
                    text=f"kronos call failed: {type(exc).__name__}: {exc}")])

    def status(self) -> dict[str, Any]:
        servers: dict[str, Any] = {}
        for key, conn in self.connections.items():
            servers[key] = {
                "title": conn.spec.title,
                "prefix": conn.spec.prefix,
                "up": conn.up,
                "tools": len(conn.tools) if conn.up else 0,
                **({"error": conn.error} if conn.error else {}),
            }
        return {
            "server": "tradebeast",
            "version": __version__,
            "total_tools": len(self.tools),
            "servers": servers,
        }


# ---------------------------------------------------------------------------
# MCP server wiring
# ---------------------------------------------------------------------------


def build_server(beast: TradeBeast) -> Server:
    async def _list_tools(ctx, params):  # noqa: ARG001
        return types.ListToolsResult(tools=list(beast.tools))

    async def _call_tool(ctx, params):  # noqa: ARG001
        arguments = params.arguments or {}
        if not isinstance(arguments, dict):
            arguments = {}
        return await beast.call(params.name, arguments)

    return Server(
        "tradebeast",
        version=__version__,
        description=(
            "The Ultimate Crypto Trading Beast — every crypto MCP fused "
            "into one unstoppable trading machine."
        ),
        on_list_tools=_list_tools,
        on_call_tool=_call_tool,
    )


async def _serve(beast: TradeBeast) -> None:
    await beast.start()
    server = build_server(beast)
    try:
        async with stdio_server() as (read, write):
            await server.run(
                read, write, server.create_initialization_options())
    finally:
        await beast.stop()


async def _dump_tools(beast: TradeBeast) -> int:
    await beast.start()
    catalog = {
        "server": "tradebeast",
        "version": __version__,
        "total_tools": len(beast.tools),
        "status": beast.status(),
        "tools": [
            {
                "name": t.name,
                "description": t.description,
                "inputSchema": t.input_schema,
            }
            for t in beast.tools
        ],
    }
    print(json.dumps(catalog, indent=2, ensure_ascii=False))
    await beast.stop()
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="TradeBeast — one MCP server fusing every crypto MCP.")
    parser.add_argument("--config", default=None,
                        help="path to config.json (default: ./config.json)")
    parser.add_argument("--dump-tools", action="store_true",
                        help="connect, print the tool catalog as JSON, exit")
    parser.add_argument("--version", action="store_true",
                        help="print version and exit")
    args = parser.parse_args(argv)
    if args.version:
        print(f"tradebeast {__version__}")
        return 0
    cfg = load_config(args.config)
    specs = resolve_specs(cfg)
    beast = TradeBeast(specs)
    if args.dump_tools:
        return asyncio.run(_dump_tools(beast))
    asyncio.run(_serve(beast))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
