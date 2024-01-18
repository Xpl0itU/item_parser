from item_parser.GRParser import GRParser
from item_parser.Item import Item


def test_parse_string_with_valid_data_single_day():
    parser = GRParser(
        """-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
"""
    )
    result = parser.parse_string()

    assert result == {
        "1": [
            Item(name="+5 Dexterity Vest", sell_in="10", quality="20"),
            Item(name="Aged Brie", sell_in="2", quality="0"),
            Item(name="Elixir of the Mongoose", sell_in="5", quality="7"),
        ]
    }


def test_parse_string_with_valid_data_multi_day():
    parser = GRParser(
        """-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7

-------- day 2 --------
name, sellIn, quality
+5 Dexterity Vest, 9, 19
Aged Brie, 1, 1
Elixir of the Mongoose, 4, 6
"""
    )
    result = parser.parse_string()

    assert result == {
        "1": [
            Item(name="+5 Dexterity Vest", sell_in="10", quality="20"),
            Item(name="Aged Brie", sell_in="2", quality="0"),
            Item(name="Elixir of the Mongoose", sell_in="5", quality="7"),
        ],
        "2": [
            Item(name="+5 Dexterity Vest", sell_in="9", quality="19"),
            Item(name="Aged Brie", sell_in="1", quality="1"),
            Item(name="Elixir of the Mongoose", sell_in="4", quality="6"),
        ],
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


def test_parse_string_with_negative_sell_in_values():
    negative_sell_in_data = """-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, -10, 20
"""
    parser = GRParser(negative_sell_in_data)
    result = parser.parse_string()

    assert result == {
        "1": [
            Item(name="+5 Dexterity Vest", sell_in="-10", quality="20"),
        ]
    }


def test_parse_string_with_non_integer_values():
    non_integer_values_data = """-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, 10.5, 20.7
"""
    parser = GRParser(non_integer_values_data)
    result = parser.parse_string()

    assert result == {
        "1": [
            Item(name="+5 Dexterity Vest", sell_in="10.5", quality="20.7"),
        ]
    }
