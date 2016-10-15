# !usr/bin/env/ python2.7

from PyQt5 import QtCore, QtGui, QtWidgets

class BackgroundItem(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, parent):
        QtWidgets.QGraphicsPixmapItem.__init__(self)
        pixmap = QtGui.QPixmap("../Game/backgroundlvl1.jpeg")

        self.setPixmap(pixmap.scaled(parent.sceneRect.width(), parent.sceneRect.height()))
        self.setZValue(-1)