from .expr import Expression, ExpressionType
from .const import Constant

class Variable(Expression):
    def __init__(self: ExpressionType, x: str = "x") -> None:
        self.x: str = x

    def differentiate(self: ExpressionType) -> Constant:
        return Constant(1)

    def eval(self: ExpressionType, x: float) -> float:
        return x

    def __repr__(self: ExpressionType) -> str:
        return f"Variable({self.x})"

    def __str__(self: ExpressionType) -> str:
        return "x"

    def deepcopy(self: ExpressionType) -> "Variable":
        return Variable(self.x)
    