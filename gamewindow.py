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

        #self.setFocusPolicy(QtCore.Qt.StrongFocus) # this function allows keyevents work

        self.ball = Ball(self)
        self.scene.addItem(self.ball)

        self.speed = 5
        self.timer = QtCore.QTimer(self)
        self.timer.start(self.speed)
        self.timer.timeout.connect(self.timeEvent)

        self.ballPreviousPositionY = self.ball.y1 - 1.1 # its demanding to give these variables initial values for example these
        self.ballPreviousPositionX = self.ball.x1 - 1.1

        self.addShapes()

    def timeEvent(self):
        self.moveBall()

    def moveBall(self):
        self.ball.collidingEvent()

        if  self.sceneRect.right() - (self.ball.x1 + self.ball.r) < 1 or self.ball.x1 - self.ball.r < 2:
            shiftX = -self.ball.x1 + self.ballPreviousPositionX
            shiftY = self.ball.y1 - self.ballPreviousPositionY

        elif self.sceneRect.bottom() - (self.ball.y1 + self.ball.r) < 1 or self.ball.y1 - self.ball.r < 2:
            shiftX = self.ball.x1 - self.ballPreviousPositionX
            shiftY = -self.ball.y1 + self.ballPreviousPositionY

        else:
            shiftX = self.ball.x1 - self.ballPreviousPositionX
            shiftY = self.ball.y1 - self.ballPreviousPositionY


        self.ballPreviousPositionX = self.ball.x1
        self.ballPreviousPositionY = self.ball.y1
        self.ball.setCoordinates(self.ball.x1 + shiftX, self.ball.y1 + shiftY)
        self.scene.update()

    def addShapes(self):
        shapeWidth = self.sceneRect.width() / 10
        rawAmount = self.sceneRect.width() / shapeWidth

        for i in xrange(0, int(rawAmount)):
            self.box.append(Rect(self, shapeWidth * i + 5, 0, shapeWidth * (i + 1), 50))
            self.scene.addItem(self.box[i])
