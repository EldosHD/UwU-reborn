from typing import Any
from lark import Token, Transformer
import nodes as uwu_nodes
import rich

class AstTransformer(Transformer):
    def LITERAL(self, item:Token) -> uwu_nodes.LiteralExprNode:
        print('literal')
        return uwu_nodes.LiteralExprNode(item.line, item.column, int(item.value))

    def expr(self, items:list[Any]) -> uwu_nodes.ExprNode:
        return items[0]

    def return_stmt(self, items: list[Any]) -> uwu_nodes.ReturnStmtNode:
        expr = items[1]
        return uwu_nodes.ReturnStmtNode(expr.line, expr.column, expr)

    def block(self, items:list[Any]) -> uwu_nodes.BlockNode:
        rich.print('Items: ' + str(items))
        statements = items[1:-1]
        return uwu_nodes.BlockNode(items[0].line, items[0].column, statements)

    def func_def(self, items:list[Any]) -> uwu_nodes.FuncDefNode:
        type = items[0].value
        identifier = items[1].value
        body = items[2]
        return uwu_nodes.FuncDefNode(items[0].line, items[0].column, type, identifier, body)

    def program(self, items:list[Any]) -> uwu_nodes.ProgramNode:
        return uwu_nodes.ProgramNode(0,0,items)
