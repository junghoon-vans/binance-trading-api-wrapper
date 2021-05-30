from marshmallow import Schema, fields


class StreamSchema(Schema):
    listenKey = fields.String(
        required=True,
    )
