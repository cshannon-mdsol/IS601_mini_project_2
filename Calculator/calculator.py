from Calculator.Addition import Addition
from Calculator.Subtraction import Subtraction
from Calculator.Multiplication import Multiplication
from Calculator.Division import Division
from Calculator.Square import Square
from Calculator.SquareRoot import SquareRoot


class Calculator:
    result = 0

    def __init__(self):
        pass

    def Add(self, a, b):
        self.result = Addition(a, b)
        return self.result

    def Subtract(self, a, b):
        self.result = Subtraction(a, b)
        return self.result

    def Multiply(self, a, b):
        self.result = Multiplication(a, b)
        return self.result

    def Divide(self, a, b):
        self.result = Division(a, b)
        return self.result

    def Square(self, a):
        self.result = Square(a)
        return self.result

    def SqRoot(self, a):
        self.result = SquareRoot(a)
        return self.result
