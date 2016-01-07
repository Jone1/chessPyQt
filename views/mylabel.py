from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSignal
from PyQt4.QtGui import QLabel, QPixmap

__author__ = 'Jone'


class MyLabel(QLabel):

    clicked = pyqtSignal(int, int)

    def __init__(self, x, y, style, *__args):
        QLabel.__init__(self, *__args)

        self.setMinimumHeight(70)
        self.setMaximumHeight(70)
        self.setStyleSheet(style)

        self.x = x
        self.y = y

    def setImagePiece(self, src):
        mypix = QPixmap(src)
        self.setPixmap(mypix)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit(self.x, self.y)
