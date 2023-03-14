import typing as t

from flask import render_template, Flask


def register_error_handlers(app: Flask) -> None:

    @app.errorhandler(404)
    def handle_error(ex: t.Union[t.Type[Exception], int]) -> str:
        return render_template("error-pages/404.jinja2")
