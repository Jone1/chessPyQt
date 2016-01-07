from pieces.piece import AbstractPiece

__author__ = 'Jone'


class Queen(AbstractPiece):

    src_white = "D:/workspace/chessQt/chessQt/gfx/qw.png"
    src_black = "D:/workspace/chessQt/chessQt/gfx/qb.png"

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color)

    def moveValidator(self, x, y):
        return self.isEmptyTo(x, y)
