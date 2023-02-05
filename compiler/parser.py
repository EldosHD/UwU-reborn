#!/usr/bin/python3
from lark import Lark

with open('uwu.lark', 'r') as file:
    data = file.read()

with open('test.uwu', 'r') as file:
    code = file.read()

print("\n----------CODE----------\n" + code + "\n------------------------\n")

tree = Lark(data, debug=True).parse(code)
print(tree.pretty())