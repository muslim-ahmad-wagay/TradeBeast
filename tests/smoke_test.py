#!/usr/bin/env python3
"""Smoke test for TradeBeast.

Spawns tradebeast.py as an MCP stdio server, lists its tools, and makes
two read-only calls end to end (a CCXT public ticker fetch and the
funding-rates comparison). Exits 0 only if both calls return real data.

Usage:
    ~/workspace/custom-connectors/_shared-venv/bin/python tests/smoke_test.py [--with-bitget]

    --with-bitget   also calls a Bitget read (futures_get_ticker). Requires
                    BITGET_API_KEY / BITGET_SECRET_KEY / BITGET_PASSPHRASE
                    in the environment; otherwise Bitget stays disabled and
                    the flag is ignored.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SHARED_VENV_PY = str(
    Path.home() / "workspace" / "custom-connectors" / "_shared-venv"
    / "bin" / "python")

from mcp import ClientSession, StdioServerParameters  # noqa: E402
from mcp.client.stdio import stdio_client  # noqa: E402


def _proxy_env() -> dict[str, str]:
    return {k: os.environ[k] for k in (
        "HTTPS_PROXY", "https_proxy", "HTTP_PROXY", "http_proxy",
        "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE",
        "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "NO_PROXY", "no_proxy")
        if k in os.environ}


def _text(result) -> str:
    parts = []
    for block in result.content:
        if getattr(block, "type", "") == "text":
            parts.append(block.text)
        else:
            parts.append(str(block))
    return "\n".join(parts)


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--with-bitget", action="store_true")
    args = parser.parse_args()

    env = _proxy_env()
    for var in ("BITGET_API_KEY", "BITGET_SECRET_KEY", "BITGET_PASSPHRASE"):
        if var in os.environ:
            env[var] = os.environ[var]

    params = StdioServerParameters(
        command=SHARED_VENV_PY, args=[str(HERE / "tradebeast.py")], env=env)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"tools listed: {len(tools.tools)}")
            names = {t.name for t in tools.tools}
            assert "ccxt_get_tickers" in names, "ccxt_get_tickers missing"
            assert "funding_compare_funding_rates" in names, (
                "funding_compare_funding_rates missing")
            assert "tradebeast_status" in names, "tradebeast_status missing"

            status = await session.call_tool("tradebeast_status", {})
            print("status:", _text(status)[:400])

            print("--- ccxt_get_tickers bitget BTC/USDT ---")
            tick = await session.call_tool(
                "ccxt_get_tickers",
                {"exchange": "bitget", "symbols": ["BTC/USDT"]})
            tick_text = _text(tick)
            print(tick_text[:600])
            assert not tick.is_error, "ccxt_get_tickers errored"
            assert "BTC/USDT" in tick_text, "ticker result missing BTC/USDT"

            print("--- funding_compare_funding_rates IDOL/USDT:USDT ---")
            fund = await session.call_tool(
                "funding_compare_funding_rates",
                {"symbols": ["IDOL/USDT:USDT"]})
            fund_text = _text(fund)
            print(fund_text[:800])
            assert not fund.is_error, "funding compare errored"
            assert "IDOL" in fund_text, "funding result missing IDOL"

            if args.with_bitget and "bitget_futures_get_ticker" in names:
                print("--- bitget_futures_get_ticker IDOLUSDT ---")
                bg = await session.call_tool(
                    "bitget_futures_get_ticker",
                    {"symbol": "IDOLUSDT", "productType": "USDT-FUTURES"})
                bg_text = _text(bg)
                print(bg_text[:600])
                assert not bg.is_error, "bitget ticker errored"
                assert "IDOL" in bg_text, "bitget result missing IDOL"

    print("SMOKE TEST PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
