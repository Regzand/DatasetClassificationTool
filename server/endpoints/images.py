from datetime import datetime
from http import HTTPStatus

from flask import send_file
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from tinydb import Query
from PIL import Image

import database as db
from schemas import ImageSchema, ImageLabelSchema, ImageFileSchema

blp = Blueprint(
    'images', 'images', url_prefix='/api/images',
    description='Operations on images'
)


@blp.route('/')
class Images(MethodView):

    @blp.response(ImageSchema(many=True), code=HTTPStatus.OK)
    def get(self):
        """ List images """
        return db.images.all()

    @blp.arguments(ImageSchema)
    @blp.arguments(ImageFileSchema, location='files')
    @blp.response(ImageSchema, code=HTTPStatus.CREATED)
    def post(self, data, files):
        """ Add image """

        # create image
        img_id = db.images.insert(dict(
            uploader='TODO',
            labels=[],
            uploaded=datetime.now()
        ))

        # save image file
        image = Image.open(files['image'].stream)
        image.save(f'./images/{img_id}.jpg')

        # return created image
        return db.images.get(doc_id=img_id)


@blp.route('/<int:img_id>')
class ImageById(MethodView):

    @blp.response(ImageSchema, code=HTTPStatus.OK)
    def get(self, img_id):
        """ Get image """
        return db.images.get(doc_id=img_id)


@blp.route('/<int:img_id>/image')
class ImageByIdFile(MethodView):

    def get(self, img_id):
        """ Get image file """

        # validate image id
        if not db.images.contains(doc_ids=[img_id]):
            abort(
                http_status_code=HTTPStatus.BAD_REQUEST,
                message=f'Image with id {img_id} does not exists'
            )

        # return image file
        return send_file(f'./images/{img_id}.jpg')


@blp.route('/<int:img_id>/labels')
class ImageByIdLabels(MethodView):

    @blp.response(ImageLabelSchema(many=True), code=HTTPStatus.OK)
    def get(self, img_id):
        """ Get labels """

        # get image
        img = db.images.get(doc_id=img_id)
        if img is None:
            abort(
                http_status_code=HTTPStatus.BAD_REQUEST,
                message=f'Image with id {img_id} does not exists'
            )

        # return image labels
        return img['labels']

    @blp.arguments(ImageLabelSchema)
    @blp.response(ImageLabelSchema, code=HTTPStatus.CREATED)
    def post(self, data, img_id):
        """ Add label """

        # validate image id
        if not db.images.contains(doc_ids=[img_id]):
            abort(
                http_status_code=HTTPStatus.BAD_REQUEST,
                message=f'Image with id {img_id} does not exists'
            )

        # validate label code
        if not db.labels.contains(Query().code == data['code']):
            abort(
                http_status_code=HTTPStatus.BAD_REQUEST,
                message=f'Unknown label code {data["code"]}'
            )

        # create label
        label = dict(
            code=data['code'],
            author='TODO',
            created=datetime.now()
        )

        # add to image
        db.images.update(
            lambda img: img['labels'].append(label),
            doc_ids=[img_id]
        )

        # return created label
        return label
