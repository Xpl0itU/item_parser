if __name__ == "__main__":
    from item_parser.GRParser import GRParser
    from pprint import pprint

    with open("stdout_bug_conjured.gr", encoding="utf-8") as f:
        pprint(GRParser(f.read()).parse_string())
