from flask import Flask
from flask_restplus import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint

# from api_config import pages

# MARK: Swagger UI
SWAGGER_URL = "/swagger"
API_URL = "http://127.0.0.1:8080/swagger.json"


def create_app() -> Flask:
    app = Flask(import_name=__name__)
    # app.register_blueprint(blueprint=pages.bp)
    # return app
    api = Api(app=app)
