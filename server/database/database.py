from datetime import datetime

from tinydb import TinyDB
from tinydb_serialization import Serializer, SerializationMiddleware


class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime

    def encode(self, obj):
        return obj.strftime('%Y-%m-%dT%H:%M:%S')

    def decode(self, s):
        return datetime.strptime(s, '%Y-%m-%dT%H:%M:%S')


class Database(TinyDB):

    def __init__(self, *args, **kwargs):
        serialization = SerializationMiddleware()

        serialization.register_serializer(DateTimeSerializer(), 'TinyDate')

        kwargs['storage'] = serialization
        super().__init__(*args, **kwargs)
