from pieces.piece import AbstractPiece

__author__ = 'Jone'


class King(AbstractPiece):

    src_black = "D:/workspace/chessQt/chessQt/gfx/kb.png"
    src_white = "D:/workspace/chessQt/chessQt/gfx/kw.png"

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color)

    def moveValidator(self, x, y):
        if abs(self.x - x) > 1 or abs(self.y - y) > 1:
            return False
        return True