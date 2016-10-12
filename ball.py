# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from rect import *

class Ball(QtWidgets.QGraphicsEllipseItem):
    def __init__(self, parent, x1 = None, y1 = None, r = None):
        QtWidgets.QWidget.__init__(self)
        if x1 == None and y1 == None and r == None:
            self.x1 = parent.geometry().width() / 2
            self.y1 = parent.geometry().height() / 2
            self.r = 20
            self.parent = parent

        elif x1 != None and y1 !=None and r != None:
            self.setCoordinates(x1, y1)
            self.setRay(r)

    def paint(self, painter, option, widget = None):
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

    def collidingEvent(self):
        collidingItems = self.collidingItems() # list with all items

        for i in xrange(0, len(self.collidingItems())):
            if isinstance(collidingItems[i], Rect):

                #path = QtGui.QPainterPath()
                #path.addEllipse(self.boundingRect())
                #print path.intersects()

                self.scene().removeItem(collidingItems[i])
                self.parent.box.remove(collidingItems[i])

    def boundingRect(self):
        return QtCore.QRectF(QtCore.QPointF(self.x1 - self.r, self.y1 - self.r), QtCore.QPointF(self.x1 + self.r, self.y1 + self.r))


    def shape(self):
       path = QtGui.QPainterPath()
       path.addEllipse(self.boundingRect())

       stroker = QtGui.QPainterPathStroker()
       stroker.setWidth(5)
       stroker.setJoinStyle(QtCore.Qt.MiterJoin)

       return stroker.createStroke(path)

