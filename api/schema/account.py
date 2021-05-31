from marshmallow import Schema, fields, validate


class AccountTransferSchema(Schema):
    asset = fields.String(
        required=True,
        metadata={
            "description": "The asset being transferred",
            "example": "USDT",
        },
    )
    amount = fields.Decimal(
        required=True,
        metadata={
            "description": "The amount to be transferred",
        },
    )
    option = fields.Integer(
        required=True,
        metadata={
            "description": "1: transfer from spot account to USDT-Ⓜ futures account."
            + "2: transfer from USDT-Ⓜ futures account to spot account."
            + "3: transfer from spot account to COIN-Ⓜ futures account."
            + "4: transfer from COIN-Ⓜ futures account to spot account.",
        },
    )


class AccountTransferHistorySchema(Schema):
    asset = fields.String(
        required=True,
        metadata={
            "description": "The asset being transferred",
            "example": "USDT",
        },
    )
    startTime = fields.Number(
        required=True,
    )
    endTime = fields.Number(
        required=False,
    )
    current = fields.Number(
        required=False,
        metadata={
            "description": "Currently querying page. Start from 1. Default:1",
            "example": "USDT",
        },
    )
    size = fields.Number(
        required=False,
        metadata={
            "description": "Default:10 Max:100",
        },
    )


class AccountTradesSchema(Schema):
    symbol = fields.String(
        required=True,
    )


class AccountPositionInfoSchema(Schema):
    symbol = fields.String(
        required=False,
    )


class AccountIncomeHistorySchema(Schema):
    symbol = fields.String(
        required=True,
        metadata={
            "description": "The asset being transferred",
            "example": "USDT",
        },
    )
    incomeType = fields.String(
        required=False,
        validate=validate.OneOf(
            [
                "TRANSFER",
                "WELCOME_BONUS",
                "REALIZED_PNL",
                "FUNDING_FEE",
                "COMMISSION",
                "INSURANCE_CLEAR",
            ]
        ),
    )
    startTime = fields.Number(
        required=False,
        metadata={
            "description": "Timestamp in ms to get funding from INCLUSIVE.",
        },
    )
    endTime = fields.Number(
        required=False,
        metadata={
            "description": "Timestamp in ms to get funding until INCLUSIVE.",
        },
    )
    limit = fields.Integer(
        required=False,
        metadata={
            "description": "Default 100; max 1000",
        },
    )


class AccountLeverageBracketSchema(Schema):
    symbol = fields.String(
        required=False,
    )
