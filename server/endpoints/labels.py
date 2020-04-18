from http import HTTPStatus

from flask.views import MethodView
from flask_smorest import Blueprint

import database as db
from schemas import LabelSchema

blp = Blueprint(
    'labels', 'labels', url_prefix='/api/labels',
    description='Operations on labels'
)


@blp.route('/')
class Users(MethodView):

    @blp.response(LabelSchema(many=True), code=HTTPStatus.OK)
    def get(self):
        """ List labels """
        return db.labels.all()
