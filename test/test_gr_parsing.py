from item_parser.GRParser import GRParser


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
        1: [
            {"name": "+5 Dexterity Vest", "sellIn": 10, "quality": 20},
            {"name": "Aged Brie", "sellIn": 2, "quality": 0},
            {"name": "Elixir of the Mongoose", "sellIn": 5, "quality": 7},
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
        1: [
            {"name": "+5 Dexterity Vest", "sellIn": 10, "quality": 20},
            {"name": "Aged Brie", "sellIn": 2, "quality": 0},
            {"name": "Elixir of the Mongoose", "sellIn": 5, "quality": 7},
        ],
        2: [
            {"name": "+5 Dexterity Vest", "sellIn": 9, "quality": 19},
            {"name": "Aged Brie", "sellIn": 1, "quality": 1},
            {"name": "Elixir of the Mongoose", "sellIn": 4, "quality": 6},
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


def test_parse_string_with_negative_sellIn_values():
    negative_sellIn_data = """-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, -10, 20
"""
    parser = GRParser(negative_sellIn_data)
    result = parser.parse_string()

    assert result == {
        1: [
            {"name": "+5 Dexterity Vest", "sellIn": -10, "quality": 20},
        ]
    }
