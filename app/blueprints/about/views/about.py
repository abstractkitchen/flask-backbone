# Learn more here: https://flask.palletsprojects.com/en/2.2.x/views/#method-hints

from flask import request, current_app, render_template
from flask.views import View


class AboutView(View):
    methods = ["GET"]

    def dispatch_request(self):
        # current_app.config.get("MY_CONFIG_VARIABLE")

        context = {
            "hello": "world"
        }

        return render_template(
            "about.jinja2",
            **context
        )
