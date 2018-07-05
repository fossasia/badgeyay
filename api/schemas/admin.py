from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class AdminSchema(Schema):
    class Meta:
        type_ = 'create-admins'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)


class AdminMailStat(Schema):
    class Meta:
        type_ = 'admin-stat-mails'
        kwargs = {'id': '<id>'}

    id = fields.Date(required=True, dump_only=True)
    lastDayCount = fields.Str(required=True, default='0')
    lastThreeDays = fields.Str(required=True, default='0')
    lastSevenDays = fields.Str(required=True, default='0')
    lastMonth = fields.Str(required=True, default='0')


class AllUserStat(Schema):
    class Meta:
        type_ = 'admin-stat-users'
        kwargs = {'id': '<id>'}

    id = fields.Date(required=True, dump_only=True)
    superAdmin = fields.Str(required=True)
    registered = fields.Str(required=True)


class AllAdminRole(Schema):
    class Meta:
        type_ = 'admins'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.Str(required=True)


class DeleteAdminRole(Schema):
    class Meta:
        type_ = 'delete-admins'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    email = fields.Str(required=True)
    siteAdmin = fields.Bool(required=True)


class SocialMedia(Schema):
    class Meta:
        type_ = 'social-contents'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True, attribute='name')
    description = fields.Str(required=True)
    link = fields.Str(required=True)
    icon = fields.Str(required=True)
