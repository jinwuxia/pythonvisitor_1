
class Engine:
    def accept(self, visitor):
        visitor.visitEngine(self)
