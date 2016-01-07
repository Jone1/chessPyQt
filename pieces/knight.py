from pieces.piece import AbstractPiece

__author__ = 'Jone'


class Knight(AbstractPiece):

    src_white = "D:/workspace/chessQt/chessQt/gfx/nw.png"
    src_black = "D:/workspace/chessQt/chessQt/gfx/nb.png"

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color)

    def moveValidator(self, x, y):
        if abs(self.x - x) == 2 and abs(self.y - y) == 1:
            return True
        elif abs(self.x - x) == 1 and abs(self.y - y) == 2:
            return True
        return False