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
    LookupSchema,
    AggregateTradesSchema,
    KlinesSchema,
    ContinousKlinesSchema,
    GetHistoricalKlinesSchema,
    PostHistoricalKlinesSchema,
    MarkPriceSchema,
    FundingRateSchema,
    TickerPriceChangeSchema,
    SymbolPriceTickerSchema,
    SymbolOrderbookTickerSchema,
    OpenInterestSchema,
    OpenInterestStatisticsSchema,
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
    ChangeLeverageSchema,
    ChangeMarginTypeSchema,
    GetPositionMarginSchema,
    PostPositionMarginSchema,
    PostPositionModeSchema,
    PostMultiAssetModeSchema,
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

market_order_book_schema = LookupSchema()
market_recent_trades_schema = LookupSchema()
market_aggregate_trades_schema = AggregateTradesSchema()
market_klines_schema = KlinesSchema()
market_continous_klines_schema = ContinousKlinesSchema()
market_get_historical_klines_schema = GetHistoricalKlinesSchema()
market_post_historical_klines_schema = PostHistoricalKlinesSchema()
market_mark_price_schema = MarkPriceSchema()
market_funding_rate_schema = FundingRateSchema()
market_ticker_price_change_schema = TickerPriceChangeSchema()
market_symbol_price_ticker_schema = SymbolPriceTickerSchema()
market_symbol_orderbook_ticker_schema = SymbolOrderbookTickerSchema()
market_open_interest_schema = OpenInterestSchema()
market_open_interest_statistics_schema = OpenInterestStatisticsSchema()

trade_get_order_schema = GetOrderSchema()
trade_post_order_schema = PostOrderSchema()
trade_delete_order_schema = DeleteOrderSchema()
trade_post_multiple_order_schema = PostMultipleOrderSchema()
trade_delete_multiple_order_schema = DeleteMultipleOrderSchema()
trade_get_open_order_schema = GetOpenOrderSchema()
trade_get_all_order_schema = GetAllOrderSchema()
trade_delete_all_order_schema = DeleteAllOrderSchema()
trade_change_leverage_schema = ChangeLeverageSchema()
trade_change_margin_type_schema = ChangeMarginTypeSchema()
trade_get_position_margin_schema = GetPositionMarginSchema()
trade_post_position_margin_schema = PostPositionMarginSchema()
trade_post_position_mode_schema = PostPositionModeSchema()
trade_post_multi_asset_mode_schema = PostMultiAssetModeSchema()
