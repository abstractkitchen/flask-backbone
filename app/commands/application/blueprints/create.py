import re
import os
import typing as t

import shutil
import click

from string import Template
from simple_term_menu import TerminalMenu

from flask import current_app
from flask.cli import with_appcontext

from app.blueprints.utils import list_boilerplate_skeletons, list_boilerplate_models
from app.utils import snake_to_camel, filesystem


def validate_bp_name(ctx: click.core.Context, param: str, value: str) -> t.Union[None, str]:
    def fail(text):
        return ctx.fail(click.style(text, fg="red", bold=True))

    if not bool(re.match("^[a-z0-9_]*$", value)):
        fail("Blueprint name must contain lowercase characters and/or underscore symbol.")

    if not bool(re.match("^[a-z]*$", value[0])):
        fail("Blueprint name must start with a letter.")

    return value


def create_blueprint(skeleton_name: str, view_style: list, name: str, create_model: bool, url_rule: str) -> None:
    def echo_success(msg: str) -> None:
        click.echo(click.style(msg, fg="green", bold=True))

    available_models: list = list_boilerplate_models(current_app.config.get("BLUEPRINTS_BOILERPLATE"))
    boilerplate_folder: str = current_app.config.get('BLUEPRINTS_BOILERPLATE')
    blueprints_folder: str = current_app.config.get("BLUEPRINTS_DIRECTORY")
    view_style_folder: str = view_style[1]

    template_vars: dict = {
        **{
            "model_name": "%sModel" % snake_to_camel(name),
            "view_name": "%sView" % snake_to_camel(name),
            "view_name_api": "%sAPI" % snake_to_camel(name),
            "blueprint_name": name,
            "blueprint_name_camelcase": snake_to_camel(name),
            "blueprint_name_route": "%s_route" % name,
            "url_rule": url_rule
        },
        **current_app.config.get("BLUEPRINTS_BOILERPLATE_CUSTOM_VARS")
    }

    # 1: Create blueprint structure
    dest_path: str = os.path.join(os.getcwd(), blueprints_folder, name)
    templates_path: str = f"{dest_path}/templates/{name}/"

    shutil.copytree(
        os.path.join(boilerplate_folder + "/skeletons", skeleton_name),
        dest_path
    )
    echo_success("[x] Structure created.")

    # 1.1: Create templates folder
    filesystem.create_folder_if_not(templates_path)
    filesystem.set_file(
        f"{templates_path}index.jinja2",
        f"<p>Welcome to your {name} blueprint route.</p>"
    )

    echo_success("[x] Templates folder created.")

    # 2: Create model
    if create_model:
        model_selection_menu: TerminalMenu = TerminalMenu(
            available_models,
            title="Select future model template"
        )
        model_template: str = available_models[model_selection_menu.show()]

        with open('%s/models/%s' % (boilerplate_folder, model_template), 'r') as f:
            model_text: str = Template(f.read()).substitute(template_vars)

        filesystem.set_file("%s/models/%s.py" % (dest_path, name), model_text)

        echo_success("[x] Model created")

    else:
        click.echo(click.style("[ ] Model not selected and ignored.", fg="cyan"))

    # 3: Modify files according to view_style
    if view_style_folder:
        view_template: str = view_style_folder + "/view.py.template"
        routes_template: str = view_style_folder + "/routes.py.template"

        if filesystem.has_file(view_template):
            view_script: t.IO = open(view_template, "r")
            filesystem.set_file("%s/views/%s.py" % (dest_path, name), view_script.read())

        if filesystem.has_file(routes_template):
            routes_script: t.IO = open(routes_template, "r")
            filesystem.set_file("%s/routes.py" % dest_path, routes_script.read())

        echo_success("[x] View style updated according to %s" % view_style[0])

    else:
        click.echo(click.style("[ ] View style not selected and ignored.", fg="cyan"))

    # 4: Replace string templates in .py files
    filesystem.replace_templates_in_files(dest_path, ".py", template_vars, ["__init__.py"])

    echo_success("[x] Template variables injected.")
    echo_success("All done. Now you can start customizing your newly created blueprint.")
    echo_success(f"› {dest_path}")


@click.command('create-blueprint')
@click.option('--name', help='Blueprint name', prompt='Enter blueprint name', callback=validate_bp_name)
@click.option('--create-model', is_flag=True, prompt='Create default model?', default=True,
              show_default=True, help='Use, if you need empty model')
@click.option('--url-rule', prompt='Set your initial url rule', help='Set initial url rule', default='')
@click.option('--skeleton', help='Skeleton name (folder name)')
@with_appcontext
def command_create_blueprint(name: str, create_model: bool, url_rule: str, skeleton: str) -> None:
    available_view_styles: list = current_app.config.get("BLUEPRINTS_VIEW_STYLES")
    available_skeletons: list = list_boilerplate_skeletons(current_app.config.get("BLUEPRINTS_BOILERPLATE"))

    if not skeleton:
        skeleton_selection_menu: TerminalMenu = TerminalMenu(
            available_skeletons,
            title="Select skeleton (Your future blueprint structure)"
        )
        skeleton: str = available_skeletons[skeleton_selection_menu.show()]

    click.echo(f"Skeleton: {skeleton}")

    view_style_selection_menu = TerminalMenu(
        list(map(lambda x: x[0], available_view_styles)),
        title="Select view style. https://flask.palletsprojects.com/en/2.2.x/views/"
    )
    view_style_index: int = view_style_selection_menu.show()
    view_style: list = available_view_styles[view_style_index]
    click.echo("View style: %s" % view_style[0])

    create_blueprint(skeleton, view_style, name, create_model, url_rule)
