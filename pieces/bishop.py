from pieces.piece import AbstractPiece

__author__ = 'Jone'


class Bishop(AbstractPiece):

    src_white = "D:/workspace/chessQt/chessQt/gfx/bw.png"
    src_black = "D:/workspace/chessQt/chessQt/gfx/bb.png"

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color)

    def moveValidator(self, x, y):
        if abs(x - self.x) != abs(y - self.y):
            return False
        return self.isEmptyTo(x, y)
