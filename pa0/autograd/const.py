from .expr import Expression, ExpressionType

class Constant(Expression):
    def __init__(self: ExpressionType, val: float) -> None:
        self.val: float = val

    def differentiate(self: ExpressionType) -> "Constant":
        return Constant(0)

    def eval(self: ExpressionType, x: float) -> float:
        return self.val

    def deepcopy(self: ExpressionType) -> "Constant":
        return Constant(self.val)

    def __repr__(self: ExpressionType) -> str:
        return f"Constant({self.val})"

    def __str__(self: ExpressionType) -> str:
        return f"{self.val}"

