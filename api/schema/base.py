from marshmallow import Schema, fields


class SymbolRequiredSchema(Schema):
    symbol = fields.String(
        required=True,
    )


class SymbolOptionalSchema(Schema):
    symbol = fields.String(
        required=False,
    )


class PairRequiredSchema(Schema):
    symbol = fields.String(
        required=True,
    )
