# !usr/bin/env python2.7
# -*- coding: utf-8 -*-

from gameview import *

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        horizontalLayout = QtWidgets.QVBoxLayout(self)
        self.setLayout(horizontalLayout)

        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setMinimumSize(QtCore.QSize(610, 20))
        self.statusBar.setMaximumSize(QtCore.QSize(610, 20))

        self.statusBar.showMessage("Let's play !!!")

        gameView = GameView(self)
        gameView.setMaximumSize(QtCore.QSize(610, 310))
        gameView.setMinimumSize(QtCore.QSize(610, 310))

        horizontalLayout.addWidget(gameView, 1)
        horizontalLayout.addWidget(self.statusBar, 2)


