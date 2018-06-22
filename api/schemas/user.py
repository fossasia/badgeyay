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


class UpdateUserSchema(Schema):
    class Meta:
        type_ = 'users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    photoURL = fields.Str(required=True)


class UserAllowedUsage(Schema):
    class Meta:
        type_ = 'user_allowed_usage'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    allowed_usage = fields.Str(required=True, dump_only=True)


class FTLUserSchema(Schema):
    class Meta:
        type_ = 'users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    photoURL = fields.Str(required=True)
    ftl = fields.Boolean(required=True)


class DeleteUserSchema(Schema):
    class Meta:
        type_ = 'delete-user'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    uid = fields.Str(required=True)


class DatedUserSchema(Schema):
    class Meta:
        type_ = 'dated-users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)


class UpdateProfileSchema(Schema):
    class Meta:
        type_ = 'update-user'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    uid = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
