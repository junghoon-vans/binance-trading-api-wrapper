from marshmallow import fields, validate

from api.schema.default import (
    SymbolRequiredSchema,
    SymbolOptionalSchema,
    PairRequiredSchema,
)
from api.enum import CandlestickInterval, ContractType, Period


class LookupSchema(SymbolRequiredSchema):
    limit = fields.Integer(
        required=False,
        validate=validate.Range(min=0, max=1000),
        metadata={
            "description": "Default 500",
        },
    )


class AggregateTradesSchema(LookupSchema):
    fromId = fields.Number(
        required=False,
        metadata={
            "description": "ID to get aggregate trades from INCLUSIVE.",
        },
    )
    startTime = fields.Number(
        required=False,
        metadata={
            "description": "Timestamp in ms to get aggregate trades from INCLUSIVE.",
        },
    )
    endTime = fields.Number(
        required=False,
        metadata={
            "description": "Timestamp in ms to get aggregate trades until INCLUSIVE.",
        },
    )


class KlinesSchema(SymbolRequiredSchema):
    interval = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in CandlestickInterval]),
    )
    startTime = fields.Number(
        required=False,
    )
    endTime = fields.Number(
        required=False,
    )
    limit = fields.Integer(
        required=False,
        validate=validate.Range(min=0, max=1500),
        metadata={
            "description": "Default 500",
        },
    )


class ContinousKlinesSchema(PairRequiredSchema):
    contractType = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in ContractType]),
    )
    interval = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in CandlestickInterval]),
    )
    startTime = fields.Number(
        required=False,
    )
    endTime = fields.Number(
        required=False,
    )
    limit = fields.Integer(
        required=False,
        validate=validate.Range(min=0, max=1500),
        metadata={
            "description": "Default 500",
        },
    )


class GetHistoricalKlinesSchema(SymbolRequiredSchema):
    interval = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in CandlestickInterval]),
    )
    startTime = fields.Number(
        required=True,
    )
    endTime = fields.Number(
        required=False,
    )
    limit = fields.Integer(
        required=False,
        validate=validate.Range(min=0, max=1000),
        metadata={
            "description": "Default 500",
        },
    )


class PostHistoricalKlinesSchema(SymbolRequiredSchema):
    interval = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in CandlestickInterval]),
    )
    startTime = fields.Number(
        required=True,
    )
    endTime = fields.Number(
        required=False,
    )


class MarkPriceSchema(SymbolOptionalSchema):
    pass


class FundingRateSchema(SymbolOptionalSchema):
    startTime = fields.Number(
        required=False,
        metadata={
            "description": "Timestamp in ms to get funding rate from INCLUSIVE.",
        },
    )
    endTime = fields.Number(
        required=False,
        metadata={
            "description": "Timestamp in ms to get funding rate until INCLUSIVE.",
        },
    )
    limit = fields.Integer(
        required=False,
        validate=validate.Range(min=0, max=1000),
        metadata={
            "description": "Default 100",
        },
    )


class TickerPriceChangeSchema(SymbolOptionalSchema):
    pass


class SymbolPriceTickerSchema(SymbolOptionalSchema):
    pass


class SymbolOrderbookTickerSchema(SymbolOptionalSchema):
    pass


class OpenInterestSchema(SymbolRequiredSchema):
    pass


class OpenInterestStatisticsSchema(SymbolRequiredSchema):
    period = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in Period]),
    )
    limit = fields.Integer(
        required=False,
        validate=validate.Range(min=0, max=500),
        metadata={
            "description": "Default 30",
        },
    )
    startTime = fields.Number(
        required=False,
    )
    endTime = fields.Number(
        required=False,
    )
