import typing as t
import secrets
import click

from string import Template

from app.utils import filesystem


APP_CONFIG_FILE = "instance/config.py"
INSTANCE_CONFIG_TEXT = """
SECRET_KEY = "$secret_key"
SQLALCHEMY_DATABASE_URI = "$sqlalchemy_database_uri"
"""

DOT_ENV_TEXT = """
FLASK_DEBUG=1
APP_CONFIG=$flask_env
FLASK_RUN_PORT=$flask_port
"""


def ask_for_database_uri() -> t.Any:
    click.echo(click.style("> Let's add database support:", fg="green", bold=True))
    click.echo("""
        Format: postgresql://<user>:<password>@localhost:5432/<db>\n
        Or leave it empty, if you don't need database support
        """)

    return click.prompt("Database URI", default="")


def create_instance_config() -> str:
    secret_key: str = secrets.token_hex()
    sqlalchemy_database_uri: t.Any = ask_for_database_uri()

    variables: dict = {
        "secret_key": secret_key,
        "sqlalchemy_database_uri": sqlalchemy_database_uri
    }

    filesystem.set_file(
        APP_CONFIG_FILE,
        Template(INSTANCE_CONFIG_TEXT).substitute(variables)
    )

    click.echo(click.style("[x] %s created." % APP_CONFIG_FILE, fg="green", bold=True))

    return sqlalchemy_database_uri


def create_dot_env() -> None:
    flask_env: t.Any = click.prompt("APP_CONFIG", default="development")

    if flask_env != "production":
        flask_port: str = click.prompt("FLASK_RUN_PORT", default="5000")
        filesystem.set_file(".env", Template(DOT_ENV_TEXT).substitute({
            "flask_env": flask_env,
            "flask_port": flask_port
        }))
        click.echo(click.style("[x] .env created.", fg="green", bold=True))

    else:
        click.echo(click.style("[] .env ignored.", fg="green", bold=True))


@click.command()
def init_config() -> None:
    click.echo(click.style("*** Starting initial configuration ***", fg="green", bold=True))

    # instance/config.py
    if filesystem.has_file(APP_CONFIG_FILE):
        click.echo("Looks like you already have %s" % APP_CONFIG_FILE)
    else:
        create_instance_config()

    # .env
    if filesystem.has_file(".env"):
        click.echo("Looks like you already have .env")
    else:
        create_dot_env()

    click.echo(click.style("All done. Now you can use 'flask run'", fg="green", bold=True))


if __name__ == '__main__':
    init_config()
