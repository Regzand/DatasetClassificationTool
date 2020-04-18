import marshmallow as ma
from flask_smorest.fields import Upload


class ImageLabelSchema(ma.Schema):
    code = ma.fields.String(required=True)

    author = ma.fields.String(dump_only=True)
    created = ma.fields.DateTime(dump_only=True)


class ImageSchema(ma.Schema):
    id = ma.fields.Int(attribute='doc_id', dump_only=True)
    uploader = ma.fields.String(dump_only=True)
    labels = ma.fields.List(ma.fields.Nested(ImageLabelSchema), dump_only=True)
    uploaded = ma.fields.DateTime(dump_only=True)


class ImageFileSchema(ma.Schema):
    image = Upload(load_only=True)
