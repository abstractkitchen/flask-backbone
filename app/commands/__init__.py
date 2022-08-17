# Register your custom commands here.

from app.commands.application import app_cli


def init_app_cli(app):
    app.cli.add_command(app_cli)
