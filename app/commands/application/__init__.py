from flask.cli import AppGroup

from app.commands.application.blueprints.create import command_create_blueprint
from app.commands.application.blueprints.list import list_blueprints_command

app_cli = AppGroup('app')

app_cli.add_command(command_create_blueprint)
app_cli.add_command(list_blueprints_command)
