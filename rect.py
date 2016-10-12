# !usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore

class Rect(QtWidgets.QGraphicsRectItem):
    def __init__(self, parent, x1 = None, y1 = None
                 , x2 = None, y2 = None):
        """first argument is parent of the object (when object is declared, next four arguments is coordinates"""
        QtWidgets.QGraphicsItem.__init__(self)
        if x1 == None and x2 == None and y1 == None and y2 == None:
            self.setCoordinates(parent.geometry().width() / 2, parent.geometry().height() / 2,
                                parent.geometry().width() / 2 + 20, parent.geometry().height() / 2 + 10)
        elif x1 != None and x2 != None and y1 != None and y2 != None:
            self.setCoordinates(x1, y1, x2, y2)

    def paint(self, painter, option, widget = None):
        pen = QtGui.QPen(QtCore.Qt.red, 5)
        painter.setPen(pen)

        rect = self.boundingRect()
        painter.drawRect(rect)

        brush = QtGui.QBrush(QtCore.Qt.black)
        painter.fillRect(rect, brush)

    def setCoordinates(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def boundingRect(self):
        return QtCore.QRectF(QtCore.QPointF(self.x1, self.y1), QtCore.QPointF(self.x2, self.y2))

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())

        stroker = QtGui.QPainterPathStroker()
        stroker.setWidth(5)
        return stroker.createStroke(path)
