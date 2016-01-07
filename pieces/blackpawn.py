from pieces.pawn import Pawn

__author__ = 'Jone'


class BlackPawn(Pawn):
    def __init__(self, x, y, color):
        super(BlackPawn, self).__init__(x, y, color)

    def moveValidator(self, x, y):
        if self.x - 1 == x and self.y - 1 == y:
            return self.isOpponentHere(self.x - 1, self.y - 1)
        elif self.x - 1 == x and self.y + 1 == y:
            return self.isOpponentHere(self.x - 1, self.y - 1)

        if y == self.y:
            if 6 == self.x and 3 > self.x - x > 0:  # First move
                return self.isEmpty(x, y)
            if 2 > self.x - x > 0:
                return self.isEmpty(x, y)
        return False