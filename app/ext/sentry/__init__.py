# more on this:
# https://flask.palletsprojects.com/en/2.2.x/errorhandling/

import sentry_sdk

from flask import Flask


def init_sentry(app: Flask) -> None:
    if app.config.get("SENTRY_ENABLED"):
        sentry_sdk.init(
            app.config.get("SENTRY_DSN"),
            integrations=[sentry_sdk.integrations.flask.FlaskIntegration()]
        )
