from pieces.piece import AbstractPiece

__author__ = 'Jone'

class Rook(AbstractPiece):
    # 30 min

    src_black = "D:/workspace/chessQt/chessQt/gfx/rb.png"
    src_white = "D:/workspace/chessQt/chessQt/gfx/rw.png"

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color)

    def moveValidator(self, x, y):
        if y != self.y and x != self.x:
            return False
        return self.isEmptyTo(x, y)