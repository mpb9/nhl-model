from flask import Flask
from gui import pages
from gui.controller import glossary_controller, bp_by_team


def create_app() -> Flask:
    app = Flask(import_name=__name__)
    app.register_blueprint(blueprint=pages.bp)
    app.register_blueprint(blueprint=glossary_controller.bp)
    app.register_blueprint(blueprint=bp_by_team.bp)
    return app
