#!/usr/bin/env python3
from pathlib import Path
import rich
from lark.tree import pydot__tree_to_png
import argparse

from ast_builder import AstTransformer
from parser import Parser


def run(input_file: Path):
    print('Compiling', input_file)
    parser = Parser()
    with input_file.open('rt') as f:
        tree = parser.parse_text(f.read())
    rich.print(tree)

    pydot__tree_to_png(tree, str(input_file.with_suffix('.png')), rankdir='TB')


    transformed = AstTransformer().transform(tree)
    rich.print(transformed)

def main(input_file: Path):
    run(input_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=Path, help='The input file to compile')

    args = parser.parse_args()

    main(args.input_file)
