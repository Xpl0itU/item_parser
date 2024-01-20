import re
from item_parser.items import Item
from item_parser.Hooks import (
    NormalItemHook,
    ConjuredItemHook,
    AgedBrieHook,
    SulfurasHook,
    BackstageHook,
)

COLUMN_COUNT = 3
SORTED_HOOKS = sorted(
    (NormalItemHook, ConjuredItemHook, AgedBrieHook, SulfurasHook, BackstageHook),
    key=lambda x: x.get_priority(),
    reverse=True,
)


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
            return int(self.match.group(1))
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
        return self.data.rsplit(", ", COLUMN_COUNT - 1)

    def is_correct(self):
        return len(self.data.split(", ")) >= COLUMN_COUNT  # TODO: improve this check


class GRParser:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def __create_item_from_raw_data(data):
        for hook in SORTED_HOOKS:
            hook_instance = hook(data)
            if hook_instance.can_hook():
                return hook_instance.hook()
        return Item(**data)

    def parse_string(self):
        parsed_data = {}
        current_parser = DayHeaderParser
        current_day = None
        current_columns = None

        parser_mapping = {
            DayHeaderParser: ColumnNamesParser,
            ColumnNamesParser: ItemInfoParser,
            ItemInfoParser: ItemInfoParser,
        }

        for line in str(self.data).splitlines():
            line_to_parse = current_parser(line)
            if current_parser == DayHeaderParser:
                current_day = line_to_parse.parse()
            elif current_parser == ColumnNamesParser:
                current_columns = line_to_parse.parse()
            elif current_parser == ItemInfoParser and line_to_parse.is_correct():
                raw_data = dict(zip(current_columns, line_to_parse.parse()))
                if raw_data:
                    parsed_data.setdefault(current_day, []).append(
                        self.__create_item_from_raw_data(raw_data)
                    )
            current_parser = (
                parser_mapping[current_parser]
                if line_to_parse.is_correct()
                else DayHeaderParser
            )  # shift parser when done, reset parsing when new day starts

        return parsed_data
