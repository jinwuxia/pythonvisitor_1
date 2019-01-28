
class Body:
    def accept(self, visitor):
        visitor.visitBody(self)
