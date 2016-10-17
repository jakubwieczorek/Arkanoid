# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from rect import *
from platform import *

class Ball(QtWidgets.QGraphicsPixmapItem):
    width = 20
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

        self.ballPreviousPosition = QtCore.QPointF()

    def collidingEvent(self):
        """ Function check is it collision and returning True if is collision and False in opposite"""
        collidingItems = self.collidingItems() # list with all items

        isCollision = False

        for i in xrange(0, len(self.collidingItems())):
            distance = pow(pow(self.getPreviousPosition().x() - self.pos().x(), 2) + pow(self.getPreviousPosition().y() - self.pos().y(), 2), 0.5)
            if type(collidingItems[i]) is Rect or type(collidingItems[i]) is Platform:
                isCollision = True

                rectPixmap = collidingItems[i]

                middleRectY = rectPixmap.y() + rectPixmap.getHeight() / 2
                middleBallY = self.y() + self.width / 2

                middleRectX = rectPixmap.x() + rectPixmap.getWidth() / 2
                middleBallX = self.x() + self.width / 2

                # collision on right or left edge of the rect
                if abs(middleBallY - middleRectY) < rectPixmap.getHeight() / 2 and -(rectPixmap.x() + rectPixmap.getWidth()) + self.x() < 3:
                    shiftX = -self.x() + self.getPreviousPosition().x()
                    shiftY = self.y() - self.getPreviousPosition().y()

                # collision on bottom or top edge of the rect
                elif abs(middleBallX - middleRectX) < rectPixmap.getWidth() / 2 + Ball.width / 2 and -(rectPixmap.y() + rectPixmap.getHeight()) + self.y() < 3 :

                    # distance between previous position and present position must be the same !!!!
                    if abs(middleBallX - middleRectX) < rectPixmap.getWidth() / 2 - Ball.width / 2: # if in setting of middle of rect
                        shiftX = self.x() - self.getPreviousPosition().x()
                        shiftY = -self.y() + self.getPreviousPosition().y()
                    elif abs(middleBallX - middleRectX) < rectPixmap.getWidth() / 2 and abs(middleBallX - middleRectX) > rectPixmap.getWidth() / 2 - Ball.width / 2: # if in setting of the corner
                        shiftX = 1.5 * (self.x() - self.getPreviousPosition().x())
                        shiftY = -self.y() + self.getPreviousPosition().y()
                        shift = pow(pow(shiftX, 2) + pow(shiftY, 2), 0.5)

                        shiftX = shiftX * distance / shift
                        shiftY = shiftY * distance / shift

                        print "I'm in 2"

                    else: # if in the setting of the corner and rect Ball corner
                        shiftX = 2 * (self.x() - self.getPreviousPosition().x())
                        shiftY = -(-self.y() + self.getPreviousPosition().y())
                        print "I'm in"

                        shift = pow(pow(shiftX, 2) + pow(shiftY, 2), 0.5)

                        shiftX = shiftX * distance / shift
                        shiftY = shiftY * distance / shift


                else:
                    shiftX = self.x() - self.getPreviousPosition().x()
                    shiftY = self.y() - self.getPreviousPosition().y()

                self.setPreviousPosition(QtCore.QPointF(self.x(), self.y()))
                self.setPos(self.x() + shiftX, self.y() + shiftY)

                if type(collidingItems[i]) is Rect:
                    self.parent.box.remove(collidingItems[i])
                    self.scene().removeItem(collidingItems[i])
                    self.parent.points = self.parent.points + 100
                    self.parent.msgToStatusBar.emit(str(self.parent.points))

        return isCollision

    def getPreviousPosition(self):
        return self.ballPreviousPosition

    def setPreviousPosition(self, pointf):
        """point is QtCore.QtPointF type"""
        self.ballPreviousPosition = pointf