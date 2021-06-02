from marshmallow import Schema, fields


class EmptyDictSchema(Schema):
    pass


class SymbolRequiredSchema(Schema):
    symbol = fields.String(
        required=True,
    )


class SymbolOptionalSchema(Schema):
    symbol = fields.String(
        required=False,
    )


class TimeSchema(Schema):
    serverTime = fields.Number(
        required=True,
    )


class StreamSchema(Schema):
    listenKey = fields.String(
        required=True,
    )
