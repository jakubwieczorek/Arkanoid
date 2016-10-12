#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from gamewindow import *

if __name__ == "__main__": # if this module is ran directly
    app = QtWidgets.QApplication(sys.argv)

    view = GameView()

    view.resize(600,300)

    view.show()

    sys.exit(app.exec_())