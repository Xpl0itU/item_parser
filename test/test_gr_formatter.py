from item_parser.ParsedGRDataFormatter import ParsedGRDataFormatter
import os


def test_format_parsed_data():
    parsed_data = {
        1: [
            {"name": "item1", "sellIn": 10, "quality": 5},
            {"name": "item2", "sellIn": 5, "quality": 10},
        ]
    }
    formatter = ParsedGRDataFormatter(parsed_data)
    expected_output = (
        "-------- day 1 --------\nname, sellIn, quality\nitem1, 10, 5\nitem2, 5, 10\n"
    )

    assert str(formatter) == expected_output


def test_empty_parsed_data():
    parsed_data = {}
    formatter = ParsedGRDataFormatter(parsed_data)
    expected_output = ""
    assert str(formatter) == expected_output


def test_export_to_file():
    parsed_data = {
        1: [
            {"name": "item1", "sellIn": 10, "quality": 5},
            {"name": "item2", "sellIn": 5, "quality": 10},
        ]
    }
    formatter = ParsedGRDataFormatter(parsed_data)
    formatter.export_to_file("test.txt")
    with open("test.txt", "r", encoding="utf-8") as file:
        assert file.read() == str(formatter)
    os.remove("test.txt")
