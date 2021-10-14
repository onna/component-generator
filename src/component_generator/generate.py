import os
from typing import Dict, Optional


def generate(structure: Dict[str, str], settings: Dict[str, str]):
    for filepath, filedata in structure.items():
        if filepath.startswith("+"):
            insert_info_file(filepath[1:], filedata, settings)
        else:
            generate_file(filepath, filedata, settings)


def insert_info_file(filepath: str, filedata_part: str, settings: Dict[str, str]):
    pass


def generate_file(filepath: str, filedata: str, settings: Dict[str, str]):
    pass


def create_folder_for_filepath(filepath: str):
    try:
        folderpath = filepath[:filepath.rindex("/")]
        os.makedirs(folderpath)
    except (ValueError, FileExistsError):
        pass
