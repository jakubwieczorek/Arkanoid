#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from MainWindow import *

if __name__ == "__main__": # this module is ran directly
    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()

    w.resize(600, 300)
    w.moveCenter()
    w.setWindowTitle("Game")
    w.show()

    sys.exit(app.exec_())