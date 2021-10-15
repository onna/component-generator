import os
from typing import Dict

from component_generator.helpers import populate_setting_values, create_folder_for_filepath
from component_generator.info_file import append_to_info_file


def generate(structure: Dict[str, str], settings: Dict[str, str]):
    for filepath, filedata in structure.items():
        if filepath.startswith("+"):
            append_to_info_file(filepath[1:], filedata, settings)
        else:
            generate_file(filepath, filedata, settings)


def generate_file(filepath: str, filedata: str, settings: Dict[str, str]):
    populated_filepath = populate_setting_values(filepath, settings)
    create_folder_for_filepath(populated_filepath)

    if os.path.exists(populated_filepath):
        raise FileExistsError
    with open(populated_filepath, "w") as file:
        file.write(populate_setting_values(filedata, settings))
