import marshmallow as ma


class LabelSchema(ma.Schema):
    code = ma.fields.String(required=True, dump_only=True)
    description = ma.fields.String(required=True, dump_only=True)
    color = ma.fields.String(required=True, dump_only=True)
