from item_parser.Items import (
    Item,
    NormalItem,
    ConjuredItem,
    AgedBrie,
    Sulfuras,
    Backstage,
)


class Hook:
    priority = -1
    base_class = Item

    def __init__(self, raw_item_data):
        self.raw_item_data = raw_item_data

    @classmethod
    def get_priority(cls):
        return cls.priority

    @classmethod
    def __create_item_from_raw_data(cls, data):
        return cls.base_class(
            name=data["name"],
            sell_in=int(data["sellIn"]),
            quality=int(data["quality"]),
        )

    def can_hook(self):
        pass

    def hook(self):
        return self.__create_item_from_raw_data(self.raw_item_data)


class NormalItemHook(Hook):
    priority = 1
    base_class = NormalItem

    def can_hook(self):
        return True


class ConjuredItemHook(Hook):
    priority = 2
    base_class = ConjuredItem

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Conjured")


class AgedBrieHook(Hook):
    priority = 2
    base_class = AgedBrie

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Aged Brie")


class SulfurasHook(Hook):
    priority = 2
    base_class = Sulfuras

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Sulfuras")


class BackstageHook(Hook):
    priority = 2
    base_class = Backstage

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Backstage passes")
