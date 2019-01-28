from Wheel import Wheel
from Body import Body
from Engine import Engine

class Car:
    def __init__(self):
        self.elements = [
            Wheel("front left"), Wheel("front right"),
            Wheel("back left"), Wheel("back right"),
            Body(), Engine()
        ]

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

        visitor.visitCar(self)
