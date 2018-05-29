from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class BadgeSchema(Schema):
    class Meta:
        type_ = 'Badges'
        self_view = 'generateBadges.generateBadges'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    image = fields.Str(required=True)
    csv = fields.Str(required=True)
    badge_id = fields.Str(required=True)
    text_color = fields.Str(required=True)
    badge_size = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/get_file',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )
