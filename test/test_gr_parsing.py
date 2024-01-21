from item_parser.GRParser import GRParser
from item_parser.Items import NormalItem, AgedBrie, ConjuredItem, Sulfuras, Backstage


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
            NormalItem(name="+5 Dexterity Vest", sellIn=10, quality=20),
            AgedBrie(name="Aged Brie", sellIn=2, quality=0),
            NormalItem(name="Elixir of the Mongoose", sellIn=5, quality=7),
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
            NormalItem(name="+5 Dexterity Vest", sellIn=10, quality=20),
            AgedBrie(name="Aged Brie", sellIn=2, quality=0),
            NormalItem(name="Elixir of the Mongoose", sellIn=5, quality=7),
        ],
        2: [
            NormalItem(name="+5 Dexterity Vest", sellIn=9, quality=19),
            AgedBrie(name="Aged Brie", sellIn=1, quality=1),
            NormalItem(name="Elixir of the Mongoose", sellIn=4, quality=6),
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
            NormalItem(name="+5 Dexterity Vest", sellIn=-10, quality=20),
        ]
    }


def test_parse_string_with_aged_brie_item():
    aged_brie_item_data = """-------- day 1 --------
name, sellIn, quality
Aged Brie, 2, 0
"""
    parser = GRParser(aged_brie_item_data)
    result = parser.parse_string()

    assert result == {
        1: [
            AgedBrie(name="Aged Brie", sellIn=2, quality=0),
        ]
    }


def test_parse_string_with_conjured_item():
    conjured_item_data = """-------- day 1 --------
name, sellIn, quality
Conjured Mana Cake, 3, 6
"""
    parser = GRParser(conjured_item_data)
    result = parser.parse_string()

    assert result == {
        1: [
            ConjuredItem(name="Conjured Mana Cake", sellIn=3, quality=6),
        ]
    }


def test_parse_string_with_sulfuras_item():
    sulfuras_item_data = """-------- day 1 --------
name, sellIn, quality
Sulfuras, Hand of Ragnaros, 0, 80
"""
    parser = GRParser(sulfuras_item_data)
    result = parser.parse_string()

    assert result == {
        1: [
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sellIn=0, quality=80),
        ]
    }


def test_parse_string_with_backstage_item():
    backstage_item_data = """-------- day 1 --------
name, sellIn, quality
Backstage passes to a TAFKAL80ETC concert, 15, 20
"""
    parser = GRParser(backstage_item_data)
    result = parser.parse_string()

    assert result == {
        1: [
            Backstage(
                name="Backstage passes to a TAFKAL80ETC concert",
                sellIn=15,
                quality=20,
            ),
        ]
    }
