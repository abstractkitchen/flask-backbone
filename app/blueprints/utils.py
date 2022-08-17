from app.utils import filesystem


IGNORE_FOLDERS = ["__pycache__", "__boilerplate__"]


def list_blueprints(blueprints_folder, cb=None):
    available_blueprints = \
        filesystem.list_directories(blueprints_folder, IGNORE_FOLDERS)

    if cb:
        for blueprint_name in available_blueprints:
            cb(blueprint_name)

    return available_blueprints


# List available skeletons(aka structure) for future blueprints
def list_boilerplate_skeletons(boilerplate_folder):
    return filesystem.list_directories(boilerplate_folder + "/skeletons")


def list_boilerplate_models(boilerplate_folder):
    return filesystem.list_files(
        boilerplate_folder + "/models", file_extension="py.template")
