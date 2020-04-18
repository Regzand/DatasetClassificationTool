import marshmallow as ma


class UserSchema(ma.Schema):
    username = ma.fields.String(required=True, dump_only=True)
    displayname = ma.fields.String(required=True, dump_only=True)
