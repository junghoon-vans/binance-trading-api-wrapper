from api.schema.default import (
    EmptyDictSchema,
    SymbolRequiredSchema,
    SymbolOptionalSchema,
    TimeSchema,
    StreamSchema,
)

from api.schema.account import (
    AccountTransferSchema,
    AccountTransferHistorySchema,
    AccountIncomeHistorySchema,
)

from api.schema.market import (
    LookupSchema,
    AggregateTradesSchema,
    KlinesSchema,
    ContinousKlinesSchema,
    HistoricalKlinesSchema,
    HistoricalKlinesGeneratorSchema,
    MarkPriceSchema,
    FundingRateSchema,
    TickerPriceChangeSchema,
    SymbolPriceTickerSchema,
    SymbolOrderbookTickerSchema,
    OpenInterestSchema,
    OpenInterestStatisticsSchema,
)


ping_schema = EmptyDictSchema()
time_schema = TimeSchema()
stream_schema = StreamSchema()

account_transfer_schema = AccountTransferSchema()
account_transfer_history_schema = AccountTransferHistorySchema()
account_trades_schema = SymbolRequiredSchema()
account_postion_info_schema = SymbolOptionalSchema()
account_income_history_schema = AccountIncomeHistorySchema()
account_leverage_bracket_schema = SymbolOptionalSchema()

market_order_book_schema = LookupSchema()
market_recent_trades_schema = LookupSchema()
market_aggregate_trades_schema = AggregateTradesSchema()
market_klines_schema = KlinesSchema()
market_continous_klines_schema = ContinousKlinesSchema()
market_historical_klines_schema = HistoricalKlinesSchema()
market_historical_klines_generator_schema = HistoricalKlinesGeneratorSchema()
market_mark_price_schema = MarkPriceSchema()
market_funding_rate_schema = FundingRateSchema()
market_ticker_price_change_schema = TickerPriceChangeSchema()
market_symbol_price_ticker_schema = SymbolPriceTickerSchema()
market_symbol_orderbook_ticker_schema = SymbolOrderbookTickerSchema()
market_open_interest_schema = OpenInterestSchema()
market_open_interest_statistics_schema = OpenInterestStatisticsSchema()
