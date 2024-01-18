import re
from items import Item

COLUMN_COUNT = 3


class BaseGRParserItem:
    def __init__(self, data):
        self.data = data

    def parse(self):
        pass

    def is_correct(self):
        pass

    def __repr__(self):
        return f"BaseGRParserItem: {self.data}"


class DayHeaderParser(BaseGRParserItem):
    def __init__(self, data):
        super().__init__(data)
        self.pattern = r"-------- day (-?\d+) --------"
        self.match = None

    def parse(self):
        self.match = re.search(self.pattern, self.data)
        if self.match:
            return self.match.group(1)
        return None

    def is_correct(self):
        return bool(self.match)


class ColumnNamesParser(BaseGRParserItem):
    def parse(self):
        return "columnNames"

    def is_correct(self):
        return len(self.data.split(", ")) == COLUMN_COUNT and self.data.startswith(
            "name"
        )


class ItemInfoParser(BaseGRParserItem):
    def parse(self):
        return "itemInfo"

    def is_correct(self):
        return len(self.data.split(", ")) >= COLUMN_COUNT  # TODO: improve this check


class GRParser:
    def __init__(self, data):
        self.data = data

    def parse_string(self):
        current_parser = DayHeaderParser
        for line in str(self.data).splitlines():
            line_to_parse = current_parser(line)
            if current_parser == DayHeaderParser:
                current_parser = ColumnNamesParser
            elif current_parser == ColumnNamesParser:
                current_parser = ItemInfoParser
            elif not line_to_parse.is_correct():
                current_parser = DayHeaderParser  # reset parsing, new day
            # print(line_to_parse)
            print(line_to_parse.parse())


if __name__ == "__main__":
    with open("stdout_bug_conjured.gr", encoding="utf-8") as f:
        GRParser(f.read()).parse_string()
