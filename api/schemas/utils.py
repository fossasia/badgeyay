from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class SetPricingSchema(Schema):
    class Meta:
        type_ = 'set-pricing'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    pricing = fields.Float(required=True)


class ReturnSetPricing(Schema):
    class Meta:
        type_ = 'pricing-done'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    pricing = fields.Float(dump_only=-True)
    status = fields.Str(dump_only=True)
    message = fields.Str(dump_only=True)
