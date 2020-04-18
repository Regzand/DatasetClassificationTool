from http import HTTPStatus

from flask.views import MethodView
from flask_smorest import Blueprint

import database as db
from schemas import UserSchema

blp = Blueprint(
    'users', 'users', url_prefix='/api/users',
    description='Operations on users'
)


@blp.route('/')
class Users(MethodView):

    @blp.response(UserSchema(many=True), code=HTTPStatus.OK)
    def get(self):
        """ List users """
        return db.users.all()
