import click

from flask import current_app
from flask.cli import with_appcontext


@click.command('me')
@click.option('--name', prompt='Enter your name')
@with_appcontext
def command_about_me(name):
    click.echo(f"Your name: {name}")


def init_blueprint_cli(blueprint):
    blueprint.cli.add_command(command_about_me)
