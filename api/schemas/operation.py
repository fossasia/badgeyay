from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class ResetPasswordOperation(Schema):
    class Meta:
        type_ = 'reset-passwords'

    id = fields.Str(required=True, dump_only=True)
    status = fields.Str(required=True)


class EmailVerificationOperation(Schema):
    class Meta:
        type_ = 'verify-mails'

    id = fields.Str(required=True, dump_only=True)
    status = fields.Str(required=True)
