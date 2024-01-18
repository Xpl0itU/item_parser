if __name__ == "__main__":
    from item_parser.GRParser import GRParser
    import os.path
    from pprint import pprint

    with open(
        os.path.join("test", "data", "stdout_bug_conjured.gr"), encoding="utf-8"
    ) as f:
        pprint(GRParser(f.read()).parse_string())
