from flask import Blueprint, current_app


# do not rename "blueprint" variable if you want to use auto import
blueprint = Blueprint(
    '$blueprint_name',
    __name__,
    template_folder='templates'
)
