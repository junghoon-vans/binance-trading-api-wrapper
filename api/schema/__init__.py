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


ping_schema = EmptyDictSchema()
time_schema = TimeSchema()
stream_schema = StreamSchema()

account_transfer_schema = AccountTransferSchema()
account_transfer_history_schema = AccountTransferHistorySchema()
account_trades_schema = SymbolRequiredSchema()
account_postion_info_schema = SymbolOptionalSchema()
account_income_history_schema = AccountIncomeHistorySchema()
account_leverage_bracket_schema = SymbolOptionalSchema()
