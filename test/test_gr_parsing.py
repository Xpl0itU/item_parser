from item_parser.GRParser import GRParser
from item_parser.Item import Item
import pytest


@pytest.fixture
def single_day_data():
    return """-------- day 0 --------
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
"""


def test_parse_string_with_valid_data_single_day(single_day_data):
    parser = GRParser(single_day_data)
    print(parser.data)
    result = parser.parse_string()

    assert result == {
        "0": [
            Item(name="+5 Dexterity Vest", sell_in="10", quality="20"),
            Item(name="Aged Brie", sell_in="2", quality="0"),
            Item(name="Elixir of the Mongoose", sell_in="5", quality="7"),
        ]
    }


def test_parse_string_with_invalid_data():
    invalid_data = "Invalid data"
    parser = GRParser(invalid_data)
    result = parser.parse_string()

    assert result == {}


def test_parse_string_with_empty_data():
    empty_data = ""
    parser = GRParser(empty_data)
    result = parser.parse_string()

    assert result == {}
