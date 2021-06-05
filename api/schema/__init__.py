from api.schema.default import (
    EmptyDictSchema,
    TimeSchema,
    StreamSchema,
)

from api.schema.account import (
    GetTransferSchema,
    PostTransferSchema,
    GetTradesSchema,
    GetPositionSchema,
    GetIncomeSchema,
    GetLeverageBracketSchema,
)

from api.schema.market import (
    GetOrderBookSchema,
    GetRecentTradesSchema,
    GetAggregateTradesSchema,
    GetKlinesSchema,
    GetContinousKlinesSchema,
    GetHistoricalKlinesSchema,
    PostHistoricalKlinesSchema,
    GetMarkPriceSchema,
    GetFundingRateSchema,
    GetTickerPriceChangeSchema,
    GetSymbolPriceTickerSchema,
    GetSymbolOrderbookTickerSchema,
    GetOpenInterestSchema,
    GetOpenInterestStatisticsSchema,
)

from api.schema.trade import (
    GetOrderSchema,
    PostOrderSchema,
    DeleteOrderSchema,
    PostMultipleOrderSchema,
    DeleteMultipleOrderSchema,
    GetOpenOrderSchema,
    GetAllOrderSchema,
    DeleteAllOrderSchema,
    PutLeverageSchema,
    PutMarginTypeSchema,
    GetPositionMarginSchema,
    PutPositionMarginSchema,
    PutPositionModeSchema,
    PutMultiAssetModeSchema,
)


ping_schema = EmptyDictSchema()
time_schema = TimeSchema()
stream_schema = StreamSchema()

account_get_transfer_schema = GetTransferSchema()
account_post_transfer_schema = PostTransferSchema()
account_get_trades_schema = GetTradesSchema()
account_get_postion_schema = GetPositionSchema()
account_get_income_schema = GetIncomeSchema()
account_get_leverage_bracket_schema = GetLeverageBracketSchema()

market_get_order_book_schema = GetOrderBookSchema()
market_get_recent_trades_schema = GetRecentTradesSchema()
market_get_aggregate_trades_schema = GetAggregateTradesSchema()
market_get_klines_schema = GetKlinesSchema()
market_get_continous_klines_schema = GetContinousKlinesSchema()
market_get_historical_klines_schema = GetHistoricalKlinesSchema()
market_post_historical_klines_schema = PostHistoricalKlinesSchema()
market_get_mark_price_schema = GetMarkPriceSchema()
market_get_funding_rate_schema = GetFundingRateSchema()
market_get_ticker_price_change_schema = GetTickerPriceChangeSchema()
market_get_symbol_price_ticker_schema = GetSymbolPriceTickerSchema()
market_get_symbol_orderbook_ticker_schema = GetSymbolOrderbookTickerSchema()
market_get_open_interest_schema = GetOpenInterestSchema()
market_get_open_interest_statistics_schema = GetOpenInterestStatisticsSchema()

trade_get_order_schema = GetOrderSchema()
trade_post_order_schema = PostOrderSchema()
trade_delete_order_schema = DeleteOrderSchema()
trade_post_multiple_order_schema = PostMultipleOrderSchema()
trade_delete_multiple_order_schema = DeleteMultipleOrderSchema()
trade_get_open_order_schema = GetOpenOrderSchema()
trade_get_all_order_schema = GetAllOrderSchema()
trade_delete_all_order_schema = DeleteAllOrderSchema()
trade_put_leverage_schema = PutLeverageSchema()
trade_put_margin_type_schema = PutMarginTypeSchema()
trade_get_position_margin_schema = GetPositionMarginSchema()
trade_put_position_margin_schema = PutPositionMarginSchema()
trade_put_position_mode_schema = PutPositionModeSchema()
trade_put_multi_asset_mode_schema = PutMultiAssetModeSchema()
