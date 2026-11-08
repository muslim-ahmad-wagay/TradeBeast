# 🦁 TradeBeast

> **The Ultimate Crypto Trading Beast — every crypto MCP fused into one unstoppable trading machine.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-stdio-green.svg)](https://modelcontextprotocol.io/)
[![Tools](https://img.shields.io/badge/Tools-295-orange.svg)](docs/TOOLS.md)
[![Bitget](https://img.shields.io/badge/Bitget-official-00D1C1.svg)](https://www.bitget.com/)

One MCP server. **295 tools. 13 sources.** Plug it into Claude Desktop, Muse, or any MCP client and your AI can see the whole crypto market at once — tickers and order books from 100+ exchanges, Binance technicals, Smart Money Concepts, Hyperliquid flow, derivatives intel, funding rates, TradingView screeners, a local ML forecast, and your own Bitget account.

No more juggling a dozen MCP servers. **Feed the beast once, and it hunts everywhere.**

---

## ⚡ What the beast can do

| Power | Source | Tools |
|---|---|---|
| Public market data — tickers, OHLCV, order books, trades on 100+ exchanges | CCXT (official) | 12 |
| Binance technical signals — swings, slopes, volume, multi-timeframe | Trading Signals | 11 |
| Derivatives intel — OI, liquidations, whales, CVD, positioning regimes | LiquidVision (hosted) | 41 |
| Smart Money Concepts — market structure, order blocks, FVGs, sweeps | SMC | 5 |
| Hyperliquid candles + structure | TradeFloor | 3 |
| Market microstructure — FVGs, liquidity zones, order blocks | Microstructure | 5 |
| RSI divergence detection + scanning | RSI Divergence | 2 |
| Full technical analysis — 54 indicators, patterns, regime, sentiment | Technical Analysis | 54 |
| 78 indicators + strategies — MACD, Ichimoku, Bollinger, ATR, VWAP… | Crypto Indicators | 78 |
| Your Bitget account — positions, orders, fills, funding, order place/cancel | Bitget (official) | 41 |
| Cross-exchange funding-rate comparison | Funding Rates | 1 |
| TradingView screeners, technicals, multi-timeframe, backtests | TradingView | 39 |
| Local 4h ML price forecast | Kronos | 2 |
| Beast health check | TradeBeast | 1 |
| **Total** | | **295** |

Every tool is namespaced by source, so there are no collisions and no guessing: `ccxt_get_tickers`, `bitget_futures_get_positions`, `tv_get_technical_analysis`, `funding_compare_funding_rates`, `kronos_forecast`, `lv_get_liquidation_cascades`, `ind_calculate_macd_strategy`…

Full catalog: **[docs/TOOLS.md](docs/TOOLS.md)** (generated from the live server).

---

## 🚀 Quickstart

```bash
git clone https://github.com/<you>/TradeBeast.git
cd TradeBeast

python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Run it (stdio MCP server — plug it into any MCP client)
.venv/bin/python tradebeast.py
```

Check what the beast sees:

```bash
.venv/bin/python tradebeast.py --dump-tools   # prints the full tool catalog as JSON
```

### First run, no keys needed

TradeBeast starts cleanly with **zero credentials**. Bitget and Kronos are optional sub-servers:

- **Bitget** stays off unless `BITGET_API_KEY`, `BITGET_SECRET_KEY` and `BITGET_PASSPHRASE` are in the environment. No keys are ever read from a file, written to disk, or logged by TradeBeast.
- **Kronos** stays off unless a local Kronos forecast server answers `http://127.0.0.1:8901/health`. The model (~200MB) is never bundled in this repo.

With neither, you still get **254 tools** out of the box.

### Enable Bitget (optional)

```bash
export BITGET_API_KEY="..."
export BITGET_SECRET_KEY="..."
export BITGET_PASSPHRASE="..."
.venv/bin/python tradebeast.py
```

Use a **trade-only** API key (no withdraw permission). TradeBeast never exposes withdraw, transfer, margin trading, copy-follow, convert execution, broker writes, leverage changes, or earn actions — those tools are blocked at the aggregator and never appear in the tool list.

### Enable Kronos (optional)

Run your local Kronos forecast server, then start TradeBeast. Override the URL with `TRADEBEAST_KRONOS_URL=http://127.0.0.1:8901`.

---

## 🔌 Connect it

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "tradebeast": {
      "command": "/absolute/path/to/TradeBeast/.venv/bin/python",
      "args": ["/absolute/path/to/TradeBeast/tradebeast.py"],
      "env": {
        "HTTPS_PROXY": "http://your-proxy:3128",
        "NODE_EXTRA_CA_CERTS": "/path/to/ca-bundle.pem"
      }
    }
  }
}
```

### Muse / any MCP client

Point it at the same command as a stdio server. Example `mcp.json`:

```json
{
  "mcpServers": {
    "tradebeast": {
      "command": "python",
      "args": ["tradebeast.py"],
      "cwd": "/absolute/path/to/TradeBeast"
    }
  }
}
```

With Bitget enabled, add the three `BITGET_*` variables to `env` (never commit them).

---

## 🧠 How it works

```
                        ┌─────────────────────┐
                        │   Your MCP client   │
                        │ Claude / Muse / …   │
                        └──────────┬──────────┘
                                   │ stdio (one connection)
                        ┌──────────┴──────────┐
                        │     TRADEBEAST      │
                        │  aggregate + route  │
                        │  295 tools, 1 wire  │
                        └──────────┬──────────┘
           ┌──────────┬───────────┼───────────┬───────────┐
           ▼          ▼           ▼           ▼           ▼
        ccxt ···   signals    liquidvision   smc ···   tradefloor
        micro ···    rsi      technical-     crypto-    bitget
                              analysis      indicators  (opt-in)
        funding ··· tradingview ··· kronos (opt-in, local)
```

- **Aggregate at startup** — TradeBeast spawns every enabled sub-server, lists its tools (with a per-server timeout), and re-exposes them under a source prefix. A dead sub-server is logged and skipped; the beast keeps serving the rest.
- **Route calls unchanged** — a tool call goes to its owning sub-server and the result comes back verbatim.
- **Self-healing** — if a sub-server connection drops mid-call (egress hiccups, the trading-signals server crashing on a bad Binance response), TradeBeast reconnects it once and retries the call once.
- **No blind retries on orders** — order place/cancel tools are never auto-retried: a lost response might mean the order already executed. On failure the beast reconnects and tells you to check positions/orders before retrying.

---

## 🛡️ Safety

- **Read-only by default.** 12 of 13 sources are pure market data and analysis. The only tools that can move money are Bitget spot/futures order place/cancel — and only when you opt in with your own keys.
- **Blocked, not just undocumented:** withdraw, transfer, margin borrow/repay/trade, copy-follow, convert execution, broker API-key/sub-account tools, leverage changes, and earn actions are filtered out of the tool list entirely.
- **No credentials in this repo.** No keys, secrets, passwords, or tokens anywhere — grep it yourself. Bitget credentials come from environment variables only.
- **No trading without you.** TradeBeast places no order on its own. Every order tool is an explicit tool call your agent makes — keep your own rules (leverage caps, stop-losses, daily limits) on top.
- **This is not financial advice.** The beast shows you the market; it does not tell you what to buy.

---

## ⚙️ Configuration

Copy `config.example.json` to `config.json` to pick which sub-servers run and override their launch commands:

```json
{
  "kronos_url": "http://127.0.0.1:8901",
  "servers": {
    "bitget": { "enabled": true },
    "kronos": { "enabled": true },
    "technical_analysis": { "enabled": false }
  }
}
```

Environment toggles also work: `TRADEBEAST_DISABLE_<name>=1` (e.g. `TRADEBEAST_DISABLE_TA=1`), `TRADEBEAST_KRONOS_URL=…`, `TRADEBEAST_CONFIG=/path/to/config.json`.

Sub-server paths in the defaults assume the standard layout (`~/workspace/custom-connectors/...` and `~/workspace/tradingview-mcp/`). If your installs live elsewhere, point `config.json` at them — see `config.example.json` for every command.

---

## 🧪 Tests

```bash
# Full smoke test: lists tools, then calls ccxt_get_tickers + funding_compare_funding_rates end to end
~/workspace/custom-connectors/_shared-venv/bin/python tests/smoke_test.py

# Also exercise the Bitget read path (needs BITGET_* env vars)
BITGET_API_KEY=... BITGET_SECRET_KEY=... BITGET_PASSPHRASE=... \
  ~/workspace/custom-connectors/_shared-venv/bin/python tests/smoke_test.py --with-bitget
```

---

## 🤝 Contributing

PRs welcome — new sub-servers, better routing, more tests. To add a source:

1. Add its spec to `_default_specs()` in `tradebeast.py` (command, prefix, allowlist).
2. Add it to `config.example.json` and the README table.
3. Run `tradebeast.py --dump-tools` and regenerate `docs/TOOLS.md`.
4. Never add a tool that moves funds without an allowlist entry and a note in the Safety section.

---

## 💛 Support

TradeBeast is free and open source (MIT). If it helps you trade smarter, tips keep the beast fed:

**USDT (TRC20):** `TPWtGkxHsrNtUY7cAuPtZzSX7otzE44zyo`

Donations are voluntary and non-refundable. Never send funds to any other address claiming to be TradeBeast.

---

## 📜 License

MIT — see [LICENSE](LICENSE).
