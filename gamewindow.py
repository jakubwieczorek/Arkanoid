# !/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from platform import *
from ball import *

class GameView(QtWidgets.QGraphicsView):
    def __init__(self):
        QtWidgets.QGraphicsView.__init__(self)

        self.box = []
        self.scene = QtWidgets.QGraphicsScene()

        self.sceneRect = QtCore.QRectF(0,0,600,300)
        self.scene.setSceneRect(self.sceneRect)

        pen = QtGui.QPen(QtCore.Qt.black, 5) # pen is painting game field on the scene
        self.scene.addRect(self.sceneRect, pen)

        self.setScene(self.scene)

        self.setWindowTitle("My Game")

        self.ball = Ball(self)
        self.scene.addItem(self.ball)

        self.speed = 5
        self.timer = QtCore.QTimer(self)
        self.timer.start(self.speed)
        self.timer.timeout.connect(self.timeEvent)

        self.ballPreviousPositionY = self.ball.y() - 1.1 # its demanding to give these variables initial values for example these
        self.ballPreviousPositionX = self.ball.x() - 1.1

        self.addShapes()

    def timeEvent(self):
        self.moveBall()

    def moveBall(self):
        self.ball.collidingEvent()

        if  self.sceneRect.right() - (self.ball.x() + 2 * self.ball.r) < 1 or self.ball.x() < 2:
            shiftX = -self.ball.x() + self.ballPreviousPositionX
            shiftY = self.ball.y() - self.ballPreviousPositionY

        elif self.sceneRect.bottom() - (self.ball.y() + 2 * self.ball.r) < 1 or self.ball.y() < 2:
            shiftX = self.ball.x() - self.ballPreviousPositionX
            shiftY = -self.ball.y() + self.ballPreviousPositionY

        else:
            shiftX = self.ball.x() - self.ballPreviousPositionX
            shiftY = self.ball.y() - self.ballPreviousPositionY


        self.ballPreviousPositionX = self.ball.x()
        self.ballPreviousPositionY = self.ball.y()
        self.ball.setPos(self.ball.x() + shiftX, self.ball.y() + shiftY)

        self.scene.update()

    def addShapes(self):
        shapeWidth = self.sceneRect.width() / 10
        rawAmount = 600 / Rect.getWidth()

        for i in xrange(0, int(rawAmount)):
            self.box.append(Rect(self, Rect.getWidth() * i, 0))
            self.scene.addItem(self.box[i])
