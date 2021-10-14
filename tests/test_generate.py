from pytest_mock import MockFixture

from component_generator.generate import generate


def test_generate_should_call_insert_info_file_if_filepath_startswith_plus(mocker: MockFixture):
    insert_info_spy = mocker.patch("component_generator.generate.insert_info_file")
    generate({"+insert_info": "dummy", "generate": "dummy"}, {})
    insert_info_spy.assert_called_once_with("insert_info", "dummy", {})


def test_generate_should_call_generate_file_if_filepath_not_startswith_plus(mocker: MockFixture):
    generate_file_spy = mocker.patch("component_generator.generate.generate_file")
    generate({"+insert_info": "dummy", "generate": "dummy"}, {})
    generate_file_spy.assert_called_once_with("generate", "dummy", {})
