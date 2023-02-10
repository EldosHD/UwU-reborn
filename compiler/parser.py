#!/usr/bin/python3
from pathlib import Path

import lark
import rich


class Parser:
    def __init__(self, grammar_path: Path = Path("UwU-reborn.lark"), start: str = "program") -> None:
        with grammar_path.open("rt") as f:
            grammar_text = f.read()

        self.lark = lark.Lark(grammar_text, start=start, ambiguity="explicit")

    def parse_text(self, program_text: str) -> lark.ParseTree:
        parsed = self.lark.parse(program_text)

        return parsed

if __name__ == "__main__":
    parser = Parser()
    with Path('test.uwu').open('rt') as f:
        tree = parser.parse_text(f.read())

    rich.print(tree)
