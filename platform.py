# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from rect import *

class Platform(Rect):
    def __init__(self, parent, x1 = None, y1 = None
                 , x2 = None, y2 = None):
        Rect.__init__(self, parent, x1, y1, x2, y2)

    def paintWidget(self, painter):
        pen = QtGui.QPen(QtCore.Qt.black, 5)
        pen.setJoinStyle(QtCore.Qt.MiterJoin)

        painter.setPen(pen)

        rect = QtCore.QRectF(QtCore.QPointF(self.x1, self.y1), QtCore.QPointF(self.x2, self.y2))
        painter.drawRect(rect)

        brush = QtGui.QBrush(QtCore.Qt.black)
        painter.fillRect(rect, brush)