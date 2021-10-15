import os
from typing import Dict


def generate(structure: Dict[str, str], settings: Dict[str, str]):
    for filepath, filedata in structure.items():
        if filepath.startswith("+"):
            insert_info_file(filepath[1:], filedata, settings)
        else:
            generate_file(filepath, filedata, settings)


def insert_info_file(filepath: str, filedata_part: str, settings: Dict[str, str]):
    pass


def generate_file(filepath: str, filedata: str, settings: Dict[str, str]):
    populated_filepath = populate_setting_values(filepath, settings)
    create_folder_for_filepath(populated_filepath)

    if os.path.exists(populated_filepath):
        raise FileExistsError
    with open(populated_filepath, "w") as file:
        file.write(populate_setting_values(filedata, settings))


def populate_setting_values(string: str, settings: Dict[str, str]) -> str:
    for key, val in settings.items():
        string = string.replace(f"${{{key}}}", val)
    return string


def create_folder_for_filepath(filepath: str):
    try:
        folderpath = filepath[: filepath.rindex("/")]
        os.makedirs(folderpath)
    except (ValueError, FileExistsError):
        pass
