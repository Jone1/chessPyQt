from PyQt4 import QtGui
from PyQt4.QtCore import QString
from PyQt4.QtGui import QMessageBox
from pieces.bishop import Bishop
from pieces.blackpawn import BlackPawn
from pieces.king import King
from pieces.knight import Knight
from pieces.piece import chessboard
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.whitepawn import WhitePawn
from ui.mainwindow import Ui_MainWindow
from views.mylabel import MyLabel

__author__ = 'Jone'


labels = {}


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setFixedSize(648, 635)
        self.setWindowTitle("ChessQt")

        self.style = ["background: #333", "background: #fff"]

        self.ui.actionNowa_gra.triggered.connect(self.newGame)

        self.next_move = False

        for i in xrange(8):
            for j in xrange(8):
                m_label = MyLabel(i, j, self.style[(i + j) % 2])
                labels[(i, j)] = m_label
                self.ui.gridLayout_2.addWidget(m_label, i, j)
                m_label.clicked.connect(self.slotClicked)
        self.newGame()

    def createPiece(self):
        chessboard[(6, 0)] = BlackPawn(6, 0, True)
        chessboard[(6, 1)] = BlackPawn(6, 1, True)
        chessboard[(6, 2)] = BlackPawn(6, 2, True)
        chessboard[(6, 3)] = BlackPawn(6, 3, True)
        chessboard[(6, 4)] = BlackPawn(6, 4, True)
        chessboard[(6, 5)] = BlackPawn(6, 5, True)
        chessboard[(6, 6)] = BlackPawn(6, 6, True)
        # chessboard[(6, 7)] = BlackPawn(6, 7, True)

        chessboard[(7, 0)] = Rook(7, 0, True)
        chessboard[(7, 1)] = Knight(7, 1, True)
        chessboard[(7, 2)] = Bishop(7, 2, True)
        chessboard[(7, 3)] = King(7, 3, True)
        self.white_king = chessboard[(7, 3)]
        chessboard[(7, 4)] = Queen(7, 4, True)
        chessboard[(7, 5)] = Bishop(7, 5, True)
        chessboard[(7, 6)] = Knight(7, 6, True)
        chessboard[(7, 7)] = Rook(7, 7, True)

        chessboard[(0, 0)] = Rook(0, 0, False)
        chessboard[(0, 1)] = Knight(0, 1, False)
        chessboard[(0, 2)] = Bishop(0, 2, False)
        chessboard[(0, 3)] = King(0, 3, False)
        self.black_king = chessboard[(0, 3)]
        chessboard[(0, 4)] = Queen(0, 4, False)
        chessboard[(0, 5)] = Bishop(0, 5, False)
        chessboard[(0, 6)] = Knight(0, 6, False)
        chessboard[(0, 7)] = Rook(0, 7, False)

        # chessboard[(1, 0)] = WhitePawn(1, 0, False)
        chessboard[(1, 1)] = WhitePawn(1, 1, False)
        chessboard[(1, 2)] = WhitePawn(1, 2, False)
        chessboard[(1, 3)] = WhitePawn(1, 3, False)
        chessboard[(1, 4)] = WhitePawn(1, 4, False)
        chessboard[(1, 5)] = WhitePawn(1, 5, False)
        chessboard[(1, 6)] = WhitePawn(1, 6, False)
        chessboard[(1, 7)] = WhitePawn(1, 7, False)

    def refreshPiece(self):
        for i in xrange(8):
            for j in xrange(8):
                if chessboard.has_key((i, j)):
                    piece = chessboard.get((i, j))
                    if piece.alive:
                        if piece.color:
                            labels.get((i, j)).setImagePiece(piece.src_black)
                        else:
                            labels.get((i, j)).setImagePiece(piece.src_white)
                else:
                    labels.get((i, j)).setImagePiece("")

    def deselectAll(self):
        for i in xrange(8):
            for j in xrange(8):
                labels.get((i, j)).setStyleSheet(self.style[(i + j) % 2])

    def movePiece(self, x, y):
        chessboard.get((self.active_x, self.active_y)).move(x, y)
        chessboard[(x, y)] = chessboard.get((self.active_x, self.active_y))
        del chessboard[(self.active_x, self.active_y)]
        self.deselectAll()
        self.refreshPiece()
        self.next_move = not self.next_move
    
        if not self.black_king.alive:
            dialog = QtGui.QDialog()
        elif not self.white_king.alive:
            QMessageBox.about(self, "Black wins.", "")

    def removePiece(self):
        for i in xrange(8):
            for j in xrange(8):
                if chessboard.has_key((i, j)):
                    del chessboard[(i, j)]

    def newGame(self):
        self.removePiece()
        self.createPiece()
        self.refreshPiece()

    def slotNewGame(self):
        self.newGame()

    def slotClicked(self, x, y):
        if chessboard.has_key((x, y)) and labels.get((x, y)).styleSheet() == "background: #00f":
            chessboard.get((x, y)).makeNotAlive()
            self.movePiece(x, y)
        elif chessboard.has_key((x, y)):
            if chessboard.get((x, y)).color == self.next_move:
                for i in xrange(8):
                    for j in xrange(8):
                        labels[(i, j)].setStyleSheet(self.style[(i+j) % 2])
                        if chessboard.get((x, y)).moveValidator(i, j) and not chessboard.get((x, y)).isSelfHere(i, j):
                            labels.get((i, j)).setStyleSheet("background: #00f")
                        else:
                            labels.get((x, y)).setStyleSheet(self.style[(i+j) % 2])
                            labels.get((x, y)).setStyleSheet("background: #f00")
                            self.active_x = x
                            self.active_y = y
        elif labels.get((x, y)).styleSheet() == "background: #00f":
            self.movePiece(x, y)