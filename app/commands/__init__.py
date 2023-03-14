# Register your custom commands here.
from flask import Flask

from app.commands.application import app_cli


def init_app_cli(app: Flask) -> None:
    app.cli.add_command(app_cli)
