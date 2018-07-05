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
    photoURL = fields.Str(required=True)
    siteAdmin = fields.Bool()


class AllUsersSchema(Schema):
    class Meta:
        type_ = 'all-users'
        self_views = 'admin.show_all_users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    created_at = fields.Date(required=True)
    photoURL = fields.Str(required=True)
    deleted_at = fields.Date()


class OAuthUserSchema(Schema):
    class Meta:
        type_ = 'users'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    photoURL = fields.Str(required=True, allow_none=True)
    siteAdmin = fields.Bool()


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


class PermissionSchema(Schema):
    class Meta:
        type_ = 'permissions'

    id = fields.Str(required=True, dump_only=True)
    isUser = fields.Bool(required=True)
    isAdmin = fields.Bool(required=True)
    isSales = fields.Bool(required=True)
