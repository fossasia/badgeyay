from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class BadgeSchema(Schema):
    class Meta:
        type_ = 'badge'
        self_view = 'generateBadges.generateBadges'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    badge_name = fields.Str(required=True)
    image = fields.Str(required=True)
    csv = fields.Str(required=True)
    csv_type = fields.Str(required=True)
    ticket_types = fields.Str(required=True)
    text_color = fields.Str(required=True)
    badge_size = fields.Str(required=True)
    download_link = fields.Str(required=True)
    created_at = fields.Date(required=True)
    image_link = fields.Str(required=True)
    logo_image_link = fields.Str(required=True)
    logo_text = fields.Str()
    logo_color = fields.Str()
    logo_image = fields.Str()
    font_color_1 = fields.Str(required=True)
    font_color_2 = fields.Str(required=True)
    font_color_3 = fields.Str(required=True)
    font_color_4 = fields.Str(required=True)
    font_color_5 = fields.Str(required=True)
    font_size_1 = fields.Str()
    font_size_2 = fields.Str()
    font_size_3 = fields.Str()
    font_size_4 = fields.Str()
    font_size_5 = fields.Str()
    font_type_1 = fields.Str(required=True)
    font_type_2 = fields.Str(required=True)
    font_type_3 = fields.Str(required=True)
    font_type_4 = fields.Str(required=True)
    font_type_5 = fields.Str(required=True)
    paper_size = fields.Str(required=True)
    download_link = fields.Str()


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
    paper_size = fields.Str(required=True)
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
