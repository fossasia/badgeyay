from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class UserSchema(Schema):
    class Meta:
        type_ = 'user-signups'
        self_view = 'registerUser.register_user'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class AllUsersSchema(Schema):
    class Meta:
        type_ = 'all-users'
        self_views = 'admin.show_all_users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)


class OAuthUserSchema(Schema):
    class Meta:
        type_ = 'users'
        self_view = 'registerUser.register_user'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    photoURL = fields.Str(required=True)
