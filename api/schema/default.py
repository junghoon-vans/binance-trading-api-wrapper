from marshmallow import Schema, fields


class TimeSchema(Schema):
    serverTime = fields.Number(
        required=True,
    )


class StreamSchema(Schema):
    listenKey = fields.String(
        required=True,
    )
