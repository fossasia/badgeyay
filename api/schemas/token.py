from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class TokenSchema(Schema):
    class Meta:
        type_ = 'reset-users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    token = fields.Str(required=True)
