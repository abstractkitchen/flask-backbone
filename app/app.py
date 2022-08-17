import os

from flask import Flask, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

from app.ext.sqlalchemy.database import init_database

from app import blueprints

from app.jinja import register_jinja_mapping
from app.errors import register_error_handlers

from app.ext.sentry import init_sentry
from app.ext.cache import cache

from app.commands import init_app_cli


def init_configuration(app):

    # Load the default configuration
    app.config.from_object('config.default')

    # Load the configuration from the instance folder
    app.config.from_pyfile('config.py')

    # Variables defined here will override those in the default configuration
    app.config.from_object(f"config.{os.environ.get('APP_CONFIG')}")


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # first, init configurations
    init_configuration(app)

    init_sentry(app)

    if len(app.config.get("SQLALCHEMY_DATABASE_URI")):
        init_database(app)

    cache.init_app(app)
    register_jinja_mapping(app)

    # automatically enabled when DEBUG_TB_ENABLED=True
    # https://github.com/flask-debugtoolbar/
    DebugToolbarExtension(app)

    # https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.url_map
    app.url_map.strict_slashes = app.config.get("FLASK_STRICT_SLASHES")

    @app.before_request
    def app_before_request():
        request_path = request.path

        # redirect: example.com/url/ -> example.com/url
        if request_path != '/' and request_path.endswith('/'):
            return redirect(request_path[:-1], 301)

    register_error_handlers(app)
    blueprints.register_blueprints(app)

    # initialize application commands from app/commands
    init_app_cli(app)

    return app
