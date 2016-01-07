__author__ = 'Jone'

chessboard = {}


class AbstractPiece(object):

    src_white = ''
    src_black = ''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.alive = True

    def moveValidator(self, x, y):
        pass

    def makeNotAlive(self):
        self.alive = False

    def isOpponentHere(self, x, y):
        if chessboard.has_key((x, y)):
            if chessboard.get((x, y)).color != self.color:
                return True
        return False

    def isSelfHere(self, x, y):
        if chessboard.has_key((x, y)):
            if chessboard.get((x, y)).color == self.color:
                return True
        return False

    def isEmpty(self, x, y):
        if chessboard.has_key((x, y)):
            return False
        return True

    def isEmptyTo(self, x, y):
        if self.x == x or self.y == y:
            for i in xrange(self.x + 1, x):
                if not self.isEmpty(i, y):
                    return False
            for i in xrange(self.y + 1, y):
                if not self.isEmpty(x, i):
                    return False
            for i in xrange(self.y - 1, y, -1):
                if not self.isEmpty(x, i):
                    return False
            for i in xrange(self.x - 1, x, -1):
                if not self.isEmpty(i, y):
                    return False
        elif x - self.x > 0 and y - self.y > 0:
            for i in xrange(1, x - self.x):
                if not self.isEmpty(self.x + i, self.y + i):
                    return False
        elif self.x - x > 0 and self.y - y > 0:
            for i in xrange(1, self.x - x):
                if not self.isEmpty(self.x - i, self.y - i):
                    return False
        elif self.y - y > 0 and x - self.x > 0:
            for i in xrange(1, self.y - y):
                if not self.isEmpty(self.x + i, self.y - i):
                    return False
        elif y - self.y > 0 and self.x - x > 0:
            for i in xrange(1, y - self.y):
                if not self.isEmpty(self.x - i, self.y + i):
                    return False
        return True


    def move(self, x, y):
        self.x = x
        self.y = y
