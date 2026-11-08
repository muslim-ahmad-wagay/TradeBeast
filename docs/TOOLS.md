# TradeBeast Tool Catalog

Generated from the live server (`tradebeast.py --dump-tools`). Total: **295 tools** across 13 sources.

Tool names are prefixed by source, e.g. `ccxt_get_tickers`, `bitget_futures_get_positions`, `tv_get_technical_analysis`, `funding_compare_funding_rates`, `kronos_forecast`.

## Sources

| Prefix | Source | Tools | Notes |
|---|---|---|---|
| `ccxt_` | CCXT (100+ exchanges, public market data) | 12 | Public market data only; trading/funds tiers off. `fetch_route` is no longer listed by the server. |
| `signals_` | Trading Signals (Binance TA) | 11 | Binance public TA. Can crash on a failed Binance call; TradeBeast reconnects it once. |
| `lv_` | LiquidVision (derivatives intel, hosted) | 41 | Hosted at liquidvision.app/mcp. Free tier; history/alerts need a key (not exposed). |
| `smc_` | SMC (Smart Money Concepts, Yahoo OHLCV) | 5 | Yahoo OHLCV + local SMC. Do not use for CYBER (Yahoo data unreliable). |
| `tradefloor_` | TradeFloor (Hyperliquid candles) | 3 | Hyperliquid candles. Bare coin names, never BTCUSDT. |
| `micro_` | Microstructure (Binance vision spot klines) | 5 | Binance vision spot klines. Spot-only. |
| `rsi_` | RSI Divergence Detector | 2 | Binance public spot klines. Read-only. |
| `ta_` | Technical Analysis (GearTrade, 54 tools) | 54 | GearTrade. ~20s per call. |
| `ind_` | Crypto Indicators (78 indicators) | 78 | Slash pairs (BTC/USDT). |
| `bitget_` | Bitget (official, reads + order place/cancel) | 41 | Official. Reads + spot/futures order place/cancel only. Withdraw/transfer/margin/copy/convert/broker/leverage tools are BLOCKED and never listed. Needs BITGET_API_KEY / BITGET_SECRET_KEY / BITGET_PASSPHRASE in the environment. |
| `funding_` | Funding Rates (cross-exchange funding comparison) | 1 | Cross-exchange funding comparison. Read-only, keyless. |
| `tv_` | TradingView (screener, technicals, backtests) | 39 | Screener + technicals. Some tools need a TradingMCP API key. |
| `kronos_` | Kronos (local 4h ML forecast) | 2 | Native tools calling the local Kronos forecast server (never bundled). Only when /health answers. |

## Every tool


### `bitget_`

- `bitget_broker_get_info` — bitget Get broker account information and commission data. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_convert_get_history` — bitget Get conversion or BGB sweep history. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_convert_get_quote` — bitget Get supported convert currencies or quoted conversion price. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_copy_get_orders` — bitget Query copy-trading historical orders. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_copy_get_positions` — bitget Get current or historical copy-trading positions/orders. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_copy_get_traders` — bitget Get copy-trading trader list and configuration candidates. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_futures_cancel_orders` — bitget Cancel futures orders by order id, batch ids, or cancel-all mode. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_futures_get_candles` — bitget Get futures candles from trade/index/mark price sources. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_futures_get_contracts` — bitget Get futures contract configuration details. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_futures_get_depth` — bitget Get futures orderbook depth with precision levels. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_futures_get_fills` — bitget Get futures fills and fill history records. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_futures_get_funding_rate` — bitget Get current or historical funding rates for a futures symbol. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_futures_get_open_interest` — bitget Get open interest for a futures contract. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_futures_get_orders` — bitget Query futures orders by id, open status, or history. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_futures_get_positions` — bitget Get current or historical futures positions. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_futures_get_ticker` — bitget Get futures ticker for one symbol or all symbols in product type. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_futures_get_trades` — bitget Get recent or historical futures trade records. Public endpoint. Rate limit: 10 req/s per IP.
- `bitget_futures_place_order` — bitget Place one or more futures orders with optional TP/SL. CAUTION Executes real trades. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_get_account_assets` — bitget Get spot/futures/funding/all account balances. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_get_account_bills` — bitget Get account bill records for spot or futures account. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_get_deposit_address` — bitget Get deposit address for coin and optional chain. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_get_transaction_records` — bitget Get deposit, withdrawal, or transfer records. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_margin_get_assets` — bitget Get crossed or isolated margin assets and risk metrics. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_margin_get_orders` — bitget Query margin orders (open/history/order detail). Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_margin_get_records` — bitget Get borrow/repay/interest/liquidation records for margin accounts. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_p2p_get_merchants` — bitget Get P2P merchant list or specific merchant details. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_p2p_get_orders` — bitget Get P2P order list or advertisement list. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_cancel_orders` — bitget Cancel one or more spot orders by id, batch ids, or symbol-wide cancel. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_cancel_plan_orders` — bitget Cancel one or multiple spot plan orders. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_get_candles` — bitget Get K-line data for spot trading pair. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_spot_get_depth` — bitget Get orderbook depth for a spot trading pair. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_spot_get_fills` — bitget Get spot fills for order execution details. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_get_orders` — bitget Query spot order detail, open orders, or history orders. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_get_plan_orders` — bitget Get current or historical spot plan orders. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_get_symbols` — bitget Get spot symbol info or coin chain info. Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_spot_get_ticker` — bitget Get real-time ticker data for spot trading pair(s). Public endpoint. Rate limit: 20 req/s per IP.
- `bitget_spot_get_trades` — bitget Get recent or historical trade records for spot symbol. Public endpoint. Rate limit: 10 req/s per IP.
- `bitget_spot_modify_order` — bitget Cancel and replace a spot order atomically. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_place_order` — bitget Place one or more spot orders. CAUTION Executes real trades. Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_spot_place_plan_order` — bitget Create or modify spot plan order (trigger order). Private endpoint. Rate limit: 10 req/s per UID.
- `bitget_system_get_capabilities` — bitget Return machine-readable server capabilities and module availability for agent planning.

### `ccxt_`

- `ccxt_call_implicit_get` — ccxt Call an exchange-specific implicit REST endpoint over HTTP GET, for data the unified API does not cover. Pass the implicit method name in the "method" argument (e.g. "publicGetTickerPrice"); these are exchange-specific — find them with describe_method {"query": ..., "exchange": ...} (its results list the name to pass here). The response is the raw exchange payload. Consult the exchange API reference (describe_exchange .urls.doc) and the ccxt manual: https://docs.ccxt.com/
- `ccxt_call_read_method` — ccxt Escape hatch covering every unified read method not served by a dedicated tool (fetchFundingRate, fetchLedger, fetchOpenInterest, fetchLiquidations, fetchEvent, fetchSettlements, …). Only fetch*/load* methods are accepted — writes are structurally rejected. Get the signature first with describe_method. Docs: https://docs.ccxt.com/
- `ccxt_describe_exchange` — ccxt One exchange's supported unified methods, market types, timeframes, required credential fields, sandbox availability and documentation URLs. Per-method detail lives in describe_method.
- `ccxt_describe_method` — ccxt Search unified method names by keyword, or get one method's signature and parameter documentation. With "exchange" it adds that exchange's own docs (including supported params.* keys and links to the exchange API reference), per-market-type feature support, and searches its implicit (exchange-specific) endpoints too. Full ccxt manual: https://docs.ccxt.com/
- `ccxt_get_ohlcv` — ccxt Historical OHLCV candlestick data for a symbol and timeframe. Rows are timestampMs, open, high, low, close, volume. Page back with "since"; "params.until" bounds the end.
- `ccxt_get_orderbook` — ccxt Current order book (bids and asks) for one unified symbol.
- `ccxt_get_safety_status` — ccxt What this server is currently allowed to do: configured accounts (names only — never credentials), enabled capability tiers, caps, sandbox/live environments, journal location, unresolved order intents, and any configuration problems.
- `ccxt_get_tickers` — ccxt 24h price tickers for one or more unified symbols on an exchange (outcome handles on prediction exchanges).
- `ccxt_get_trades` — ccxt Recent public trades for one unified symbol.
- `ccxt_list_exchanges` — ccxt List every exchange this server supports (built from ccxt.exchanges at runtime), with name, websocket and prediction-market availability. Filter by a name query or by support for a unified method.
- `ccxt_search_events` — ccxt Search events on a prediction-market exchange (polymarket, kalshi, limitless, myriad, hyperliquid with prediction=true). A scoping filter is required: query, tags, or params.eventId/params.slug. Returns events with their markets and outcome handles — outcome handles are what you pass as the symbol to get_tickers/get_orderbook/create_order on prediction exchanges.
- `ccxt_search_markets` — ccxt Search and filter the markets of one exchange (by text, base, quote, settle currency, market type), paginated. Use this to resolve unified symbols — there is deliberately no list-all-markets tool. On prediction exchanges use search_events instead.

### `funding_`

- `funding_compare_funding_rates` — funding 
    Compare current funding rates for multiple symbols across specified exchanges.

    Parameters:
        symbols (Liststr): List of trading pairs (e.g., "BTC/USDT:USDT", "ETH/USDT:USDT").
        exchanges (Liststr, optional): List of exchanges to compare (e.g., "binance", "bybit").
            Defaults to all supported exchanges (binance, bybit, okx).
        params (Dict, optional): Additional parameters for the API call (e.g., {"type": "swap"}). Defaults to {}.

    Returns:
        str: Markdown table comparing funding rates across exchanges and symbols.

### `ind_`

