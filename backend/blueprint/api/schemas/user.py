from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class UserSchema(Schema):
    class Meta:
        type_ = 'Users'
        self_view = 'loginUser.login'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    name = fields.Str(required=True)
