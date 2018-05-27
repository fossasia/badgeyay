from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import fields


class FileSchema(Schema):
    class Meta:
        type_ = 'File'
        self_view = 'fileUploader.get_file'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    filename = fields.Str(required=True)
    filetype = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/get_file',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )
