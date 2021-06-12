from marshmallow import Schema, fields, validate

from api.enum import IncomeType
from api.schema.base import SymbolRequiredSchema, SymbolOptionalSchema


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
        default=1,
        validate=validate.Range(min=1),
        metadata={
            "description": "Currently querying page.",
        },
    )
    size = fields.Number(
        required=False,
        default=10,
        validate=validate.Range(min=0, max=100),
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
        default=100,
        validate=validate.Range(min=1, max=1000),
    )


class GetLeverageBracketSchema(SymbolOptionalSchema):
    pass
