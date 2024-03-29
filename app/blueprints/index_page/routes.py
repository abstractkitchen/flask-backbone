from flask import Blueprint, make_response, render_template, current_app, Response


blueprint: Blueprint = Blueprint(
    'index',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@blueprint.route("/", methods=["get"])
def index_route() -> Response:
    return make_response(
        render_template(
            "index.jinja2",
        )
    )


