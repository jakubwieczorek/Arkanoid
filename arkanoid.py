# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from plib.mainwindow import *

if __name__ == "__main__": # if this module is ran directly
    app = QtWidgets.QApplication(sys.argv)

    view = MainWindow()

    view.resize(680,400)
    view.setMaximumSize(QtCore.QSize(680, 400))
    view.setMinimumSize(QtCore.QSize(680, 400))

    view.show()

    sys.exit(app.exec_())
