# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from rect import *

class Platform(Rect):
    width = 100
    height = width * 157 / 654

    def __init__(self, parent, x, y):
        QtWidgets.QGraphicsPixmapItem.__init__(self)

        pixmap = QtGui.QPixmap("../Game/platform.png")
        self.setPixmap(pixmap.scaled(Platform.width, Platform.height, QtCore.Qt.KeepAspectRatio))
        self.setPos(x, y)

    def getWidth():
        return Platform.width
    getWidth = staticmethod(getWidth)

    def getHeight():
        return Platform.height
    getHeight = staticmethod(getHeight)