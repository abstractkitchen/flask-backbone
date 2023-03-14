"""
Import blueprints from the folder structure.

You can remove code below and import blueprints one by one, like so:

    from app.blueprints.user.routes import blueprint as user_blueprint

    def register_blueprints(app):
        app.register_blueprint(user_blueprint)

"""

from flask import Flask
from importlib import import_module

from app.blueprints.utils import list_blueprints


def register_blueprints(app: Flask) -> None:
    for blueprint_name in list_blueprints(app.config.get("BLUEPRINTS_DIRECTORY")):
        blueprint_module = import_module(f"app.blueprints.{blueprint_name}.routes")

        app.register_blueprint(blueprint_module.blueprint)
