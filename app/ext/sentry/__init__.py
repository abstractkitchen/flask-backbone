# more on this:
# https://flask.palletsprojects.com/en/2.2.x/errorhandling/

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def init_sentry(app):
    if app.config.get("SENTRY_ENABLED"):
        sentry_sdk.init(
            app.config.get("SENTRY_DSN"),
            integrations=[FlaskIntegration()]
        )
