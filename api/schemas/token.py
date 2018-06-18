from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class TokenSchema(Schema):
    class Meta:
        type_ = 'reset-users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    token = fields.Str(required=True)


class ValidTokenSchema(Schema):
    class Meta:
        type_ = 'valid-tokens'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    valid = fields.Bool(required=True)


class LoginTokenSchema(Schema):
    class Meta:
        type_ = 'login-tokens'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    token = fields.Str(required=True)
