from flask import render_template


def register_error_handlers(app):

    @app.errorhandler(404)
    def handle_error(ex):
        return render_template("error-pages/404.jinja2")