- `ind_calculate_absolute_price_oscillator` — crypto_indicators Calculate the Absolute Price Oscillator (APO) for a given trading pair using Binance OHLCV data
- `ind_calculate_absolute_price_oscillator_strategy` — crypto_indicators Calculate the Absolute Price Oscillator Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_acceleration_bands` — crypto_indicators Calculate the Acceleration Bands (AB) for a given trading pair using Binance OHLCV data
- `ind_calculate_acceleration_bands_strategy` — crypto_indicators Calculate the Acceleration Bands Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_accumulation_distribution` — crypto_indicators Calculate the Accumulation/Distribution (AD) for a given trading pair using Binance OHLCV data
- `ind_calculate_aroon` — crypto_indicators Calculate the Aroon Indicator for a given trading pair using Binance OHLCV data
- `ind_calculate_aroon_strategy` — crypto_indicators Calculate the Aroon Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_average_true_range` — crypto_indicators Calculate the Average True Range (ATR) for a given trading pair using Binance OHLCV data
- `ind_calculate_awesome_oscillator` — crypto_indicators Calculate the Awesome Oscillator (AO) for a given trading pair using Binance OHLCV data
- `ind_calculate_awesome_oscillator_strategy` — crypto_indicators Calculate the Awesome Oscillator Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_balance_of_power` — crypto_indicators Calculate the Balance of Power (BOP) for a given trading pair using Binance OHLCV data
- `ind_calculate_balance_of_power_strategy` — crypto_indicators Calculate the Balance of Power Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_bollinger_bands` — crypto_indicators Calculate the Bollinger Bands (BB) for a given trading pair using Binance OHLCV data
- `ind_calculate_bollinger_bands_strategy` — crypto_indicators Calculate the Bollinger Bands Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_bollinger_bands_width` — crypto_indicators Calculate the Bollinger Bands Width (BBW) for a given trading pair using Binance OHLCV data
- `ind_calculate_chaikin_money_flow` — crypto_indicators Calculate the Chaikin Money Flow (CMF) for a given trading pair using Binance OHLCV data
- `ind_calculate_chaikin_money_flow_strategy` — crypto_indicators Calculate the Chaikin Money Flow Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_chaikin_oscillator` — crypto_indicators Calculate the Chaikin Oscillator (CMO) for a given trading pair using Binance OHLCV data
- `ind_calculate_chande_forecast_oscillator` — crypto_indicators Calculate the Chande Forecast Oscillator (CFO) for a given trading pair using Binance OHLCV data
- `ind_calculate_chande_forecast_oscillator_strategy` — crypto_indicators Calculate the Chande Forecast Oscillator Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_chandelier_exit` — crypto_indicators Calculate the Chandelier Exit (CE) for a given trading pair using Binance OHLCV data
- `ind_calculate_commodity_channel_index` — crypto_indicators Calculate the Commodity Channel Index (CCI) for a given trading pair using Binance OHLCV data
- `ind_calculate_donchian_channel` — crypto_indicators Calculate the Donchian Channel (DC) for a given trading pair using Binance OHLCV data
- `ind_calculate_double_exponential_moving_average` — crypto_indicators Calculate the Double Exponential Moving Average (DEMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_ease_of_movement` — crypto_indicators Calculate the Ease of Movement (EMV) for a given trading pair using Binance OHLCV data
- `ind_calculate_ease_of_movement_strategy` — crypto_indicators Calculate the Ease of Movement Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_exponential_moving_average` — crypto_indicators Calculate the Exponential Moving Average (EMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_force_index` — crypto_indicators Calculate the Force Index (FI) for a given trading pair using Binance OHLCV data
- `ind_calculate_force_index_strategy` — crypto_indicators Calculate the Force Index Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_ichimoku_cloud` — crypto_indicators Calculate the Ichimoku Cloud for a given trading pair using Binance OHLCV data
- `ind_calculate_ichimoku_cloud_strategy` — crypto_indicators Calculate the Ichimoku Cloud Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_kdj` — crypto_indicators Calculate the Random Index (KDJ) for a given trading pair using Binance OHLCV data
- `ind_calculate_kdj_strategy` — crypto_indicators Calculate the KDJ Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_keltner_channel` — crypto_indicators Calculate the Keltner Channel (KC) for a given trading pair using Binance OHLCV data
- `ind_calculate_macd_strategy` — crypto_indicators Calculate the MACD Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_mass_index` — crypto_indicators Calculate the Mass Index (MI) for a given trading pair using Binance OHLCV data
- `ind_calculate_momentum_strategy` — crypto_indicators Calculate the Momentum Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_money_flow_index` — crypto_indicators Calculate the Money Flow Index (MFI) for a given trading pair using Binance OHLCV data
- `ind_calculate_money_flow_index_strategy` — crypto_indicators Calculate the Money Flow Index Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_moving_average_convergence_divergence` — crypto_indicators Calculate the MACD for a given trading pair using Binance OHLCV data
- `ind_calculate_moving_max` — crypto_indicators Calculate the Moving Max (MMAX) for a given trading pair using Binance OHLCV data
- `ind_calculate_moving_min` — crypto_indicators Calculate the Moving Min (MMIN) for a given trading pair using Binance OHLCV data
- `ind_calculate_moving_standard_deviation` — crypto_indicators Calculate the Moving Standard Deviation (MSTD) for a given trading pair using Binance OHLCV data
- `ind_calculate_moving_sum` — crypto_indicators Calculate the Moving Sum (MSUM) for a given trading pair using Binance OHLCV data
- `ind_calculate_negative_volume_index` — crypto_indicators Calculate the Negative Volume Index (NVI) for a given trading pair using Binance OHLCV data
- `ind_calculate_negative_volume_index_strategy` — crypto_indicators Calculate the Negative Volume Index Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_on_balance_volume` — crypto_indicators Calculate the On-Balance Volume (OBV) for a given trading pair using Binance OHLCV data
- `ind_calculate_parabolic_sar` — crypto_indicators Calculate the Parabolic SAR (PSAR) for a given trading pair using Binance OHLCV data
- `ind_calculate_parabolic_sar_strategy` — crypto_indicators Calculate the Parabolic SAR Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_percentage_price_oscillator` — crypto_indicators Calculate the Percentage Price Oscillator (PPO) for a given trading pair using Binance OHLCV data
- `ind_calculate_percentage_volume_oscillator` — crypto_indicators Calculate the Percentage Volume Oscillator (PVO) for a given trading pair using Binance OHLCV data
- `ind_calculate_price_rate_of_change` — crypto_indicators Calculate the Price Rate of Change (ROC) for a given trading pair using Binance OHLCV data
- `ind_calculate_projection_oscillator` — crypto_indicators Calculate the Projection Oscillator (PO) for a given trading pair using Binance OHLCV data
- `ind_calculate_projection_oscillator_strategy` — crypto_indicators Calculate the Projection Oscillator Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_qstick` — crypto_indicators Calculate the Qstick Indicator for a given trading pair using Binance OHLCV data
- `ind_calculate_relative_strength_index` — crypto_indicators Calculate the Relative Strength Index (RSI) for a given trading pair using Binance OHLCV data
- `ind_calculate_rolling_moving_average` — crypto_indicators Calculate the Rolling Moving Average (RMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_rsi2_strategy` — crypto_indicators Calculate the RSI2 Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_simple_moving_average` — crypto_indicators Calculate the Simple Moving Average (SMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_since_change` — crypto_indicators Calculate the Since Change for a given trading pair using Binance OHLCV data
- `ind_calculate_stochastic_oscillator` — crypto_indicators Calculate the Stochastic Oscillator (STOCH) for a given trading pair using Binance OHLCV data
- `ind_calculate_stochastic_oscillator_strategy` — crypto_indicators Calculate the Stochastic Oscillator Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_triangular_moving_average` — crypto_indicators Calculate the Triangular Moving Average (TRIMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_triple_exponential_average` — crypto_indicators Calculate the Triple Exponential Average (TRIX) for a given trading pair using Binance OHLCV data
- `ind_calculate_triple_exponential_moving_average` — crypto_indicators Calculate the Triple Exponential Moving Average (TEMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_true_range` — crypto_indicators Calculate the True Range (TR) for a given trading pair using Binance OHLCV data
- `ind_calculate_typical_price` — crypto_indicators Calculate the Typical Price for a given trading pair using Binance OHLCV data
- `ind_calculate_typical_price_strategy` — crypto_indicators Calculate the Typical Price Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_ulcer_index` — crypto_indicators Calculate the Ulcer Index (UI) for a given trading pair using Binance OHLCV data
- `ind_calculate_volume_price_trend` — crypto_indicators Calculate the Volume Price Trend (VPT) for a given trading pair using Binance OHLCV data
- `ind_calculate_volume_weighted_average_price` — crypto_indicators Calculate the Volume Weighted Average Price (VWAP) for a given trading pair using Binance OHLCV data
- `ind_calculate_volume_weighted_average_price_strategy` — crypto_indicators Calculate the VWAP Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_volume_weighted_moving_average` — crypto_indicators Calculate the Volume Weighted Moving Average (VWMA) for a given trading pair using Binance OHLCV data
- `ind_calculate_volume_weighted_moving_average_strategy` — crypto_indicators Calculate the VWMA Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_vortex` — crypto_indicators Calculate the Vortex Indicator for a given trading pair using Binance OHLCV data
- `ind_calculate_vortex_strategy` — crypto_indicators Calculate the Vortex Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)
- `ind_calculate_williams_r` — crypto_indicators Calculate the Williams R (WILLR) for a given trading pair using Binance OHLCV data
- `ind_calculate_williams_r_strategy` — crypto_indicators Calculate the Williams R Strategy for a given trading pair using Binance OHLCV data. Outputs: -1 (SELL), 0 (HOLD), 1 (BUY)

### `kronos_`

- `kronos_forecast` — kronos 4h close-price forecast from the local Kronos ML model. Arguments: {"symbol": "IDOL/USDT"}. Takes up to ~3 minutes (the model runs in a worker).
- `kronos_health` — kronos Health check of the local Kronos forecast server.

### `lv_`

- `lv_ask` — liquidvision ONE CALL instead of five: ask in plain words ('where is leverage stacked on BTC',
    'why did ETH drop', 'is SOL funding crowded', 'biggest whales near liquidation') and get
    `answer`: short statements with the numbers in them, `facts`: the same numbers as JSON,
    `sources`: which endpoints were read and how old their data is, `caveats`. The question is
    read for its topics (liquidations, funding, open interest, whales, levels, sentiment;
    English or Russian) and only those endpoints are fetched. No model involved: facts, not
    opinion, so you do the judging. Free, no key. For the base rate of the current state
    call get_precedents; for a narrative with an LLM call explain_market.
- `lv_explain_market` — liquidvision AI risk-intelligence answer: ask e.g. 'Why did BTC drop 4%?' and get a
    concise grounded explanation (liquidation cascades, funding extremes, where
    the positions sit, next risk zone) computed from live derivatives data
    across 13 venues (CEXs, Hyperliquid and GMX).
- `lv_get_accuracy` — liquidvision measured The public accuracy audit: our open interest and funding vs Binance, Bybit, OKX and
    Hyperliquid's own endpoints, sampled every 10 min (diff %, snapshot age, 24h mean/max), plus how
    the modeled liquidation map scored against realized liquidations. Read this before trusting
    any number here with money.
- `lv_get_arbitrum_perps` — liquidvision Arbitrum perps board: GMX v2 open interest per coin and its share of every
    tracked venue, GMX funding next to the CEX median (8h basis), on-chain
    liquidations over 24h. Ask this for 'how is Arbitrum positioned vs CEXs'.
- `lv_get_cash_flows` — liquidvision Derivatives cash flow per exchange: net USD into/out of open interest
    over 1h/4h/24h windows, per core symbol. Positive = money flowing in.
- `lv_get_cvd` — liquidvision Cumulative volume delta split by trade size (retail <$10K, mid <$100K,
    large <$1M, whale >$1M). Whale-vs-retail divergence is the usual smart-money reading; buckets
    are per published row and only Binance aggregates taker orders, so compare buckets within one
    exchange (exchange=binance) rather than across venues.
- `lv_get_detective_events` — liquidvision measured Detective: what the watched large holders did. Private wallets with a large
    share of a token's supply (Ethereum, Solana) and Hyperliquid accounts with a large share of
    a contract's open interest are watched live. Event types: to_exchange (a watched wallet sent
    tokens to a recognised exchange, custodian, market maker, DEX pool or bridge: a possible sale,
    reported at any size), large_move (at least $100k to an address we do not recognise),
    hl_position (a watched Hyperliquid position opened, closed or changed by a quarter and $1M+).
    Each event carries the sender's share of supply when it was added to the list, the destination
    label and its source, amount, best-effort USD and an explorer link. Filters: hours (1-720),
    chain (ethereum|solana|hyperliquid), type, symbol (coin). The watch list itself: GET
    https://liquidvision.app/api/v1/detective/watch.
- `lv_get_footprint` — liquidvision measured Footprint chart data: for each candle, taker BUY and taker SELL volume in
    USD and the trade count at each of 30 price levels, from the archived trade streams of
    Binance, Bybit, OKX, Bitget and Gate. Use it to see at which prices aggressive buyers
    or sellers were absorbed; for the net flow over time by trade size use get_cvd. symbol:
    BTCUSDT, ETHUSDT or SOLUSDT only. minutes: look-back window, 15 to 10080. step: candle
    size in minutes, 1 to 240.
- `lv_get_funding_arbitrage` — liquidvision measured Funding carry screener on REALIZED numbers: for each coin, the venue pair a desk
    would put on (short where funding is richest, long where it is cheapest) and what that pair
    actually earned from funding over the last 7 and 30 days from our hourly archive, annualized;
    positive_share_7d = share of the week's hours the pair was net positive (0.5 is a coin flip);
    current_spread_apr = the same pair right now; mark_gap_bps = short-venue mark over long-venue
    mark (positive = entry in your favour). Use get_funding_dispersion for the live spread across
    all venues. Everything is gross: before taker fees, basis moves and two margin accounts.
    Not financial advice.
- `lv_get_funding_dispersion` — liquidvision Coins ranked by how far funding disagrees ACROSS exchanges.

    For each coin: the spread in APR points between the venue charging the most
    and the one paying the most, plus which venue to hold the long on and which
    to hold the short on. Every leg is annualized with its own settlement cycle
    (1h / 4h / 8h), and the ranking uses the median rate over `window` minutes
    rather than the latest print, which is noisy for hourly contracts.
- `lv_get_funding_history` — liquidvision measured Funding rate over time for one contract, one row per venue per time bucket:
    ts (ms), exchange, funding_rate (per settlement interval, a fraction), mark_price and
    funding_hours (that contract's interval: 1, 4 or 8). Annualize as rate * 8760 / funding_hours.
    This is the LIVE predicted rate sampled over time; for the rates actually paid at each
    settlement (2 years back) use get_funding_settlements. symbol: BASEUSDT. minutes: 5 to 20160.
- `lv_get_funding_rates` — liquidvision Latest perpetual funding rates and mark prices for every tracked
    exchange/symbol pair. Positive rate = longs pay shorts.
- `lv_get_funding_settlements` — liquidvision Settled funding rates, one row per settlement, from Binance and Bybit
    history — up to 730 days for any pool coin (e.g. BTCUSDT). The backtest
    series; get_funding_history is the live 10-second archive since July 2026.
- `lv_get_hip3_markets` — liquidvision measured The HIP-3 board: Hyperliquid's builder-deployed perp markets (equity indices,
    stocks, commodities, pre-IPO names; coins named dex:COIN such as xyz:SP500) with what the live
    list alone cannot tell you. Per dex: OI, share, 24h/7d OI change, 24h volume, liquidations.
    Per market: mark, 24h change, OI and its 24h/7d change, 24h volume and turnover (volume/OI),
    hourly funding and APR, liquidations 24h/7d (count, USD, long share), and gap_bps = HIP-3 mark
    vs the mean mark of other venues listing the same underlying (Lighter, Ostium, gTrade).
    `leaders` lists OI growth/decline, funding extremes, most liquidated, widest gap.
    dex filters to one builder (xyz, io, para...); sort = oi | volume | funding | liq | gap | oi_change;
    limit caps the markets list. OI changes are null until the archive is that old (started
    2026-10-31). No key needed.
- `lv_get_hl_account` — liquidvision measured One Hyperliquid account by address: live positions (size, entry, mark,
    liquidation price, distance to liquidation, leverage, unrealized PnL), account value, and
    its archived position snapshots. History depth: 24 h free, 31 days Pro, everything since
    2026-09-27 on Bot (key from the MCP connection's X-API-Key header, or api_key).
- `lv_get_hl_builder_markets` — liquidvision measured Perp markets deployed on Hyperliquid by third parties (HIP-3 builder dexs):
    equity indices, single stocks, commodities and pre-IPO names such as xyz:SP500 or xyz:GOLD.
    For each dex: its markets (coin named dex:COIN), open interest in USD (one side), 24h
    volume, mark price, hourly funding and its APR. These are NOT in get_open_interest or
    get_funding_rates, which cover Hyperliquid's own crypto listing. Live from Hyperliquid,
    cached 2 minutes. No arguments.
- `lv_get_hl_liquidation_map` — liquidvision measured, RISK AHEAD, Hyperliquid REAL open positions on Hyperliquid binned by the
    liquidation price the exchange itself reports: the 10,000 largest accounts plus every account
    that traded since the reader started (~10,000 accounts, ~40-45% of venue open interest, stated
    in covered_long_pct/covered_short_pct). Not a model. Use this for Hyperliquid; use
    get_lighter_liquidation_map for Lighter and get_liquidation_map (modeled) for the CEXs.
    Returns long/short notional per bin, cumulative curves and the largest positions. range: 12h
    | 1d | 3d | 7d | max (±100%, recommended: large accounts run low leverage).
- `lv_get_hl_whales` — liquidvision measured Leveraged positions of the 10,000 largest Hyperliquid accounts with the
    exchange-reported liquidation price, closest to liquidation first (sort='value' = largest
    first). Filters: coin (BTC), side (long|short), min_usd, max_dist_pct. Each row carries the
    account address; pass it to get_hl_account. Snapshot age is in age_s.
- `lv_get_lighter_liquidation_map` — liquidvision measured, RISK AHEAD, Lighter REAL open positions on Lighter (zk perp DEX; crypto plus
    equity indices, stocks, forex, commodities) binned by Lighter's own liquidation price. Not a
    model. Use this for Lighter; get_hl_liquidation_map for Hyperliquid; get_liquidation_map
    (modeled) for the CEXs. Accounts are discovered from the public trade stream, so coverage
    (covered_long_pct/covered_short_pct of venue open interest) grows with time. Returns long/short
    notional per bin, cumulative curves and the largest positions. range: 12h | 1d | 3d | 7d | max.
- `lv_get_lighter_whales` — liquidvision measured Leveraged positions on Lighter with the exchange-reported liquidation price,
    closest to liquidation first (sort='value' = largest first). Filters: coin (BTC), side
    (long|short), min_usd, max_dist_pct. address is the Lighter account index, l1_address the
    wallet. Snapshot age is in age_s.
- `lv_get_liquidation_cascades` — liquidvision measured, PAST Liquidation CASCADES as discrete events: bursts of liquidations detected
    against each coin's own 7-day normal minute. Use it for "when did forced selling snowball and
    what did price do"; not for totals (get_liquidations_summary), raw orders (get_liquidations)
    or open positions at risk (*_liquidation_map). Each event: coin, which side broke, start, how
    long it ran, total and peak-minute USD, multiple of the coin's normal minute, the mark-price
    move during it and in the hour after. market_wide lists minutes when three or more unrelated
    coins cascaded together. hours: display window (baseline is always the last 7 days).
- `lv_get_liquidation_heatmap` — liquidvision modeled, RISK AHEAD, CEX, over time The same estimated CEX map as get_liquidation_map but
    as a time series: gridtb is the estimated USD of leveraged positions with their
    liquidation price in price bin b at time colst (ms), binsb the bin's centre price (240
    bins fitted to the traded range), pricet the close. A level disappears once price trades
    through it. Call this only to see WHEN a cluster formed and whether it survived; for the
    current picture call get_liquidation_map (far smaller answer, split by leverage and exchange).
    The answer is large (about 35,000 numbers). symbol: BASEUSDT. exchange: all | binance | bybit
    | okx. range: 12h | 1d | 3d | 7d.
- `lv_get_liquidation_map` — liquidvision modeled, RISK AHEAD, CEX, now ESTIMATED open leveraged positions on Binance/Bybit/OKX per
    price bin at their liquidation price, from candles and open-interest deltas (the CEXs do not
    publish positions). Current snapshot only; for its evolution over time use
    get_liquidation_heatmap; for REAL positions use get_hl_liquidation_map (Hyperliquid) or
    get_lighter_liquidation_map (Lighter); for what already got liquidated use the PAST tools.
    Returns notional per bin split by leverage tier (5/10/20/25/50/100x) and by exchange, plus
    cumulative long/short curves from the current price outward. exchange: all | binance | bybit |
    okx. range: 12h | 1d | 3d | 7d. It ranks levels ("if price reaches this level, how much is
    there": top quarter of traded levels holds ~30-32% of liquidated USD, chance ~24%); it does NOT
    predict where price will go. Live scoring: get_accuracy.
- `lv_get_liquidations` — liquidvision measured, PAST Individual liquidation ORDERS that already happened (side, price, qty),
    newest first, at most `limit` rows (max 2000). This is the raw feed: use it when you need the
    orders themselves. For totals use get_liquidations_summary; for cascades as events use
    get_liquidation_cascades; for where OPEN positions would be liquidated use a *_liquidation_map
    tool. Market-wide, 500 rows is only a few minutes of a busy hour: pass `symbol` (BTCUSDT)
    and/or `min_usd` to look further back. side=long means a long position was liquidated.
- `lv_get_liquidations_summary` — liquidvision measured, PAST TOTALS of liquidations that already happened: rekt (USD liquidated in the
    last 1h/4h/12h/24h, split long/short), by_symbol and by_exchange over the last `minutes`, and
    series (30-minute buckets). The one to call for "how much was liquidated"; it does not return
    individual orders (get_liquidations) or events (get_liquidation_cascades), and says nothing
    about open positions (the *_liquidation_map tools). Totals are a floor: Binance and Bitget
    throttle their feeds. side=long means longs were liquidated. minutes: 1 to 1440.
- `lv_get_long_short_ratio` — liquidvision Latest global long/short account ratio per exchange/symbol.
- `lv_get_market_brief` — liquidvision Deterministic market brief for a perp symbol: 24h liquidations (totals,
    by exchange), current funding + 24h extremes per venue, OI by venue with
    1h/4h/24h changes, net position flows, modeled liquidation risk zones
    above/below price, and top-trader positioning. Free, no LLM involved —
    ideal input for your own reasoning.
- `lv_get_microstructure` — liquidvision Cross-venue order book microstructure for BTC, ETH and SOL.

    Per venue: spread in bps, immediately-executable depth in USD and the bid
    share of it, measured over a band narrow enough that every venue's stream
    captured it, each venue around its own mid. Also the basis - how far apart
    venues price the same asset - plus a per-minute spread history.

    Does NOT answer "what moves price 0.5%": the streams only carry the
    innermost levels, so that would be extrapolation, not measurement.
- `lv_get_oi_board` — liquidvision Per-venue open-interest ranking for a perp symbol (e.g. BTCUSDT): OI in
    coins and USD, market share %, 1h/4h/24h OI change % and USD flow, and
    OI / 24h-volume ratio per exchange, plus market totals.
- `lv_get_open_interest` — liquidvision Latest open interest (contracts and USD) per exchange/symbol.
- `lv_get_open_interest_history` — liquidvision measured Open interest over time for one contract, one row per venue per time
    bucket: ts (ms), exchange, oi (coins, one side), oi_usd. Use it to see how positioning
    built up or unwound; for the current snapshot with shares and 1h/4h/24h changes use
    get_oi_board, for every contract at once get_open_interest. symbol: BASEUSDT (BTCUSDT).
    minutes: look-back window, 5 to 20160 (14 days); snapped to a fixed set of windows.
- `lv_get_orderbook_heatmap` — liquidvision measured Resting limit orders over time on ONE exchange: cells of (time bucket, price
    bucket, quantity in coins) from archived order-book snapshots, with price_min, price_max,
    price_step and time_step (seconds) describing the grid. Shows where bid and ask walls
    stood and when they were pulled; not liquidations (see get_liquidation_heatmap for
    those) and not trades (get_footprint). exchange: binance | bybit | okx. symbol: BTCUSDT,
    ETHUSDT or SOLUSDT only. minutes: 1 to 1440.
- `lv_get_positioning_regime` — liquidvision Per-coin positioning regime from price direction crossed with open interest.

    price up + OI up = new longs; price up + OI down = short covering (a rally
    with no new buyers); price down + OI up = new shorts; price down + OI down =
    long flush. Returns a market summary (coins and net OI per regime) plus per
    coin the price change, OI change and current OI over the window.
- `lv_get_precedents` — liquidvision measured When did the market look like this before, and what did price do next?
    Scans our hourly archive for hours whose positioning resembled now (OI change 24h within
    3 pp, funding APR within 15 points and same sign, long share within 5 pp, liquidation
    volume within x2.5), one per day, and returns the 24h and 72h price outcome of those
    look-alikes: count, share that went up, median and quartiles, worst and best, next to the
    unconditional base rate over the same archive. `verdict` says whether the sample is big
    enough to mean anything. Frequencies from our archive (since 2026-09), NOT a forecast.
    Metered: free key (100/day), Pro/Bot, or x402.
- `lv_get_spoofing` — liquidvision Order-book wall lifecycle heuristic: large levels classified as
    active_wall / absorbed / pulled_wall / suspected_spoof based on whether
    trades executed into them before they vanished.
- `lv_get_stocks` — liquidvision Crypto-related equities (COIN, MSTR, miners) and spot BTC/ETH ETF quotes:
    price, day change %, range, volume. ~15-min delayed.
- `lv_get_token_unlocks` — liquidvision Upcoming token unlock events for pool coins, nearest first: next unlock
    timestamp and token amount per public vesting schedule.
- `lv_get_tokenized_stocks` — liquidvision measured Tokenized stocks, indices, ETFs, commodities, FX, rates and pre-IPO names traded as
    PERPS on DEXs (Lighter and Hyperliquid builder markets): one row per underlying (NVDA, TSLA,
    S&P 500, Gold, EUR/USD, Anthropic...) with every venue's mark, open interest, 24 h volume,
    funding APR and the price gap between venues in bps. asset_class filters: equity |
    crypto_equity | etf | index | commodity | fx | rates | preipo. Use get_hl_builder_markets for
    the raw Hyperliquid HIP-3 list by dex.
- `lv_get_top_traders` — liquidvision Top lead traders (OKX copy trading, public data): total PnL, win rate,
    AUM, copiers, live open positions (pair, side, leverage, entry, uPnL) and
    recently closed trades with realized PnL.
- `lv_list_history_packages` — liquidvision measured Monthly Parquet history packages for backtests: liquidations (11 venues), funding hourly and
    settlements, open interest hourly, Hyperliquid and Lighter positions with liquidation prices — one file per
    dataset per month since 2026-07 with rows, bytes and sha256. Each entry has `url` (download with the API key
    in X-API-Key) and `available` for the caller's tier: Pro = this month and the previous one, Bot = all,
    free = none (use get_history for the last 24 h).
- `lv_list_markets` — liquidvision measured What exists: every venue we track and, for each, the contracts with live open
    interest right now (BASEUSDT symbols), plus the top-100 coin pool. Call this first when unsure
    which symbol or exchange string another tool accepts.

### `micro_`

- `micro_get_fair_value_gaps` — microstructure Detect 3-candle fair value gaps (FVG) with fill/mitigation status.
- `micro_get_liquidity_zones` — microstructure Detect resting-liquidity levels (clusters of equal highs = buy-side, equal lows = sell-side).

    Returns levels sorted by distance from current price, with touch count and whether
    the level has already been swept.
- `micro_get_market_structure` — microstructure Current trend read plus recent break-of-structure (BOS) and change-of-character (CHoCH) events.
- `micro_get_order_blocks` — microstructure Detect order blocks: the last opposite candle before an impulsive move, with mitigation status.
- `micro_get_snapshot` — microstructure One-call snapshot: structure + nearest liquidity + unfilled FVGs + recent order blocks.

### `rsi_`

- `rsi_detect_rsi_divergence` — rsi Check the latest closed candle for a fresh RSI divergence.

    Returns the current price and RSI(14) plus any regular/hidden
    bullish/bearish divergence ending at the latest candle.
- `rsi_scan_rsi_divergences` — rsi Scan the whole candle window for every RSI divergence found.

    Returns counts by type plus the full list (newest first, max 50).

### `signals_`

- `signals_fetchBookData` — signals Fetch real-time order book analysis and liquidity data. Provides comprehensive order book metrics: Best Bid/Ask prices, Mid Price, Spread, Depth Imbalance (buy vs sell pressure), Top 20 highest volume order book levels for both bids and asks. Shows actual market depth with exact buy/sell order quantities and their percentage distribution. Reveals institutional order levels, support/resistance zones, and liquidity walls. Essential for precision entries: detect liquidity gaps, identify whale orders, analyze market maker behavior, and spot potential breakout/breakdown levels based on order book structure and volume distribution.
- `signals_fetchFifteenMinuteCandleHistory` — signals Fetch raw 15-minute candle OHLCV data (last 8 candles). Provides detailed candle analysis: Open/High/Low/Close prices, Volume, 15-minute Volatility percentage ((High-Low)/Close*100), Body Size percentage (candle body relative to total range), Candle Type classification (Bullish/Bearish/Doji), and High-Volatility detection (>1.5x average volatility). Each candle includes timestamp, formatted prices/volumes, and advanced volatility metrics with HIGH-VOLATILITY flagging for exceptional movements exceeding normal thresholds. Critical for rapid 15-minute price movements identification, momentum shifts detection, and spotting high-volatility breakout periods for quick entry/exit decisions.
- `signals_fetchHourCandleHistory` — signals Fetch raw 1-hour candle OHLCV data (last 6 candles). Provides detailed candle analysis: Open/High/Low/Close prices, Volume, 1-hour Volatility percentage ((High-Low)/Close*100), Body Size percentage (candle body relative to total range), and Candle Type classification (Bullish/Bearish/Doji). Each candle includes timestamp, formatted prices/volumes, and comprehensive volatility metrics for hourly trend analysis and major momentum identification. Essential for understanding recent hourly price action, major trend shifts, and identifying significant candle pattern formations for position timing.
- `signals_fetchLongTermSignals` — signals Fetch comprehensive analysis based on 1-hour candles (48 candles, 48-hour lookback). Provides complete technical indicators: RSI(14), Stochastic RSI(14), MACD(12,26,9), Signal(9), Bollinger Bands(20,2), ATR(14), ATR(20), SMA(50), EMA(20), EMA(34), DEMA(21), WMA(20), Momentum(10), Stochastic(14,3,3), CCI(20), ADX(14), +DI, -DI. Includes Fibonacci retracement/extension levels (0%, 23.6%, 38.2%, 50%, 61.8%, 78.6%, 100%, 127.2%, 161.8%), support/resistance detection, candle pattern recognition, volume trend analysis, and 15 recent candles with detailed market overview. Indicators calculated from 48 1-hour candles (48 hours). Primary tool for position timing decisions over extended periods and confirming directional bias.
- `signals_fetchMicroTermSignals` — signals Fetch ultra-fast analysis based on 1-minute candles (60 candles, 1-hour lookback). Provides comprehensive technical indicators: RSI(9), RSI(14), Stochastic RSI(9,14), MACD(8,21,5), Signal(5), Histogram, Bollinger Bands(8,2.0), Stochastic K/D(3,3,3) and (5,3,3), ADX(9), +DI(9), -DI(9), ATR(5,9), CCI(9), Momentum(5,10). Includes ultra-fast moving averages: EMA(3,8,13,21), SMA(8), DEMA(8), WMA(5). Volume analysis: SMA(5), ratio, trend detection. Price changes: 1m/3m/5m percentage changes, volatility(5), true range, support/resistance levels, 15 recent candles. Indicators calculated from 60 1-minute candles (1 hour). Advanced signals: Bollinger position (0-100%), squeeze momentum, pressure index, tick direction. Data quality metrics and market microstructure analysis. TTL: 30 seconds for ultra-fast updates. ESSENTIAL for detecting rapid reversals, momentum shifts, and precision entry/exit timing.
- `signals_fetchOneMinuteCandleHistory` — signals Fetch raw 1-minute candle OHLCV data (last 15 candles). Provides detailed candle analysis: Open/High/Low/Close prices, Volume, 1-minute Volatility percentage ((High-Low)/Close*100), Body Size percentage (candle body relative to total range), and Candle Type classification (Bullish/Bearish/Doji). Each candle includes timestamp, formatted prices/volumes, and volatility metrics for ultra-granular market analysis and immediate momentum detection. Essential for ultra-precise timing, immediate market reactions analysis, minute-by-minute price action monitoring, and detecting rapid momentum shifts for quick entry/exit decisions.
- `signals_fetchShortTermSignals` — signals Fetch comprehensive analysis based on 15-minute candles (144 candles, 36-hour lookback). Provides complete technical indicators: RSI(9), Stochastic RSI(9), MACD(8,21,5), Bollinger Bands(10,2), ATR(9), SMA(50), EMA(8), EMA(21), DEMA(21), WMA(20), Momentum(8), Stochastic(5,3,3), CCI(14), ADX(14), +DI, -DI. Includes Fibonacci retracement/extension levels (0%, 23.6%, 38.2%, 50%, 61.8%, 78.6%, 100%, 127.2%, 161.8%) with 288-candle lookback, support/resistance detection, volume trend analysis (increasing/decreasing/stable), market overview, and 15 recent candles. Indicators calculated from 144 15-minute candles (36 hours), Fibonacci from 288 candles. ROC(3) for 45-minute momentum analysis. PRIMARY TOOL for detecting rapid market movements, momentum shifts, and making precise entry/exit decisions with high-frequency trading signals.
- `signals_fetchSlopeData` — signals Fetch minute-by-minute trend slope analysis from 120 one-minute candles (2 hours). Provides ultra-granular indicators: SMA(15), EMA(15), Price Slope (USD/minute), Momentum(10), VWAP, VMA(15), Volume Momentum(10), Price-Volume Strength correlation. Includes detailed price and volume arrays with timestamps for ultra-granular trend analysis, slope calculation, and immediate momentum shift detection with minute-level precision. 1-minute candles: 15-period moving averages, 10-period momentum, 2-hour lookback window. Essential for precise entry/exit timing, detecting immediate trend changes, and capturing micro-movements in volatile markets.
- `signals_fetchSwingTermSignals` — signals Fetch comprehensive analysis based on 30-minute candles (96 candles, 48-hour lookback). Provides complete technical indicators: RSI(14), Stochastic RSI(14), MACD(12,26,9), Bollinger Bands(20,2), ATR(14), SMA(20), EMA(13), EMA(34), DEMA(21), WMA(20), Momentum(8), Stochastic(14,3,3), CCI(20), ADX(14), +DI, -DI. Includes comprehensive volatility analysis (historical volatility, ATR, volatility percentile), Fibonacci retracement/extension levels (23.6%, 38.2%, 50%, 61.8%, 78.6%, 127.2%, 161.8%, 261.8%), support/resistance detection, volume trend analysis, market overview, and 15 recent candles. Indicators calculated from 96 30-minute candles (48 hours). Essential for medium-term trend analysis, position timing, and bridging signals between different timeframes.
- `signals_fetchThirtyMinuteCandleHistory` — signals Fetch raw 30-minute candle OHLCV data (last 6 candles). Provides detailed candle analysis: Open/High/Low/Close prices, Volume, 30-minute Volatility percentage ((High-Low)/Close*100), Body Size percentage (candle body relative to total range), and Candle Type classification (Bullish/Bearish/Doji). Each candle includes timestamp, formatted prices/volumes, and comprehensive volatility metrics for analysis and pattern recognition. Optimal for analyzing recent 30-minute price patterns, medium-term momentum shifts, and bridging signals between different timeframes.
- `signals_fetchVolumeData` — signals Fetch comprehensive volume analysis with support/resistance levels. Provides pivot point calculations (S1/S2/S3, R1/R2/R3), significant volume spikes detection (1.5x+ above average), comprehensive technical indicators: SMA(20,50,200), EMA(12,26,50), DEMA(21), WMA(20), RSI(14), Stochastic RSI(14), Bollinger Bands(20,2), ATR(14), ADX(14), CCI(20), Momentum(10), volume ratio analysis. Analyzes 220-hour candle data for SMA(200) accuracy, focuses on 96-hour analysis window with 15 recent candles. Reports maximum 56 high-volume trading signals with price/volume correlations. ESSENTIAL for volume validation, liquidity zones identification, support/resistance confirmation, and detecting institutional activity patterns. Critical for confirming entries with volume backing.

### `smc_`

- `smc_smc_find_fair_value_gaps` — smc Find fair value gaps — three-candle imbalances price tends to rebalance.

    Reports each gap's zone, direction, and whether it has been filled. Unfilled
    gaps act as magnets and make natural entry or target zones.

    Returns (JSON mode): {"symbol","interval",
        "fair_value_gaps": {"index","top","bottom","kind","filled",
        "filled_index","time"}}.
- `smc_smc_find_liquidity_sweeps` — smc Find liquidity sweeps — swing highs/lows wicked through and rejected.

    A sweep takes stops resting beyond an obvious swing, then price closes back
    on the original side. Often precedes a reversal, and distinct from a BOS
    (which closes *through* the level).

    Returns (JSON mode): {"symbol","interval",
        "liquidity_sweeps": {"index","swept_level","swept_swing_index",
        "kind","time"}}.
- `smc_smc_find_order_blocks` — smc Find order blocks — the last opposite candle before a structure break.

    Each block is the institutional footprint before an impulsive move, reported
    with its zone (top/bottom), direction, and whether price has since mitigated
    (revisited) it. Unmitigated blocks are the ones traders usually watch.

    Returns (JSON mode): {"symbol","interval",
        "order_blocks": {"index","top","bottom","kind","break_index",
        "mitigated","mitigated_index","time"}}.
- `smc_smc_full_analysis` — smc Run every SMC tool and return one combined, plain-English read.

    Combines market structure, order blocks, fair value gaps, and liquidity
    sweeps into a single narrative plus the current price and bias — the fastest
    way to get a complete picture in one call.

    Returns (JSON mode): {"symbol","interval","last_price","bias",
        "events","order_blocks","fair_value_gaps","liquidity_sweeps"} where each
        list matches the per-tool JSON schema.
- `smc_smc_get_market_structure` — smc Read market structure: swing points, BOS/CHoCH events, and trend bias.

    Returns the chronological sequence of structure breaks and the current
    directional bias (bullish / bearish / neutral) for the requested instrument
    and timeframe.

    Returns (JSON mode): {"symbol", "interval", "bias",
        "events": {"index","price","event","direction","time"},
        "swing_count"}.

### `ta_`

- `ta_accelerator_oscillator` — technical_analysis Bill Williams Accelerator Oscillator - measures acceleration/deceleration of momentum
- `ta_awesome_oscillator` — technical_analysis Bill Williams Awesome Oscillator - shows momentum changes using simple moving averages of the median price
- `ta_calculate_position_setup` — technical_analysis Calculate position size, leverage, margin, and quantity for a trading signal
- `ta_calculate_risk_management` — technical_analysis Calculate stop loss, take profit, and risk/reward ratio for a trading position
- `ta_chande_momentum` — technical_analysis Chande Momentum Oscillator - measures momentum on both sides with range of -100 to +100
- `ta_channels` — technical_analysis Calculate various channel indicators. Supported types:
- keltner_channels: Keltner Channels - EMA-based volatility bands using ATR
- donchian_channels: Donchian Channels - highest high and lowest low bands
- price_channel: Price Channel - similar to Donchian with middle line
- `ta_coppock_curve` — technical_analysis Coppock Curve - combines two ROC periods for identifying major market bottoms and long-term momentum
- `ta_detrended_price` — technical_analysis Detrended Price Oscillator - removes trend from price data to identify cycles and overbought/oversold conditions
- `ta_double_ema` — technical_analysis Double Exponential Moving Average - reduces lag compared to traditional EMA
- `ta_elder_ray` — technical_analysis Elder Ray Index - measures buying and selling pressure using Bull Power and Bear Power
- `ta_fisher_transform` — technical_analysis Fisher Transform - normalizes price data using Gaussian distribution for sharp reversal signals
- `ta_gator_oscillator` — technical_analysis Bill Williams Gator Oscillator - shows convergence/divergence of Alligator lines and identifies trend strength
- `ta_get_External_data` — technical_analysis Get comprehensive external market data including funding rates, open interest, liquidations, whale positions, and top traders for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_Multitimeframe` — technical_analysis Get multi-timeframe trend alignment analysis for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_candlestick_patterns` — technical_analysis Get candlestick pattern detection for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_correlation_analysis` — technical_analysis Get BTC dominance, altcoin correlation with BTC, beta analysis, and market regime for multiple tickers. Useful for understanding market dynamics and diversification.
- `ta_get_divergence` — technical_analysis Get RSI divergence detection for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_indicators` — technical_analysis Get comprehensive technical analysis indicators for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_liquidation_levels` — technical_analysis Get liquidation level analysis with heatmap data from HyperScreener for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_long_short_ratio` — technical_analysis Get long/short ratio analysis with whale positions and top traders data from HyperScreener for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_market_regime` — technical_analysis Get market regime analysis (trending/choppy/volatile) for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_market_sentiment` — technical_analysis Get comprehensive market sentiment analysis using free APIs.

Includes:
- Fear & Greed Index (alternative.me) - Market emotion indicator
- BTC Dominance (CoinGecko) - Altseason indicator
- Funding Rate Summary (Hyperliquid) - Derivatives sentiment

All data from FREE APIs, no API keys required.

Output:
- Individual metrics with interpretations
- Overall sentiment score (0-100)
- Trading recommendation based on combined signals
- `ta_get_market_structure` — technical_analysis Get market structure analysis for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_orderbook_depth` — technical_analysis Get real-time L2 order book depth analysis from Hyperliquid for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_price` — technical_analysis Get latest prices for multiple trading tickers/symbols at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_tier_classification` — technical_analysis Get market breakdown by trader tier (Shrimp to Institutional) for given tickers. Shows count, notional, and wallet addresses per tier with Long/Short breakdown.
- `ta_get_volume_analysis` — technical_analysis Get comprehensive volume analysis for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_volume_profile` — technical_analysis Get volume profile analysis for multiple trading tickers at once (e.g., "BTC", "ETH", "SOL")
- `ta_get_whale_position` — technical_analysis Track positions from specific wallet addresses with labeling support. Can also include top whales from HyperScreener. Supports change detection alerts.
- `ta_hull_ma` — technical_analysis Hull Moving Average - reduces lag while maintaining smoothness for better trend identification
- `ta_kaufman_adaptive_ma` — technical_analysis Adaptive moving average that adjusts smoothing based on market efficiency and volatility
- `ta_know_sure_thing` — technical_analysis Know Sure Thing - combines multiple timeframe ROC calculations for momentum analysis
- `ta_ma_envelope` — technical_analysis Moving Average Envelope for volatility-based support/resistance and overbought/oversold signals
- `ta_mcginley_dynamic` — technical_analysis Adaptive moving average that adjusts to market volatility and reduces lag compared to traditional MAs
- `ta_momentum` — technical_analysis Momentum Indicator - measures the rate of price change over a specified period
- `ta_patterns` — technical_analysis Calculate various pattern recognition indicators. Supported types:
- fractals: Bill Williams Fractals - identifies swing highs and lows
- zigzag: ZigZag Indicator - filters noise to show significant moves
- change_of_character: COC - detects market structure changes
- `ta_percentage_price_oscillator` — technical_analysis Percentage Price Oscillator - MACD expressed as percentage for better cross-asset comparability
- `ta_pivot_points` — technical_analysis Calculate various pivot point levels. Supported types:
- camarilla: Camarilla Pivots - intraday support/resistance levels (requires high, low, close)
- standard: Standard Pivot Points - classic floor trader pivots (requires high, low, close)
- fibonacci_retracement: Fibonacci Retracement - key retracement levels (requires closes array)
- `ta_rainbow_ma` — technical_analysis Multiple moving averages with different periods for comprehensive trend visualization and alignment analysis
- `ta_rate_of_change` — technical_analysis Rate of Change - measures the percentage change in price over a specified period
- `ta_relative_vigor_index` — technical_analysis Relative Vigor Index - compares close vs open momentum to identify trend strength and reversals
- `ta_schaff_trend_cycle` — technical_analysis Schaff Trend Cycle - combines MACD with Stochastic oscillator and double smoothing for early trend signals
- `ta_smoothed_ma` — technical_analysis Smoothed Moving Average - provides smooth trend following with reduced noise
- `ta_stochastic_rsi` — technical_analysis Stochastic RSI - combines RSI with stochastic formula for overbought/oversold signals
- `ta_strength_indicators` — technical_analysis Calculate various strength/power indicators. Supported types:
- bull_bear_power: Bull Bear Power - measures buying vs selling strength
- force_index: Force Index - combines price and volume for trend strength
- center_of_gravity: COG - identifies turning points using weighted prices
- balance_of_power: BOP - measures buyer vs seller control
- `ta_trend_indicators` — technical_analysis Calculate various trend indicators. Supported types:
- supertrend: SuperTrend - ATR-based trend following indicator
- alligator: Bill Williams Alligator - three smoothed MAs for trend
- ichimoku_cloud: Ichimoku Cloud - comprehensive trend system
- vortex: Vortex Indicator - identifies trend direction
- linear_regression: Linear Regression - statistical trend line
- r_squared: R-Squared - measures trend strength/reliability
- `ta_triple_ema` — technical_analysis Triple Exponential Moving Average - further reduces lag and provides smooth trend signals
- `ta_trix` — technical_analysis TRIX - shows the rate of change of a triple exponentially smoothed moving average
- `ta_true_strength_index` — technical_analysis True Strength Index - uses double-smoothed momentum to reduce noise and provide clearer signals
- `ta_ultimate_oscillator` — technical_analysis Ultimate Oscillator - combines three different timeframes to reduce false signals
- `ta_volatility_indicators` — technical_analysis Calculate various volatility indicators. Supported types:
- bollinger_band_width: BB Width - measures Bollinger Band expansion/contraction
- bollinger_percent_b: %B - price position within Bollinger Bands
- chaikin_volatility: Chaikin Volatility - rate of change of trading range
- historical_volatility: HV - annualized standard deviation of returns
- mass_index: Mass Index - identifies trend reversals through range expansion
- ulcer_index: Ulcer Index - measures downside volatility and drawdown risk
- `ta_volume_indicators` — technical_analysis Calculate various volume-based indicators. Supported types:
- chaikin_money_flow: CMF - volume-weighted accumulation/distribution
- chaikin_oscillator: Chaikin Oscillator - A/D line momentum
- volume_oscillator: Volume Oscillator - compares volume MAs
- price_volume_trend: PVT - cumulative volume based on price change
- positive_volume_index: PVI - tracks price on increasing volume days
- volume_roc: Volume Rate of Change - volume momentum
- volume_zone_oscillator: VZO - volume distribution analysis
- money_flow_index: MFI - volume-weighted RSI
- `ta_vwma` — technical_analysis Volume Weighted Moving Average - gives more weight to periods with higher volume
- `ta_weighted_ma` — technical_analysis Weighted Moving Average - gives more weight to recent prices for responsive trend analysis

### `tradebeast_`

- `tradebeast_status` — tradebeast Health of the beast: which sub-servers are up, how many tools each exposes, and the total tool count.

### `tradefloor_`

- `tradefloor_analyze_structure` — tradefloor Read market structure: trend, character shifts (ChoCh) and continuation breaks (BOS).

    Returns the current trend, every structural break in the window with its
    time and price, the last validated swing high and low, the potential swing
    levels a pullback is forming against, and the impulse peak or trough of the
    current leg.

    Give a coin (BTC, ETH, SOL; tokenised equities as xyz:AAPL) to fetch candles
    from Hyperliquid's public endpoint, or pass your own candles, or neither to
    see a worked example on bundled ETH-15m data.

    Set include_candles=true when you intend to DRAW the result: the response
    then carries the candles themselves, on the same time scale as the levels.
- `tradefloor_find_blocks` — tradefloor Find fair value gaps, order blocks and the pullback zones holding them.

    Reports blocks on the current impulse leg, then again per Fibonacci pullback
    zone (discount, equilibrium, premium, golden pocket), and says which zones
    price is sitting in right now.

    Same input options as analyze_structure.
- `tradefloor_find_liquidity_sweeps` — tradefloor Find stop-hunts: breaks that first ran the liquidity resting past a level.

    A sweep is a structural break whose candle pushed through one or more prior
    swing levels before closing back inside. Each result names the sweeping
    candle and every level it took out, which is what separates an engineered
    break from a clean one.

    Same input options as analyze_structure.

### `tv_`

- `tv_advanced_candle_pattern` — tradingview Advanced candle pattern analysis using multi-timeframe data.

    Args:
        exchange: Exchange name (BINANCE, KUCOIN, etc.)
        base_timeframe: Base timeframe for analysis (5m, 15m, 1h, 4h)
        pattern_length: Number of consecutive periods to analyse (2-4)
        min_size_increase: Minimum percentage increase in candle size
        limit: Maximum number of results to return
- `tv_backtest_strategy` — tradingview Backtest a trading strategy on historical data with institutional-grade metrics.

    Args:
        symbol: Yahoo Finance symbol (AAPL, BTC-USD, THYAO.IS, ^GSPC)
        strategy: rsi | bollinger | macd | ema_cross | supertrend | donchian
                  | rsi_pullback | keltner_breakout | triple_ema
                  (rsi_pullback and triple_ema need period >= '1y' for SMA200 warmup)
        period: '1mo', '3mo', '6mo', '1y', '2y'
        initial_capital: Starting capital in USD (default $10,000)
        commission_pct: Per-trade commission % (default 0.1%)
        slippage_pct: Per-trade slippage % (default 0.05%)
        interval: '1d' (daily) or '1h' (hourly)
        include_trade_log: Include full per-trade log (default False)
        include_equity_curve: Include equity curve data points (default False)
- `tv_bitcoin_market_pulse` — tradingview Single-call BTC macro context: price, dominance, total market cap + risk assessment.

    Use this WHENEVER analyzing any cryptocurrency (altcoin or BTC itself) to
    get the broader market frame in one shot. A SOL/ETH/whatever setup looks
    very different when BTC is dumping with rising dominance vs. when alts
    are leading. Calling this once gives Claude the macro context to provide
    Bitcoin-aware commentary alongside the per-coin analysis - without
    chaining 2-3 separate yahoo_price + manual reasoning calls.

    Returns:
      - bitcoin: price, 24h change %, volume, market cap
      - dominance: BTC and ETH market-cap share of total crypto
      - total_market: total crypto mcap + 24h change + active coin count
      - assessment: label (HIGH_RISK / ALT_RISK / ALT_FAVORABLE / OPPORTUNITY_WITH_CAUTION / NEUTRAL) + 1-paragraph reasoning
- `tv_bollinger_scan` — tradingview Scan for assets with low Bollinger Band Width (squeeze detection). Works with crypto and stocks.

    This scans a whole EXCHANGE for squeezes (canonical name is exactly
    `bollinger_scan`; there is no "get_bollinger_band_analysis" tool). For
    the Bollinger read of ONE symbol, call `coin_analysis` instead.

    Example: bollinger_scan(exchange="BINANCE", timeframe="15m", bbw_threshold=0.008)

    Args:
        exchange: Exchange — crypto: KUCOIN, BINANCE, BYBIT, MEXC; stocks: EGX, BIST, NASDAQ, NYSE, BURSA, HKEX, SSE, SZSE, TWSE, TPEX, EPA (Euronext Paris), AMS, BRU, LIS, MIL, LSE, SIX, BME, XETRA, FWB, TSX, TSXV, NSE, BSE (India), IDX (Indonesia)
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M. Typical squeeze thresholds: 15m→0.008, 1h→0.02, 4h→0.04, 1D→0.12
        bbw_threshold: Maximum BBW value to filter (default 0.04)
        limit: Number of rows to return (max 100)

    Returns ``listdict`` on success. On ANY failure returns a structured
    error envelope ``{"error": {"code": ..., "retryable": ...}}``.
- `tv_coin_analysis` — tradingview Get detailed analysis for a specific asset (coin or stock) on specified exchange and timeframe.

    This is the canonical single-symbol technical readout (there is no
    "get_technical_analysis" or "get_technical_summary" tool — use THIS one).
    Use `multi_timeframe_analysis` instead when you need trend alignment
    across several timeframes, and `combined_analysis` when you also want
    news sentiment + headlines in the same call.

    Example: coin_analysis(symbol="BTCUSDT", exchange="BINANCE", timeframe="1h")

    Args:
        symbol: Bare ticker, no exchange prefix — crypto: "BTCUSDT", "ETHUSDT"; stocks: "COMI" (EGX), "THYAO" (BIST), "600519" (SSE), "300251" (SZSE), "2330" (TWSE), "3105" (TPEX)
        exchange: Exchange — crypto: KUCOIN, BINANCE, MEXC; stocks: EGX, BIST, NASDAQ, NYSE, BURSA, HKEX, SSE, SZSE, TWSE, TPEX, EPA (Euronext Paris), AMS, BRU, LIS, MIL, LSE, SIX, BME, XETRA, FWB, TSX, TSXV, NSE, BSE (India), IDX (Indonesia). If the symbol isn't listed there, the error's `listed_on` field names exchanges that do list it.
        timeframe: Time interval (5m, 15m, 1h, 4h, 1D, 1W, 1M)

    Returns:
        Detailed analysis with all indicators and metrics
- `tv_combined_analysis` — tradingview POWER TOOL: TradingView technical analysis + news sentiment + financial news.

    Use this when you want TA AND sentiment AND news for one symbol in a
    single call. For indicators only, `coin_analysis` is faster; for
    cross-timeframe trend alignment use `multi_timeframe_analysis`.

    Example: combined_analysis(symbol="NVDA", exchange="NASDAQ", timeframe="1D")

    Args:
        symbol: Bare ticker, no exchange prefix ("AAPL", "BTCUSDT", "THYAO", "GDX")
        exchange: Exchange (NASDAQ, NYSE, AMEX, NYSEARCA, PCX, BINANCE, KUCOIN, MEXC, BIST, EGX, TWSE, TPEX)
        timeframe: Analysis timeframe (5m, 15m, 1h, 4h, 1D, 1W)
- `tv_compare_strategies` — tradingview Run all 9 strategies (RSI, Bollinger, MACD, EMA Cross, Supertrend, Donchian, RSI Pullback, Keltner Breakout, Triple EMA) and return a ranked leaderboard.

    Args:
        symbol: Yahoo Finance symbol (AAPL, BTC-USD, SPY…)
        period: '1mo', '3mo', '6mo', '1y', '2y'
                (period >= '1y' recommended so rsi_pullback and triple_ema can
                 complete SMA200 warmup; otherwise they contribute zero trades)
        initial_capital: Starting capital in USD (default $10,000)
        interval: '1d' (daily) or '1h' (hourly)
- `tv_consecutive_candles_scan` — tradingview Scan for coins with consecutive growing/shrinking candles pattern.

    Args:
        exchange: Exchange name (BINANCE, KUCOIN, etc.)
        timeframe: Time interval (5m, 15m, 1h, 4h)
        pattern_type: "bullish" (growing candles) or "bearish" (shrinking candles)
        candle_count: Number of consecutive candles to check (2-5)
        min_growth: Minimum growth percentage for each candle
        limit: Maximum number of results to return
- `tv_egx_fibonacci_retracement` — tradingview Fibonacci retracement analysis for EGX stocks.

    Args:
        symbol: EGX stock symbol (e.g., "COMI", "TMGH", "FWRY")
        lookback: Period for swing high/low — "1M", "3M", "6M", "52W", "ALL" (default 52W)
        timeframe: Analysis timeframe (5m, 15m, 1h, 4h, 1D, 1W, 1M — default 1D)
- `tv_egx_index_analysis` — tradingview Analyse an EGX index showing constituent performance with full indicators.

    Args:
        index: EGX30, EGX70, EGX100, SHARIAH33, EGX35LV, TAMAYUZ
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M (default 1D)
        limit: Number of stocks to show in detail (max 100)
- `tv_egx_market_overview` — tradingview Get a comprehensive overview of the Egyptian Exchange (EGX) market.

    Args:
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M (default 1D for stocks)
        limit: Number of stocks per category (max 20)
- `tv_egx_sector_scan` — tradingview Scan EGX stocks by sector. Shows available sectors if none specified.

    Args:
        sector: Sector name (banks, healthcare_and_pharma, real_estate, etc.)
                Leave empty to list all sectors.
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M
        limit: Max results per sector (max 50)
- `tv_egx_sector_scanner` — tradingview Sector rotation scanner for EGX — identifies hot/cold sectors and top picks.

    Args:
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M (default 1D)
        top_n_sectors: Number of top sectors to show stock picks for (1-18, default 5)
        top_n_stocks: Number of top stocks per highlighted sector (1-10, default 3)
        min_stock_score: Minimum stock score for picks (0-100, default 60)
- `tv_egx_smart_money_scanner` — tradingview Rank EGX index constituents by smart-money accumulation evidence.

    Runs the full smart_money_analysis per constituent (Yahoo .CA history,
    bounded thread pool) and ranks by the volume-flow composite score, with
    the banker decomposition and oscillator state attached per row. Rows the
    data source can't serve are listed under `skipped`, never silently
    dropped.

    Args:
        index: EGX30 | EGX70 | EGX100 | SHARIAH33 | EGX35LV | TAMAYUZ
        limit: Max ranked rows to return (default 10, max 50)
        period: History window — 1mo | 3mo | 6mo | 1y | 2y (default 6mo)
        min_score: Only include rows with composite score >= this (0-100)
- `tv_egx_stock_screener` — tradingview Production stock ranking engine for EGX — finds strong stocks with actionable setups.

    Args:
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M (default 1D)
        min_score: Minimum stock score to include (0-100, default 55)
        index_filter: Filter by index — EGX30, EGX70, EGX100, SHARIAH33, EGX35LV, TAMAYUZ
        limit: Number of results (max 50)
- `tv_egx_trade_plan` — tradingview Generate a full trade plan for a specific EGX stock.

    Args:
        symbol: EGX stock symbol (e.g., "COMI", "TMGH", "FWRY")
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M (default 1D)
- `tv_financial_news` — tradingview Real-time financial news via Marketaux (licensed).

    Args:
        symbol: Optional symbol filter ("AAPL", "BTC"). None = all news.
        category: News category ("crypto", "stocks", "all")
        limit: Max number of news items
- `tv_futures_category_snapshot` — tradingview Quote all major front-month contracts in a specific futures category.

    Args:
        category: equity_index | energy | metals | agriculture | rates | forex | crypto_futures

    Returns:
        OHLCV quotes for the standard watchlist of contracts in that category.
        Example symbols: ES1! NQ1! (equity_index), CL1! NG1! (energy), GC1! SI1! (metals).
- `tv_futures_market_overview` — tradingview Top futures contracts sorted by trading volume.

    Args:
        category:   all | equity_index | energy | metals | agriculture | rates | forex | crypto_futures
        exchanges:  us (CME, COMEX, NYMEX, CBOT) | global (adds ICE, EUREX)
        limit:      max contracts to return (default 30)
        volume_min: minimum volume filter (0 = no filter)

    Returns:
        Dict with total_available count and list of contracts with OHLCV + % change.
- `tv_futures_top_movers` — tradingview Futures contracts with the biggest percentage moves today.

    Args:
        direction:  gainers | losers
        exchanges:  us | global
        limit:      max results
        volume_min: minimum volume filter (default 10, filters illiquid contracts)

    Returns:
        List of futures ranked by % change with OHLCV data.
- `tv_futures_watchlist` — tradingview Return the full categorized list of well-known front-month futures symbols.

    Categories: equity_index, energy, metals, agriculture, rates, forex, crypto_futures.
    Use these symbols with futures_category_snapshot or coin_analysis for deeper analysis.
- `tv_market_sentiment` — tradingview News sentiment for stocks and crypto (licensed Marketaux entity sentiment).

    Args:
        symbol: Asset symbol ("AAPL", "BTC", "ETH", "TSLA")
        category: News group to search ("crypto", "stocks", "all")
        limit: Max articles to analyse
- `tv_market_snapshot` — tradingview Global market overview: major indices, top crypto, FX rates, and key ETFs.
    Powered by Yahoo Finance.
- `tv_multi_agent_analysis` — tradingview Run a multi-agent debate (Technical, Sentiment, Risk) for a specific symbol.

    Args:
        symbol: Symbol — crypto: "BTCUSDT"; stocks: "COMI" (EGX), "THYAO" (BIST), "600519" (SSE), "300251" (SZSE), "2330" (TWSE), "3105" (TPEX), "GDX" (AMEX)
        exchange: Exchange — crypto: KUCOIN, BINANCE, MEXC; stocks: EGX, BIST, NASDAQ, NYSE, AMEX, NYSEARCA, PCX, SSE, SZSE, TWSE, TPEX, EPA (Euronext Paris), AMS, BRU, LIS, MIL, LSE, SIX, BME, XETRA, FWB, TSX, TSXV, NSE, BSE (India), IDX (Indonesia)
        timeframe: Time interval (5m, 15m, 1h, 4h, 1D, 1W)

    Returns:
        A structured debate between 3 AI agents culminating in a final trading decision.
- `tv_multi_timeframe_analysis` — tradingview Multi-timeframe alignment analysis (Weekly → Daily → 4H → 1H → 15m).

    Canonical name is exactly `multi_timeframe_analysis` (there is no
    "get_multi_timeframe_analysis" tool). Use this for cross-timeframe trend
    alignment on ONE symbol; for a single-timeframe deep dive use
    `coin_analysis`; for TA + sentiment + news use `combined_analysis`.

    Example: multi_timeframe_analysis(symbol="SOLUSDT", exchange="BINANCE")

    Args:
        symbol: Bare ticker, no exchange prefix — crypto: "BTCUSDT"; stocks: "COMI" (EGX), "THYAO" (BIST), "600519" (SSE), "300251" (SZSE), "2330" (TWSE), "3105" (TPEX), "GDX" (AMEX)
        exchange: Exchange — crypto: KUCOIN, BINANCE, MEXC; stocks: EGX, BIST, NASDAQ, NYSE, AMEX, NYSEARCA, PCX, SSE, SZSE, TWSE, TPEX, EPA (Euronext Paris), AMS, BRU, LIS, MIL, LSE, SIX, BME, XETRA, FWB, TSX, TSXV, NSE, BSE (India), IDX (Indonesia)
- `tv_rating_filter` — tradingview Filter coins by Bollinger Band rating.

    Args:
        exchange: Exchange name like KUCOIN, BINANCE, BYBIT, MEXC, etc.
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M
        rating: BB rating (-3 to +3): -3=Strong Sell, -2=Sell, -1=Weak Sell, 1=Weak Buy, 2=Buy, 3=Strong Buy
        limit: Number of rows to return (max 50)

    Returns ``listdict`` on success. On ANY failure returns a structured
    error envelope ``{"error": {"code": ..., "retryable": ...}}``.
- `tv_smart_money_analysis` — tradingview Banker/hot-money proxy read for one symbol from price+volume history.

    Three independent families, computed from Yahoo Finance OHLCV:
      - mcdx_style: RSI-horizon decomposition (banker RSI50 / hot-money RSI40
        / retail RSI14, each scaled 0-20) — sustained slow-horizon strength
        that fast horizons can't fake reads as institutional accumulation.
      - banker_fund_oscillator: EMA(13)-smoothed 34-bar stochastic of the
        weighted typical price, 0-100, with BANKER_ENTRY/EXIT states.
      - volume_flow_composite: CMF(20) + MFI(14) + OBV trend + up/down volume
        balance → 0-100 accumulation score.
    Plus a consensus vote across the three.

    These are documented, reproducible formula variants inspired by the
    public "banker fund" indicator family — NOT actual institutional-flow
    data, and not copies of any closed-source script.

    Args:
        symbol: Bare ticker — EGX: "COMI", "TMGH"; US: "AAPL"; crypto pairs
            work via Yahoo notation ("BTC-USD").
        exchange: EGX (maps to Yahoo .CA), BIST (.IS), TADAWUL (.SR); anything
            else passes the symbol to Yahoo unchanged.
        period: 1mo | 3mo | 6mo | 1y | 2y (default 6mo)
        interval: 1d (default) or 1h
- `tv_smart_volume_scanner` — tradingview Smart volume + technical analysis combination scanner.

    Args:
        exchange: Exchange name
        min_volume_ratio: Minimum volume multiplier (default 2.0)
        min_price_change: Minimum price change percentage (default 2.0)
        rsi_range: "oversold" (<30), "overbought" (>70), "neutral" (30-70), "any"
        limit: Number of results (max 30)

    Returns ``listdict`` on success. On ANY failure returns a structured
    error envelope ``{"error": {"code": ..., "retryable": ...}}``.
- `tv_stock_extended_hours` — tradingview Real-time pre-market and after-hours prices for a US stock symbol.

    Use this when the user asks about a stock outside the regular 9:30am-4pm
    ET session — earnings reactions, overnight news, "what is X doing in
    after-hours?", "how did Y open in pre-market?". Returns the most recent
    valid print from each session window (pre-market, regular, post-market)
    along with computed % changes vs. the previous close and the regular
    close, respectively.

    During the regular session, post_market will be null (no data yet).
    On weekends/holidays, returns whatever's most recent in each window.

    Args:
        symbol: US stock symbol — AAPL, NVDA, TSLA, SPY, ^GSPC, etc.

    Returns:
        - pre_market: {price, as_of_utc, change_vs_previous_close_pct, reference_close} or null;
          the change is measured from reference_close, the last regular close
          (before the open that is newer than previous_close)
        - regular: {price, as_of_utc, change_pct} (consolidated tape close)
        - post_market: {price, as_of_utc, change_vs_regular_close_pct} or null
        - previous_close, currency, exchange, market_state for context
- `tv_stock_options_chain` — tradingview Full options chain (calls + puts) for a US stock symbol and one expiry.

    Use this when the user asks "what's the options chain for X?", "show me
    AAPL puts expiring next Friday", or wants to inspect bid/ask/IV/volume on
    a specific strike. If no expiry is provided, returns the nearest expiry
    so Claude can quote it back and ask "want a different one?".

    Args:
        symbol: US stock symbol — AAPL, NVDA, TSLA, SPY, etc.
        expiry: Optional ISO date (YYYY-MM-DD). Must match one of the
            `available_expiries` Yahoo returns; otherwise returns an error
            with the list of valid dates.

    Returns:
        - underlying_price, underlying_change_pct
        - requested_expiry, available_expiries (list of YYYY-MM-DD)
        - call_count, put_count
        - calls: list of {strike, last_price, bid, ask, volume,
          open_interest, implied_volatility, in_the_money, expiration}
        - puts: same shape as calls
- `tv_stock_options_unusual_activity` — tradingview Top strikes by volume / open-interest ratio — institutional positioning signal.

    Use this when the user asks "any unusual options activity on X?", "where
    is the smart money positioned on NVDA before earnings?", or wants a
    V/OI screener for a ticker. A V/OI ratio > 1 means today's volume already
    exceeds standing open interest, which classically flags fresh institutional
    positioning on a specific strike in a specific direction (call vs put).

    Scans the soonest few expirations, filters out illiquid strikes (under
    `min_volume`), and returns the top-N sorted by V/OI descending. Also
    returns aggregate call vs put volume so Claude can comment on the
    overall directional bias.

    Args:
        symbol: US stock symbol — AAPL, NVDA, TSLA, SPY, META, etc.
        top_n: How many strikes to return. Default 10.
        min_volume: Filter floor for today's volume — prevents noise from
            illiquid strikes with high V/OI ratios. Default 100.
        expiries: Number of soonest expirations to scan. Default 4
            (typically covers ~1 month of weeklies + monthlies).

    Returns:
        - underlying_price
        - expiries_scanned (list of YYYY-MM-DD)
        - total_call_volume, total_put_volume, put_call_volume_ratio
        - unusual: list of top-N contracts sorted by V/OI desc, each with
          {strike, side (call|put), expiration, volume, open_interest,
          v_oi_ratio, last_price, implied_volatility, in_the_money,
          strike_vs_spot_pct (moneyness)}
- `tv_stock_prices` — tradingview Current price + daily % change for specific stock symbols.

    Args:
        tickers: comma-separated EXCHANGE:SYMBOL list (max 2000 — one
            upstream request even at full size), e.g.
            "NASDAQ:NVDA, NASDAQ:TSLA, KRX:005930". The exchange prefix is
            required — the scanner's direct-ticker lookup is exchange-scoped.

    Returns:
        Envelope dict: rows of {ticker, symbol, description, exchange, price,
        open, high, low, currency, change_percent} plus a not_found list naming any requested
        ticker the scanner didn't recognize.
- `tv_stock_screener` — tradingview Screen stocks by share type — the API twin of TradingView's
    "Common stock" / "Preferred stock" symbol-search filter.

    Args:
        country: TradingView market name — e.g. america, korea, germany,
            brazil, japan, uk, india, turkey, canada, australia, france, hongkong
        stock_type: common | preferred
        limit: rows to return (max 2000, single upstream request), ranked by market cap descending
        exclude_otc: default True — drop OTC listings (foreign companies traded
            over-the-counter); "america" otherwise means "US venue", not "US company"
        compact: default False — True returns only ticker/symbol/price/currency/
            change_percent per row (light payload for bulk price feeds)
        sort_by: market_cap (default) | dividend_yield | change | price —
            server-side descending sort over the WHOLE market, so e.g.
            sort_by=dividend_yield with limit=20 is the market's true top-20
            dividend payers, not just the biggest companies re-sorted

    Returns:
        Envelope dict: total_matches (market-wide count), returned, and rows
        of {ticker, symbol, description, exchange, price, open, high, low,
        currency, change_percent, dividend_yield, market_cap} — price is the
        current/last close; open/high/low are the current session's daily bar. Prices are in the
        market's local currency (e.g. KRW for korea).
- `tv_top_gainers` — tradingview Return top gainers for an exchange and timeframe using Bollinger Band analysis.

    Args:
        exchange: Exchange name — crypto: KUCOIN, BINANCE, BYBIT, MEXC; stocks: EGX, BIST, NASDAQ, NYSE, BURSA, HKEX, SSE, SZSE, TWSE, TPEX, EPA (Euronext Paris), AMS, BRU, LIS, MIL, LSE, SIX, BME, XETRA, FWB, TSX, TSXV, NSE, BSE (India), IDX (Indonesia)
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M
        limit: Number of rows to return (max 50)

    Returns:
        listdict on success. On ANY failure returns a structured error
        envelope ``{"error": {"code": ..., "retryable": ...}}`` — never a
        raw exception string.
- `tv_top_losers` — tradingview Return top losers for an exchange and timeframe. Supports crypto (KUCOIN, BINANCE, MEXC) and stocks (EGX, BIST, NASDAQ).

    Returns ``listdict`` on success. On ANY failure returns a structured
    error envelope ``{"error": {"code": ..., "retryable": ...}}``.
- `tv_volume_breakout_scanner` — tradingview Detect coins with volume breakout + price breakout.

    Args:
        exchange: Exchange name like KUCOIN, BINANCE, BYBIT, MEXC, etc.
        timeframe: One of 5m, 15m, 1h, 4h, 1D, 1W, 1M
        volume_multiplier: How many times the volume should be above normal level (default 2.0)
        price_change_min: Minimum price change percentage (default 3.0)
        limit: Number of rows to return (max 50)

    Returns ``listdict`` on success, or an error envelope on total upstream
    failure (``{"error": {"code": "ALL_BATCHES_FAILED", ...}}``). The empty
    list now strictly means "no matches today"; rate-limit cliffs surface
    explicitly.
- `tv_volume_confirmation_analysis` — tradingview Detailed volume confirmation analysis for a specific coin.

    Args:
        symbol: Coin symbol (e.g., BTCUSDT)
        exchange: Exchange name
        timeframe: Time frame for analysis
- `tv_walk_forward_backtest_strategy` — tradingview Walk-forward backtest to detect overfitting — validates strategy on unseen data.

    Args:
        symbol: Yahoo Finance symbol (AAPL, BTC-USD, SPY…)
        strategy: rsi | bollinger | macd | ema_cross | supertrend | donchian
                  | keltner_breakout
                  (rsi_pullback and triple_ema not supported here — SMA200 warmup
                   exceeds typical fold size; use run_backtest with period='2y')
        period: '1mo', '3mo', '6mo', '1y', '2y' (recommend '2y')
        initial_capital: Starting capital per fold in USD (default $10,000)
        commission_pct: Per-trade commission % (default 0.1%)
        slippage_pct: Per-trade slippage % (default 0.05%)
        n_splits: Number of walk-forward folds (default 3, max 10)
        train_ratio: Fraction of each fold used for training (default 0.7)
        interval: '1d' (daily) or '1h' (hourly)
- `tv_yahoo_price` — tradingview Real-time price quote from Yahoo Finance for any stock, crypto, ETF or index.

    Args:
        symbol: Yahoo Finance symbol — e.g. AAPL, BTC-USD, SPY, ^GSPC, EURUSD=X, THYAO.IS
