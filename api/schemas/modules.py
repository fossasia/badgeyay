from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class ModuleSchema(Schema):
    class Meta:
        type_ = 'modules'

    id = fields.Integer(dump_only=True, as_string=True)
    ticketInclude = fields.Boolean(required=True)
    paymentInclude = fields.Boolean(required=True)
    donationInclude = fields.Boolean(required=True)
