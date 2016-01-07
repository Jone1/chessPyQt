from PyQt4 import QtGui
import sys

__author__ = 'Jone'

from views.mainwindow import Main

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    m = Main()
    m.show()
    sys.exit(app.exec_())