from pieces.piece import AbstractPiece

__author__ = 'Jone'


class Pawn(AbstractPiece):

    src_white = "D:/workspace/chessQt/chessQt/gfx/pw.png"
    src_black = "D:/workspace/chessQt/chessQt/gfx/pb.png"

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color)

