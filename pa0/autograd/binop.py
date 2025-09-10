from enum import Enum
from typing import Type
from .expr import Expression, ExpressionType

OpType = Type["Op"]

class Op(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4

    def __str__(self: OpType) -> str:
        op_str: str = None
        if self == Op.ADD:
            op_str = "+"
        elif self == Op.SUB:
            op_str = "-"
        elif self == Op.MUL:
            op_str = "*"
        elif self == Op.DIV:
            op_str = "/"
        else:
            raise ValueError("ERROR: unknown op [{0}]".format(self))
        return op_str

    def __repr__(self: OpType) -> str: 
        return self.__str__()


class BinaryOp(Expression):

    def __init__(self: OpType, lhs: Expression, op: Op, rhs: Expression) -> None:
        self.lhs: Expression = lhs
        self.op: Op = op
        self.rhs: Expression = rhs

    def differentiate(self: ExpressionType) -> "BinaryOp":
        from .pow import Power

        if (self.op.__str__() == "+"):
            val: "BinaryOp" = BinaryOp(self.lhs.differentiate(), Op(1), self.rhs.differentiate())        

        elif (self.op.__str__() == "-"):
            val: "BinaryOp" = BinaryOp(self.lhs.differentiate(), Op(2), self.rhs.differentiate())        

        elif (self.op.__str__() == "*"):
            val: "BinaryOp" = BinaryOp(
                BinaryOp(self.lhs.differentiate(), Op(3), self.rhs), 
                Op(1),
                BinaryOp(self.lhs, Op(3), self.rhs.differentiate()))
            
        elif (self.op.__str__() == "/" and self.rhs != 0):
            val = BinaryOp(
                    BinaryOp(
                        BinaryOp(
                            self.rhs, 
                            Op(3), 
                            self.lhs.differentiate()
                        ), 
                        Op(2),
                        BinaryOp(
                            self.lhs, 
                            Op(3), 
                            self.rhs.differentiate()
                        )
                    ),
                    Op(4),
                    Power(self.rhs, 2)
            )        
             
        else:
            raise ValueError("ERROR: something went wrong lil bro.{}".format(self))
        return val

    def eval(self: ExpressionType, x: float) -> float:
        val: float = None
        if (self.op.__str__() == "+"):
            val = self.lhs.eval(x) + self.rhs.eval(x)

        elif (self.op.__str__() == "-"):
            val = self.lhs.eval(x) - self.rhs.eval(x)

        elif (self.op.__str__() == "*"):
            val = self.lhs.eval(x) * self.rhs.eval(x)

        elif (self.op.__str__() == "/" and self.rhs.eval(x) != 0):
            val = self.lhs.eval(x) / self.rhs.eval(x)

        else:
            raise ValueError("ERROR: unknown op [{0}]".format(self)) 
            
        return val


    def __repr__(self: ExpressionType) -> str:
        return f"BinaryOp({self.lhs}, {self.op}, {self.rhs})"
    
    def __str__(self: ExpressionType) -> str:
        expr_wrapper = lambda x: f"({x})" if (isinstance(x, BinaryOp)) else x
        op_wrapper = lambda x: f" {x} " if (isinstance(x, Op) and x.__str__() == "-") else x

        return (f"{expr_wrapper(self.lhs)}{op_wrapper(self.op.__str__())}{expr_wrapper(self.rhs)}")
 
    def deepcopy(self: ExpressionType) -> "BinaryOp":
        return BinaryOp(self.lhs, self.op, self.rhs)