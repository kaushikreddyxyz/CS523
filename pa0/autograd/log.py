from .expr import Expression, ExpressionType
from .binop import BinaryOp, Op
from math import log


class Log(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
        self.arg: Expression = arg

    def differentiate(self: ExpressionType) -> ExpressionType:
        return BinaryOp(self.arg.differentiate(), Op(4), self.arg)

    def eval(self: ExpressionType, x: float) -> float:
        return log(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> "Log":
        return Log(self.arg)

    def __repr__(self: ExpressionType) -> str:
        return f"Log({self.arg})"

    def __str__(self: ExpressionType) -> str:
        return f"log({self.arg})"