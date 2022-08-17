"""
https://flask.palletsprojects.com/en/2.2.x/templating/#context-processors

"""


def register_context_processor(app):

    @app.context_processor
    def inject_is_production():
        return dict(
            application_name="Flask-Backbone"
        )
