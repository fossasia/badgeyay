from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class BadgeSchema(Schema):
    class Meta:
        type_ = 'Badges'
        self_view = 'generateBadges.generateBadges'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    badge_id = fields.Str(required=True)
    download_link = fields.Str(required=True)


class AllBadges(Schema):
    class Meta:
        type_ = 'all-badges'
        self_view = 'admin.get_all_badges'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    badge_name = fields.Str(required=True)
    image = fields.Str(required=True)
    csv = fields.Str(required=True)
    badge_id = fields.Str(required=True)
    text_color = fields.Str(required=True)
    badge_size = fields.Str(required=True)
    created_at = fields.Date(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/get_file',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )


class UserBadges(Schema):
    class Meta:
        type_ = 'my-badges'
        self_view = 'generateBadges.get_badges'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    badge_name = fields.Str(required=True)
    image = fields.Str(required=True)
    csv = fields.Str(required=True)
    badge_id = fields.Str(required=True)
    text_color = fields.Str(required=True)
    badge_size = fields.Str(required=True)
    download_link = fields.Str(required=True)
    created_at = fields.Date(required=True)
    image_link = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/get_file',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )


class DeletedBadges(Schema):
    class Meta:
        type_ = 'user-badges'
        self_view = 'generateBadges.delete_badge'
        self_view_kwargs = {'badgeId': '<id>'}

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


class DatedBadgeSchema(Schema):
    class Meta:
        type_ = 'dated-badges'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)


class AllGenBadges(Schema):
    class Meta:
        type_ = 'all-badges'
        kwargs = {'id': '<id>'}

    id = fields.Date(required=True, dump_only=True)
    cnt = fields.Str(required=True)
