import click

from flask import current_app
from flask.cli import with_appcontext

from app.blueprints.utils import list_blueprints


@click.command("list-blueprints")
@with_appcontext
def list_blueprints_command() -> None:
    available_blueprints: list = list_blueprints(current_app.config.get("BLUEPRINTS_DIRECTORY"))

    [click.echo(bp_name) for bp_name in available_blueprints]
