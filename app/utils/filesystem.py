import os
import glob
import shutil

import typing as t

from pathlib import Path
from string import Template


def create_folder_if_not(folder_path: str) -> None:
    return os.makedirs(os.path.dirname(folder_path), exist_ok=True)


def list_files(directory: str, **kwargs) -> t.List[str]:
    ignore: list = kwargs.get("ignore", [""])
    file_extension: t.Union[str, None] = kwargs.get("file_extension")

    files: list = []

    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            if file not in ignore:
                if file_extension and file.endswith(file_extension):
                    files.append(file)

                elif not file_extension:
                    files.append(file)

    return files


def list_directories(directory: str, ignore: t.Union[None, list] = None) -> t.List[str]:
    if not ignore:
        ignore: list = ["__pycache__"]

    return list(
        filter(
            lambda x: os.path.isdir(os.path.join(directory, x)) and x not in ignore,
            os.listdir(directory)
        )
    )


def set_file(file_path: str, file_content: str) -> None:
    with open(file_path, 'w') as f:
        f.write(file_content)
        f.close()


def has_file(file_path: str) -> bool:
    potential_file = Path(file_path)

    return potential_file.is_file()


def copy_file(src: str, dest: str) -> str:
    return shutil.copy(src, dest)


def read_file(file_path: str) -> t.IO:
    return open(file_path, 'r')


def replace_templates_in_files(
        lookup_path: str, file_extension: str, template_vars: dict, ignore: t.Union[None, t.List[str]] = None) -> None:

    if not ignore:
        ignore: list = []

    files: t.List[str] = [f for f in glob.glob(lookup_path + "/**/*%s" % file_extension, recursive=True)]

    for f in files:
        if f.split("/")[-1] not in ignore:
            file: t.IO = open(f, 'r')
            file_content = Template(file.read()).substitute(template_vars)
            file.close()

            file: t.IO = open(f, 'w')
            file.write(file_content)
            file.close()
