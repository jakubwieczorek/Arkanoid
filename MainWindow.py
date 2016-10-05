#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from engine import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self) # explicit calling of constructor in parent class

        self.initUI()

    def initUI(self):
        engine = Engine(self)
        self.setCentralWidget(engine)

    def moveCenter(self):
        size = self.geometry()
        screen = QtWidgets.QDesktopWidget().screenGeometry()

        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
