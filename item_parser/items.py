from dataclasses import dataclass


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int


class Interface:
    def update_quality(self):
        pass


class NormalItem(Item, Interface):
    def setSell_in(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality = self.quality + value
        else:
            self.quality = 0
        assert (
            0 <= self.quality <= 50
        ), f"{self.__class__.__name__}'s quality out of range"

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSell_in()


class ConjuredItem(NormalItem):
    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()


class AgedBrie(NormalItem):
    def setQuality(self, value):
        super().setQuality(self, value)

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()


class Sulfuras(NormalItem):
    def update_quality(self):
        assert self.quality == 80, f"{self.__class__.__name__}'s quality isn't 80"


class Backstage(NormalItem):
    def setQuality(self, value):
        super().setQuality(self, value)
        assert (
            0 <= self.quality <= 50
        ), f"{self.__class__.__name__}'s quality out of range"

    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSell_in()
