import os
from typing import Dict

from component_generator.constants import START_BLOCK, END_BLOCK
from component_generator.helpers import populate_setting_values, create_folder_for_filepath


class FileNotUpdatableException(Exception):
    def __init__(self, filepath: str):
        super().__init__(f"File {filepath} not updatable")


def generate(structure: Dict[str, str], settings: Dict[str, str]):
    for filepath, filedata in structure.items():
        if filepath.startswith("+"):
            insert_info_file(filepath[1:], filedata, settings)
        else:
            generate_file(filepath, filedata, settings)


def insert_info_file(filepath: str, filedata_part: str, settings: Dict[str, str]):
    populated_filepath = populate_setting_values(filepath, settings)
    with open(populated_filepath, "r") as reader:
        file_data = reader.read()
    _check_info_file(file_data, populated_filepath)
    with open(populated_filepath, "w") as writer:
        writer.write(_append_filedata(file_data, filedata_part))


def _check_info_file(file_data: str, filepath: str):
    if not (START_BLOCK in file_data and END_BLOCK in file_data):
        raise FileNotUpdatableException(filepath)


def _append_filedata(existing_filedata: str, new_filedata: str) -> str:
    return "\n".join(
        (
            existing_filedata[: existing_filedata.index(END_BLOCK)],
            new_filedata,
            existing_filedata[existing_filedata.index(END_BLOCK) :],
        )
    )


def generate_file(filepath: str, filedata: str, settings: Dict[str, str]):
    populated_filepath = populate_setting_values(filepath, settings)
    create_folder_for_filepath(populated_filepath)

    if os.path.exists(populated_filepath):
        raise FileExistsError
    with open(populated_filepath, "w") as file:
        file.write(populate_setting_values(filedata, settings))
