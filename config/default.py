# https://flask.palletsprojects.com/en/2.2.x/config/#builtin-configuration-values

DEBUG = False
IS_PRODUCTION = False

# https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.url_map
FLASK_STRICT_SLASHES = False

# https://flask-caching.readthedocs.io/en/latest/
CACHE_TYPE = "NullCache"

# SQLAlchemy
SQLALCHEMY_AUTOCOMMIT = False
SQLALCHEMY_AUTOFLUSH = False
SQLALCHEMY_ENGINE_ECHO = False

# Blueprints configuration. Only change this at your own risk.
BLUEPRINTS_DIRECTORY = "app/blueprints"
BLUEPRINTS_BOILERPLATE = BLUEPRINTS_DIRECTORY + "/__boilerplate__"
BLUEPRINTS_VIEW_STYLES = [
    ["None", ""],
    ["Standard (url rule decorator)", BLUEPRINTS_BOILERPLATE + "/views/standard"],
    ["flask.views.View", BLUEPRINTS_BOILERPLATE + "/views/flask_view"],
    ["flask.views.MethodView", BLUEPRINTS_BOILERPLATE + "/views/flask_mv"]
]


# override this value in instance/config.py
# flask-sentry configuration. sentry-sdk[flask]
SENTRY_ENABLED = False
SENTRY_DSN = ""


# *******************************************************************
# ****** AFTER THIS LINE YOU CAN DEFINE YOU OWN DEFAULT CONFIGURATIONS ******
# *******************************************************************

# ADVANCED: Add your own blueprint boilerplate view styles
BLUEPRINTS_VIEW_STYLES = BLUEPRINTS_VIEW_STYLES + [

]

# Pass custom params when creating a new blueprint
# you can use them as follows in *.py files: $variable_name
# those vars are reserved:
# - model_name, blueprint_name, blueprint_name_camelcase, url_rule
BLUEPRINTS_BOILERPLATE_CUSTOM_VARS = {
    "version": "0.1"
}
