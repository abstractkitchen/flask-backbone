import os
import glob
import shutil

from pathlib import Path
from string import Template


def create_folder_if_not(folder_path):
    return os.makedirs(os.path.dirname(folder_path), exist_ok=True)


def list_files(directory, **kwargs):
    ignore = kwargs.get("ignore", [""])
    file_extension = kwargs.get("file_extension")

    files = []

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            if file not in ignore:
                if file_extension and file.endswith(file_extension):
                    files.append(file)

                elif not file_extension:
                    files.append(file)

    return files


def list_directories(directory, ignore=None):
    if not ignore:
        ignore = ["__pycache__"]

    return list(
        filter(
            lambda x: os.path.isdir(os.path.join(directory, x)) and x not in ignore,
            os.listdir(directory)
        )
    )


def set_file(file_path, file_content):
    with open(file_path, 'w') as f:
        f.write(file_content)
        f.close()


def has_file(file_path):
    potential_file = Path(file_path)

    return potential_file.is_file()


def copy_file(src, dest):
    return shutil.copy(src, dest)


def read_file(file_path):
    return open(file_path, 'r')


def replace_templates_in_files(lookup_path, file_extension, template_vars, ignore=None):
    if not ignore:
        ignore = []

    files = [f for f in glob.glob(lookup_path + "/**/*%s" % file_extension, recursive=True)]

    for f in files:
        if f.split("/")[-1] not in ignore:
            file = open(f, 'r')
            file_content = Template(file.read()).substitute(template_vars)
            file.close()

            file = open(f, 'w')
            file.write(file_content)
            file.close()
