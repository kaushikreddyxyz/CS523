from .expr import Expression, ExpressionType
from .binop import BinaryOp, Op
from math import exp


class Exp(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
        self.arg: Expression = arg

    def differentiate(self: ExpressionType) -> ExpressionType:
        return BinaryOp(self.arg.differentiate(), Op(3), Exp(self.arg))

    def eval(self: ExpressionType, x: float) -> float:
        return exp(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> "Exp":
        return Exp(self.arg)

    def __repr__(self: ExpressionType) -> str:
        return f"Exp({self.arg})"

    def __str__(self: ExpressionType) -> str:
        return f"exp({self.arg})"