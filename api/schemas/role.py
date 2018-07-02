from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class AllRoleSchema(Schema):
    class Meta:
        type_ = 'roles'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True, attribute='name')
    created_at = fields.DateTime(required=True)
    deleted_at = fields.DateTime()
