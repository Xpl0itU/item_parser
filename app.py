if __name__ == "__main__":
    from item_parser.GRParser import GRParser
    from pprint import pprint

    with open("stdout_bug_conjured.gr", encoding="utf-8") as f:
        parsed_data = GRParser(f.read()).parse_string()
        pprint(parsed_data)
        parsed_data[0].pop(0)
        GRParser(parsed_data).export_to_file("stdout_bug_conjured_updated.gr")
