from flask import Flask
from flask_smorest import Api

from endpoints import images, users, labels

# create backend
app = Flask('DatasetClassificationTool')

# settings
app.config['OPENAPI_URL_PREFIX'] = '/api'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_REDOC_PATH'] = '/redoc'
app.config['OPENAPI_REDOC_URL'] = 'https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js'

# api
api = Api(app)
api.register_blueprint(images)
api.register_blueprint(users)
api.register_blueprint(labels)

# run it!!!
if __name__ == '__main__':
    app.run()
