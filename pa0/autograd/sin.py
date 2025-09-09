from .expr import Expression, ExpressionType
from .binop import BinaryOp, Op
from math import sin


class Sin(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
        self.arg: Expression = arg

    def differentiate(self: ExpressionType) -> ExpressionType:
        from .cos import Cos
        return BinaryOp(self.arg.differentiate(), Op(3), Cos(self.arg))

    def eval(self: ExpressionType, x: float) -> float:
        return sin(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> "Sin":
        return Sin(self.arg)

    def __repr__(self: ExpressionType) -> str:
        return f"Sin{self.arg}"

    def __str__(self: ExpressionType) -> str:
        return f"Sin{self.arg}"