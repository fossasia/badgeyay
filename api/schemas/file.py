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


class ManualFileSchema(Schema):
    class Meta:
        type_ = 'text-data'
        self_view = 'fileUploader.upload_manual_data'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    filename = fields.Str(required=True)
    filetype = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/manual_data',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )


class CSVUploadSchema(Schema):
    class Meta:
        type_ = 'csv-file'
        self_view = 'fileUploader.fileUpload'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    filename = fields.Str(required=True)
    filetype = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/manual_data',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )


class ImageFileSchema(Schema):
    class Meta:
        type_ = 'img-file'
        self_view = 'fileUploader.uploadImage'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    filename = fields.Str(required=True)
    filetype = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/manual_data',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )


class DefImageSchem(Schema):
    class Meta:
        type_ = 'def-image-uploads'
        self_view = 'fileUploader.upload_default'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    filename = fields.Str(required=True)
    filetype = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/manual_data',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )


class ColorImageSchema(Schema):
    class Meta:
        type_ = 'bg-color'
        self_view = 'fileUploader.background_color'
        kwargs = {'id': '<id>'}

    id = fields.Str(required=True, dump_only=True)
    filename = fields.Str(required=True)
    filetype = fields.Str(required=True)
    user_id = fields.Relationship(
        self_url='/api/upload/background_color',
        self_url_kwargs={'file_id': '<id>'},
        related_url='/user/register',
        related_url_kwargs={'id': '<id>'},
        include_resource_linkage=True,
        type_='User'
    )
