from .expr import Expression, ExpressionType
from .binop import BinaryOp, Op
from .const import Constant
from math import cos


class Cos(Expression):
    def __init__(self: ExpressionType, arg: Expression) -> None:
        self.arg: Expression = arg

    def differentiate(self: ExpressionType) -> ExpressionType:
        from .sin import Sin
        return BinaryOp(
                    BinaryOp(
                        Constant(-1),
                        Op(2),
                        self.arg.differentiate()
                    ),
                    Op(3), 
                    Sin(self.arg)
                )

    def eval(self: ExpressionType, x: float) -> float:
        return cos(self.arg.eval(x))

    def deepcopy(self: ExpressionType) -> "Cos":
        return Cos(self.arg)

    def __repr__(self: ExpressionType) -> str:
        return f"Cos{self.arg}"

    def __str__(self: ExpressionType) -> str:
        return f"Cos{self.arg}"