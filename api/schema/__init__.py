from api.schema.default import EmptyDictSchema, TimeSchema, StreamSchema
from api.schema.account import (
    AccountTransferSchema,
    AccountTransferHistorySchema,
    AccountTradesSchema,
    AccountPositionInfoSchema,
    AccountIncomeHistorySchema,
    AccountLeverageBracketSchema,
)


ping_schema = EmptyDictSchema()
time_schema = TimeSchema()
stream_schema = StreamSchema()

account_transfer_schema = AccountTransferSchema()
account_transfer_history_schema = AccountTransferHistorySchema()
account_trades_schema = AccountTradesSchema()
account_postion_info_schema = AccountPositionInfoSchema()
account_income_history_schema = AccountIncomeHistorySchema()
account_leverage_bracket_schema = AccountLeverageBracketSchema()
