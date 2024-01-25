from dataclasses import dataclass
from typing import Any, Dict, Iterable


@dataclass
class ParsedGRDataFormatter:
    parsed_data: Dict[int, Iterable[Dict[str, Any]]]

    def __format_day(self, day: int, items: Iterable[Dict[str, Any]]) -> str:
        day_header = f"-------- day {day} --------"
        column_names = ", ".join(items[0].keys())
        items_data = "\n".join([", ".join(map(str, item.values())) for item in items])
        return f"{day_header}\n{column_names}\n{items_data}\n"

    def __str__(self) -> str:
        return "\n".join(
            (self.__format_day(day, items) for day, items in self.parsed_data.items())
        )

    def export_to_file(self, file_name: str) -> None:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(str(self))
