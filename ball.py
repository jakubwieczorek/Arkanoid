# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from rect import *

class Ball(QtWidgets.QGraphicsPixmapItem):
    width = 50

    def __init__(self, parent, x1 = None, y1 = None):
        QtWidgets.QWidget.__init__(self)
        if x1 == None and y1 == None:
            self.setPos(parent.geometry().width() / 2, parent.geometry().height() / 2)

        elif x1 != None and y1 !=None:
            self.setPos(x1, y1)

        pixmap = QtGui.QPixmap("../Game/ball.png")
        self.setPixmap(pixmap.scaled(Ball.width, Ball.width, QtCore.Qt.KeepAspectRatio))

        self.parent = parent

        self.r = Ball.width / 2

    def collidingEvent(self):
        collidingItems = self.collidingItems() # list with all items

        for i in xrange(0, len(self.collidingItems())):
            if isinstance(collidingItems[i], Rect):

                self.scene().removeItem(collidingItems[i])
                self.parent.box.remove(collidingItems[i])
"""
    def paint(self, painter, option, widget = None):
        pen = QtGui.QPen(QtCore.Qt.red, 5)
        painter.drawRect(self.boundingRect())

    def boundingRect(self):
        return QtCore.QRectF(self.x(), self.y(), self.x() + Rect.width, self.y() + Rect.width)
"""