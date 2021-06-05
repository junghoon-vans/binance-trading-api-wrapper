from marshmallow import Schema, fields, validate

from api.enum import IncomeType
from api.schema.default import SymbolRequiredSchema, SymbolOptionalSchema


class GetTransferSchema(Schema):
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


class PostTransferSchema(Schema):
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


class GetTradesSchema(SymbolRequiredSchema):
    pass


class GetPositionSchema(SymbolOptionalSchema):
    pass


class GetIncomeSchema(Schema):
    symbol = fields.String(
        required=True,
        metadata={
            "description": "The asset being transferred",
            "example": "USDT",
        },
    )
    incomeType = fields.String(
        required=False,
        validate=validate.OneOf([e.value for e in IncomeType]),
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


class GetLeverageBracketSchema(SymbolOptionalSchema):
    pass
