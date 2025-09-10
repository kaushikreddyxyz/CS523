from .expr import Expression, ExpressionType
from .binop import BinaryOp, Op
from .const import Constant

class Power(Expression):
    def __init__(self: ExpressionType, base: Expression, exp: float) -> None:
        self.base: Expression = base
        self.exp: float = float(exp)

    def __repr__(self: ExpressionType) -> str:
        return f"Power({self.base}, {self.exp})"
    
    def __str__(self: ExpressionType) -> str:
        return f"({self.base}^{self.exp})"

    def eval(self: ExpressionType, x: float) -> float:
        return self.base.eval(x) ** self.exp

    def differentiate(self: ExpressionType) -> ExpressionType:
        return BinaryOp(
                    BinaryOp(
                        Constant(self.exp), 
                        Op(3), 
                        Power(self.base, self.exp - 1)
                    ), 
                    Op(3), 
                    self.base.differentiate()
                )


    def deepcopy(self: ExpressionType) -> "Power":
        return Power(self.base, self.exp)
