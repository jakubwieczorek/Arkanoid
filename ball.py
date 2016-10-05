# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui

class Ball(QtWidgets.QWidget):
    def __init__(self, parent, x1 = None, y1 = None, r = None):
        QtWidgets.QWidget.__init__(self)
        if x1 == None and y1 == None and r == None:
            self.x1 = parent.geometry().width() / 2
            self.y1 = parent.geometry().height() / 2
            self.r = 20

        elif x1 != None and y1 !=None and r != None:
            self.setCoordinates(x1, y1)
            self.setRay(r)

    def paintWidget(self, painter):
        pen = QtGui.QPen(QtCore.Qt.green, 5)
        pen.setJoinStyle(QtCore.Qt.MiterJoin)

        brush = QtGui.QBrush(QtCore.Qt.yellow)
        brush.setStyle(QtCore.Qt.SolidPattern)

        painter.setPen(pen)
        painter.setBrush(brush)

        painter.drawEllipse(QtCore.QPointF(self.x1, self.y1), self.r, self.r)

    def setCoordinates(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def setRay(self, r):
        self.r = r
