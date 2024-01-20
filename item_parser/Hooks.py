from item_parser.Items import NormalItem, ConjuredItem, AgedBrie, Sulfuras, Backstage


class Hook:
    priority = -1

    def __init__(self, raw_item_data):
        self.raw_item_data = raw_item_data

    @classmethod
    def get_priority(cls):
        return cls.priority

    def can_hook(self):
        pass

    def hook(self):
        pass


class NormalItemHook(Hook):
    priority = 1

    def can_hook(self):
        return True

    def hook(self):
        return NormalItem(
            name=self.raw_item_data["name"],
            sell_in=self.raw_item_data["sellIn"],
            quality=self.raw_item_data["quality"],
        )


class ConjuredItemHook(Hook):
    priority = 2

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Conjured")

    def hook(self):
        return ConjuredItem(
            name=self.raw_item_data["name"],
            sell_in=self.raw_item_data["sellIn"],
            quality=self.raw_item_data["quality"],
        )


class AgedBrieHook(Hook):
    priority = 2

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Aged Brie")

    def hook(self):
        return AgedBrie(
            name=self.raw_item_data["name"],
            sell_in=self.raw_item_data["sellIn"],
            quality=self.raw_item_data["quality"],
        )


class SulfurasHook(Hook):
    priority = 2

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Sulfuras")

    def hook(self):
        return Sulfuras(
            name=self.raw_item_data["name"],
            sell_in=self.raw_item_data["sellIn"],
            quality=self.raw_item_data["quality"],
        )


class BackstageHook(Hook):
    priority = 2

    def can_hook(self):
        return self.raw_item_data["name"].startswith("Backstage passes")

    def hook(self):
        return Backstage(
            name=self.raw_item_data["name"],
            sell_in=self.raw_item_data["sellIn"],
            quality=self.raw_item_data["quality"],
        )
