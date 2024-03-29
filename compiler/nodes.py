import abc
import rich

class Node(abc.ABC):
    """Used for giving exact positions for error messages"""
    def __init__(self, line:int, column:int) -> None:
        self.line = line
        self.column = column


class ExprNode(Node):
    def __init__(self, line: int, column: int) -> None:
        super().__init__(line, column)
        
class StmtNode(Node):
    def __init__(self, line: int, column: int) -> None:
        super().__init__(line, column)

# for now only int is allowed for literals TODO: change later
class LiteralExprNode(ExprNode):
    def __init__(self, line: int, column: int, value:int) -> None:
        super().__init__(line, column)
        self.value = value


class ReturnStmtNode(StmtNode):
    def __init__(self, line: int, column: int, expr:ExprNode) -> None:
        super().__init__(line, column)
        assert isinstance(expr, ExprNode)
        self.expr = expr


# takes a list of statements
class BlockNode(Node):
    """A list of statements"""
    def __init__(self, line: int, column: int, stmts:list[StmtNode]) -> None:
        super().__init__(line, column)
        rich.print(stmts)
        assert all([isinstance(n, StmtNode) for n in stmts])
        self.stmts = stmts


class FuncDefNode(Node):
    """Has a return type, identifier and body (block)"""
    def __init__(self, line: int, column: int, type:str, identifier:str, body:BlockNode) -> None:
        super().__init__(line, column)
        self.type = type
        self.identifier = identifier
        assert isinstance(body, BlockNode)
        self.body = body


class ProgramNode(Node):
    """A list of functions"""
    def __init__(self, line: int, column: int, func_defs: list[FuncDefNode]) -> None:
        super().__init__(line, column)
        assert all([isinstance(n, FuncDefNode) for n in func_defs])
        self.func_defs = func_defs

