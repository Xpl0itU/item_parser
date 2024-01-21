from dataclasses import dataclass, asdict
import re
from item_parser.Items import Item
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
        self.match = re.fullmatch(self.pattern, self.data)
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
        split_data = self.data.split(", ")
        return len(split_data) >= COLUMN_COUNT and all(
            lambda x: x != "" for x in split_data
        )


class GRParser:
    @dataclass
    class InternalGRParserState:
        current_parser: type(BaseGRParserItem)
        current_day: int
        current_columns: list
        parsed_data: dict

        parser_mapping = {
            DayHeaderParser: ColumnNamesParser,
            ColumnNamesParser: ItemInfoParser,
            ItemInfoParser: ItemInfoParser,
        }

        def update_state(self, line_to_parse, create_item_func):
            parser_actions = {
                DayHeaderParser: lambda: self.update_day(line_to_parse),
                ColumnNamesParser: lambda: self.update_columns(line_to_parse),
                ItemInfoParser: lambda: self.update_item(
                    line_to_parse, create_item_func
                ),
            }
            parser_actions.get(self.current_parser, lambda: None)()

        def update_day(self, line_to_parse):
            self.current_day = line_to_parse.parse()

        def update_columns(self, line_to_parse):
            self.current_columns = line_to_parse.parse()

        def update_item(self, line_to_parse, create_item_func):
            if line_to_parse.is_correct():
                raw_data = dict(zip(self.current_columns, line_to_parse.parse()))
                if raw_data:
                    self.parsed_data.setdefault(self.current_day, []).append(
                        create_item_func(raw_data)
                    )

        def update_parser(self, line_to_parse):
            self.current_parser = (
                self.parser_mapping[self.current_parser]
                if line_to_parse.is_correct()
                else DayHeaderParser
            )

    def __init__(self, data):
        self.data = data

    @staticmethod
    def __create_item_from_raw_data(data):
        for hook in SORTED_HOOKS:
            hook_instance = hook(data)
            if hook_instance.can_hook():
                return hook_instance.hook()
        return Item(
            name=data["name"],
            sellIn=int(data["sellIn"]),
            quality=int(data["quality"]),
        )  # we should never get here

    def parse_string(self):
        internal_state = self.InternalGRParserState(
            current_parser=DayHeaderParser,
            current_day=0,
            current_columns=[],
            parsed_data={},
        )

        for line in self.data.splitlines():
            line_to_parse = internal_state.current_parser(line)
            internal_state.update_state(line_to_parse, self.__create_item_from_raw_data)
            internal_state.update_parser(line_to_parse)

        return internal_state.parsed_data

    @staticmethod
    def __parsed_data_to_string(parsed_data):
        output = ""
        for day, items in parsed_data.items():
            output += f"-------- day {day} --------\n"
            column_names = ", ".join(asdict(items[0]).keys())
            output += f"{column_names}\n"

            for item_data in items:
                output += ", ".join(map(str, asdict(item_data).values())) + "\n"
            output += "\n"
        return output

    def export_to_file(self, file_name):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(self.__parsed_data_to_string(self.data) + "\n")
