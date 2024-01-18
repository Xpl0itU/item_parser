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
        return self.data.split(", ")

    def is_correct(self):
        return len(self.data.split(", ")) == COLUMN_COUNT and self.data.startswith(
            "name"
        )


class ItemInfoParser(BaseGRParserItem):
    def parse(self):
        return self.data.rsplit(", ", COLUMN_COUNT)

    def is_correct(self):
        return len(self.data.split(", ")) >= COLUMN_COUNT  # TODO: improve this check


class GRParser:
    def __init__(self, data):
        self.data = data

    def parse_string(self):
        parsed_raw_data = {}
        current_parser = DayHeaderParser
        current_day = None
        current_columns = None
        for line in str(self.data).splitlines():
            line_to_parse = current_parser(line)
            if current_parser == DayHeaderParser: # TODO: simplify this code and do the parsing in one pass
                current_day = line_to_parse.parse()
                current_parser = ColumnNamesParser
            elif current_parser == ColumnNamesParser:
                current_columns = line_to_parse.parse()
                current_parser = ItemInfoParser
            elif current_parser == ItemInfoParser and line_to_parse.is_correct():
                data_to_add = dict(zip(current_columns, line_to_parse.parse()))
                if current_day in parsed_raw_data:
                    parsed_raw_data[current_day].append(data_to_add)
                else:
                    parsed_raw_data[current_day] = [data_to_add]
            elif not line_to_parse.is_correct():
                current_parser = DayHeaderParser  # reset parsing, new day

        return dict(
            map(
                lambda x: (
                    x[0],
                    tuple(
                        map(
                            lambda y: Item(
                                name=y["name"],
                                sell_in=y["sellIn"],
                                quality=y["quality"],
                            ),
                            x[1],
                        )
                    ),
                ),
                parsed_raw_data.items(),
            )
        )


if __name__ == "__main__":
    from pprint import pprint

    with open("stdout_bug_conjured.gr", encoding="utf-8") as f:
        pprint(GRParser(f.read()).parse_string())
