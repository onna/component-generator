from pytest_mock import MockFixture  # type: ignore

from component_generator.generate import generate, create_folder_for_filepath


def test_generate_should_call_insert_info_file_if_filepath_startswith_plus(mocker: MockFixture):
    insert_info_spy = mocker.patch("component_generator.generate.insert_info_file")
    generate({"+insert_info": "dummy", "generate": "dummy"}, {})
    insert_info_spy.assert_called_once_with("insert_info", "dummy", {})


def test_generate_should_call_generate_file_if_filepath_not_startswith_plus(mocker: MockFixture):
    generate_file_spy = mocker.patch("component_generator.generate.generate_file")
    generate({"+insert_info": "dummy", "generate": "dummy"}, {})
    generate_file_spy.assert_called_once_with("generate", "dummy", {})


def test_create_folder_for_filepath(mocker: MockFixture):
    dummy_folder = "dummy_folder"
    mkdir_spy = mocker.patch("os.makedirs")
    create_folder_for_filepath(f"{dummy_folder}/dummy_file")
    mkdir_spy.assert_called_once_with(dummy_folder)


def test_create_folder_for_filepath_with_nested_folderpath(mocker: MockFixture):
    dummy_folderpath = "dummy/folder/child"
    mkdir_spy = mocker.patch("os.makedirs")
    create_folder_for_filepath(f"{dummy_folderpath}/dummy_file")
    mkdir_spy.assert_called_once_with(dummy_folderpath)


def test_create_folder_for_filepath_doesnt_create_anything_if_no_folderpath(mocker: MockFixture):
    mkdir_spy = mocker.patch("os.makedirs")
    create_folder_for_filepath("dummy_file")
    mkdir_spy.assert_not_called()


def test_create_folder_for_filepath_if_folder_already_exists(mocker: MockFixture):
    mocker.patch("os.makedirs", side_effect=FileExistsError())
    create_folder_for_filepath("already_exists/dummy_file")
