
class Wheel:
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        visitor.visitWheel(self)
