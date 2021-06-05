from marshmallow import Schema, fields, validate

from api.schema.base import SymbolRequiredSchema, SymbolOptionalSchema
from api.enum import (
    OrderSide,
    PositionSide,
    OrderType,
    TimeInForce,
    OrderRespType,
    FuturesMarginType,
)


class GetOrderSchema(SymbolRequiredSchema):
    orderId = fields.Number(
        metadata={
            "description": "Either orderId or origClientOrderId must be sent.",
        },
    )
    origClientOrderId = fields.String()


class PostOrderSchema(SymbolRequiredSchema):
    side = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in OrderSide]),
    )
    positionSide = fields.String(
        default="BOTH",
        validate=validate.OneOf([e.value for e in PositionSide]),
        metadata={
            "description": "Default for One-way Mode;"
            + "LONG or SHORT must be sent in Hedge Mode.",
        },
    )
    type = fields.String(
        required=True,
        validate=validate.OneOf([e.value for e in OrderType]),
    )
    timeInForce = fields.String(
        validate=validate.OneOf([e.value for e in TimeInForce]),
    )
    quantity = fields.Decimal(
        metadata={
            "description": "Cannot be sent with closePosition=true(Close-All)",
        },
    )
    reduceOnly = fields.Boolean(
        default="False",
        metadata={
            "description": "Cannot be sent in Hedge Mode;"
            + "cannot be sent with closePosition=true"
        },
    )
    price = fields.Decimal()
    newClientOrderId = fields.String(
        metadata={
            "description": "A unique id among open orders."
            + "Automatically generated if not sent."
        },
        validate=validate.Regexp("^[\\.A-Z\\:/a-z0-9_-]{1,36}$"),
    )
    stopPrice = fields.Decimal(
        metadata={
            "description": "Used with STOP/STOP_MARKET"
            + " or TAKE_PROFIT/TAKE_PROFIT_MARKET orders."
        },
    )
    closePosition = fields.Boolean(
        metadata={
            "description": "Close-All，used with STOP_MARKET or TAKE_PROFIT_MARKET."
        },
    )
    activationPrice = fields.Decimal(
        metadata={
            "description": "Used with TRAILING_STOP_MARKET orders,"
            + " default as the latest price(supporting different workingType)"
        },
    )
    callbackRate = fields.Decimal(
        validate=validate.Range(min=0.1, max=5),
        metadata={"description": "Used with TRAILING_STOP_MARKET orders."},
    )
    workingType = fields.String(
        metadata={
            "description": "stopPrice triggered by: "
            + "'ARK_PRICE' 'ONTRACT_PRICE' Default 'ONTRACT_PRICE'"
        },
    )
    priceProtect = fields.Boolean(
        default="False",
        metadata={
            "description": "Used with STOP/STOP_MARKET"
            + " or TAKE_PROFIT/TAKE_PROFIT_MARKET orders."
        },
    )
    newOrderRespType = fields.String(
        default=OrderRespType.ACK,
        validate=validate.OneOf([e.value for e in OrderRespType]),
    )


class DeleteOrderSchema(SymbolRequiredSchema):
    orderId = fields.Number(
        metadata={
            "description": "Either orderId or origClientOrderId must be sent.",
        },
    )
    origClientOrderId = fields.String()


class MultipleOrderSchema(SymbolRequiredSchema):
    quantity = fields.Decimal(
        requried=True,
        metadata={
            "description": "Cannot be sent with closePosition=true(Close-All)",
        },
    )


class PostMultipleOrderSchema(PostOrderSchema):
    batchOrders = fields.List(
        fields.Nested(MultipleOrderSchema),
        validate=validate.Length(max=5),
    )


class DeleteMultipleOrderSchema(SymbolRequiredSchema):
    orderIdList = fields.List(
        fields.Number(
            validate=validate.Length(max=10),
        ),
        metadata={
            "description": "Either orderIdList or origClientOrderIdList must be sent.",
        },
    )
    origClientOrderIdList = fields.List(
        fields.String(
            validate=validate.Length(max=10),
        )
    )


class GetOpenOrderSchema(SymbolRequiredSchema):
    orderId = fields.Number(
        metadata={
            "description": "Either orderId or origClientOrderId must be sent.",
        },
    )
    origClientOrderId = fields.String()


class GetAllOrderSchema(SymbolOptionalSchema):
    pass


class DeleteAllOrderSchema(SymbolRequiredSchema):
    pass


class PutLeverageSchema(SymbolRequiredSchema):
    leverage = fields.Integer(
        required=True,
        validate=validate.Range(min=1, max=125),
    )


class PutMarginTypeSchema(SymbolRequiredSchema):
    marginType = fields.String(
        validate=validate.OneOf([e.value for e in FuturesMarginType]),
    )


class GetPositionMarginSchema(SymbolRequiredSchema):
    type = fields.Integer(
        metadata={
            "description": "1: Add position margin，2: Reduce position margin",
        },
    )
    startTime = fields.Number(
        required=False,
    )
    endTime = fields.Number(
        required=False,
    )
    limit = fields.Integer(default=500)


class PutPositionMarginSchema(SymbolRequiredSchema):
    positionSide = fields.String(
        default="BOTH",
        validate=validate.OneOf([e.value for e in PositionSide]),
        metadata={
            "description": "Default for One-way Mode; LONG or SHORT for Hedge Mode."
            + "It must be sent in Hedge Mode.",
        },
    )
    amount = fields.Decimal(
        required=True,
    )
    type = fields.Integer(
        metadata={
            "description": "1: Add position margin，2: Reduce position margin",
        },
    )


class PutPositionModeSchema(Schema):
    dualSidePosition = fields.Boolean(
        required=True,
        metadata={
            "description": "'true': Hedge Mode; 'false': One-way Mode",
        },
    )


class PutMultiAssetModeSchema(Schema):
    multiAssetsMargin = fields.Boolean(
        required=True,
        metadata={
            "description": "'true': Multi-Assets Mode; 'false': Single-Asset Mode",
        },
    )
