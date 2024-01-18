class Item:
    def __init__(self, name, sell_in, quality):
        self._name = name
        self._sell_in = sell_in
        self._quality = quality

    @property
    def name(self):
        return self._name

    @property
    def sell_in(self):
        return self._sell_in

    @property
    def quality(self):
        return self._quality

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.sell_in == other.sell_in
            and self.quality == other.quality
        )

    def __repr__(self):
        return f"Item(name={self.name}, sell_in={self.sell_in}, quality={self.quality})"
