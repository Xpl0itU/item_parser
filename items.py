class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @property
    def name(self):
        return self.__name

    @property
    def sell_in(self):
        return self.__sell_in

    @property
    def quality(self):
        return self.__quality

    @name.setter
    def name(self, value):
        self.__name = value

    @sell_in.setter
    def sell_in(self, value):
        self.__sell_in = value

    @quality.setter
    def quality(self, value):
        self.__quality = value

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.sell_in == other.sell_in
            and self.quality == other.quality
        )

    def __repr__(self):
        return f"Item(name={self.name}, sell_in={self.sell_in}, quality={self.quality})"
