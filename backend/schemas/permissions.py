from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields

class ModifyPermissionsIncoming(Schema):
    class Meta:
        type_ = 'modify-permissions'

    id = fields.Str(required=True, dump_only=True)
    uid = fields.Str(required=True)
    isUser = fields.Boolean(default=True)
    isAdmin = fields.Boolean(default=False)
    isSales = fields.Boolean(default=False)

class ModifyPermissionsDone(Schema):
    class Meta:
        type_ = 'modification-done'

    id = fields.Str(required=True, dump_only=True)
    isUser = fields.Boolean(dump_only=True)
    isAdmin = fields.Boolean(dump_only=True)
    isSales = fields.Boolean(dump_only=True)
