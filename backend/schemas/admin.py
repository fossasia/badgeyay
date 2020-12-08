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

class AdminBadgeSchema(Schema):
    class Meta:
        type_ = 'all-admin-badges'

    id = fields.Str(required=True, dump_only=True, attribute='Badges.id')
    image = fields.Str(required=True, attribute='Badges.image')
    csv = fields.Str(required=True, attribute='Badges.csv')
    text_colour = fields.Str(required=True, attribute='Badges.text_colour')
    badge_size = fields.Str(required=True, attribute='Badges.badge_size')
    download_link = fields.Str(required=True, attribute='Badges.download_link')
    created_at = fields.Date(required=True, attribute='Badges.created_at')
    user_id = fields.Str(required=True, attribute='Badges.user_id')
    username = fields.Str(required=True, attribute='User.username')
    badge_name = fields.Str(required=True, attribute='Badges.badge_name')
    deleted_at = fields.DateTime(attribute='Badges.deleted_at')

class AdminReportSchema(Schema):
    class Meta:
        type_ = 'admin-reports'

    id = fields.Date(required=True, dump_only=True)
    mailSentCount = fields.Int(as_string=True)
    badgeCount = fields.Int(as_string=True)
    badgeDeletionCount = fields.Int(as_string=True)
    userCreationCount = fields.Int(as_string=True)
    userDeletionCount = fields.Int(as_string=True)

class RoleSchema(Schema):
    class Meta:
        type_ = 'roles'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    created_at = fields.Str(required=True)

class SalesSchema(Schema):
    class Meta:
        type_ = 'create-sales'

    id = fields.Str(required=True, dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)

class DeleteSales(Schema):
    class Meta:
        type_ = 'delete-sales'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    email = fields.Str(required=True)

class SettingsSchema(Schema):
    class Meta:
        type_ = 'settings'

    id = fields.DateTime()
    appEnvironment = fields.Integer(as_string=True)
    appName = fields.Str()
    secretKey = fields.Str()
    firebaseStorageBucket = fields.Str()
    firebaseDatabaseURL = fields.Str()
    fromMail = fields.Str()
    sendGridApiKey = fields.Str()

class Mails(Schema):
    class Meta:
        type_ = 'messages'
    id = fields.Str()
    Description = fields.Str()
    Subject = fields.Str()
