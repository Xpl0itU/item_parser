from items import Item


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
    def parse(self):
        return "dayHeader"

    def is_correct(self):
        return self.data.startswith("-")


class ColumnNamesParser(BaseGRParserItem):
    def parse(self):
        return "columnNames"

    def is_correct(self):
        return len(self.data.split(", ")) == 3 and self.data.startswith("name")


class ItemInfoParser(BaseGRParserItem):
    def parse(self):
        return "itemInfo"

    def is_correct(self):
        return len(self.data.split(", ")) == 3


class GRParser:
    def __init__(self, data):
        self.data = data

    def parse_string(self):
        current_parser = DayHeaderParser
        for line in str(self.data).splitlines():
            parsed_line = current_parser(line)
            if current_parser == DayHeaderParser:
                current_parser = ColumnNamesParser
            elif current_parser == ColumnNamesParser:
                current_parser = ItemInfoParser
            elif not parsed_line.is_correct():
                current_parser = DayHeaderParser  # reset parsing, new day
            print(parsed_line.parse())


if __name__ == "__main__":
    with open("stdout_bug_conjured.gr", encoding="utf-8") as f:
        GRParser(f.read()).parse_string()
