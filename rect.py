# !usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore

class Rect(QtWidgets.QWidget):

    def __init__(self, parent, x1 = None, y1 = None
                 , x2 = None, y2 = None):
        """first argument is parent of the object (when object is declared, next four arguments is coordinates"""
        QtWidgets.QWidget.__init__(self)
        if x1 == None and x2 == None and y1 == None and y2 == None:
            self.setCoordinates(parent.geometry().width() - 20, parent.geometry().width() + 40,
                                parent.geometry().height() - 10, parent.geometry().height())
        elif x1 != None and x2 != None and y1 != None and y2 != None:
            self.setCoordinates(x1, y1, x2, y2)

    def paintWidget(self, painter):
        pen = QtGui.QPen(QtCore.Qt.red, 5)
        painter.setPen(pen)

        rect = QtCore.QRectF(QtCore.QPointF(self.x1, self.y1), QtCore.QPointF(self.x2, self.y2))
        painter.drawRect(rect)

        brush = QtGui.QBrush(QtCore.Qt.black)
        painter.fillRect(rect, brush)

    def setCoordinates(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2



