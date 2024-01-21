import pytest
from item_parser.Hooks import (
    NormalItemHook,
    ConjuredItemHook,
    AgedBrieHook,
    SulfurasHook,
    BackstageHook,
)
from item_parser.Items import NormalItem, ConjuredItem, AgedBrie, Sulfuras, Backstage


@pytest.mark.parametrize(
    "hook_class, raw_item_data, expected_instance, expected_attributes",
    [
        (
            NormalItemHook,
            {"name": "item", "sellIn": "10", "quality": "20"},
            NormalItem,
            {"name": "item", "sell_in": 10, "quality": 20},
        ),
        (
            NormalItemHook,
            {"name": "item", "sellIn": "10", "quality": "abc"},
            Exception,
            None,
        ),
        (
            ConjuredItemHook,
            {"name": "Conjured item", "sellIn": "10", "quality": "20"},
            ConjuredItem,
            {"name": "Conjured item", "sell_in": 10, "quality": 20},
        ),
        (
            ConjuredItemHook,
            {"name": "Conjured item", "sellIn": "10", "quality": "abc"},
            Exception,
            None,
        ),
        (
            AgedBrieHook,
            {"name": "Aged Brie", "sellIn": "10", "quality": "20"},
            AgedBrie,
            {"name": "Aged Brie", "sell_in": 10, "quality": 20},
        ),
        (
            AgedBrieHook,
            {"name": "Aged Brie", "sellIn": "10", "quality": "abc"},
            Exception,
            None,
        ),
        (
            SulfurasHook,
            {"name": "Sulfuras", "sellIn": "10", "quality": "80"},
            Sulfuras,
            {"name": "Sulfuras", "sell_in": 10, "quality": 80},
        ),
        (
            SulfurasHook,
            {"name": "Sulfuras", "sellIn": "10", "quality": "abc"},
            Exception,
            None,
        ),
        (
            BackstageHook,
            {"name": "Backstage", "sellIn": "10", "quality": "20"},
            Backstage,
            {"name": "Backstage", "sell_in": 10, "quality": 20},
        ),
        (
            BackstageHook,
            {"name": "Backstage", "sellIn": "10", "quality": "abc"},
            Exception,
            None,
        ),
    ],
)
def test_hook(hook_class, raw_item_data, expected_instance, expected_attributes):
    hook = hook_class(raw_item_data)

    if expected_instance == Exception:
        with pytest.raises(Exception):
            hook.hook()
    else:
        item = hook.hook()
        assert isinstance(item, expected_instance)

        if expected_attributes:
            for attr, value in expected_attributes.items():
                assert getattr(item, attr) == value
