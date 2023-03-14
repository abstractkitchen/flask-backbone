from flask import Blueprint

from app.blueprints.about.views.about import AboutView
from app.blueprints.about.commands import init_blueprint_cli


blueprint: Blueprint = Blueprint(
    'about',
    __name__,
    template_folder='templates'
)


# todo: set unique name for as_view('<name>') it will be used in flask.url_for()
blueprint.add_url_rule('/about', view_func=AboutView.as_view('about_page'))

init_blueprint_cli(blueprint)
