# !usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from platform import *
from ball import *
class Engine(QtWidgets.QFrame):
    def __init__(self, parent):
        QtWidgets.QFrame.__init__(self)
        self.box = [] # box for all bricks on the top of the screen

        # in constructor width of the frame is bigger about 40 pixels than outside. I don't know why.
        initWidth = self.geometry().width() - 40
        # the same problem but bigger about 180 pixels
        initHeight = self.geometry().height() - 180

        self.platformX = initWidth / 2 - 20
        self.platformY = initHeight

        self.platform = Platform(self) # platform on the bottom of the screen

        self.addWidgetsToBox(1)

        self.setFocusPolicy(QtCore.Qt.StrongFocus) # this function allows keyevents work

        self.ball = Ball(self)

        self.speed = 10
        self.timer = QtCore.QBasicTimer()
        self.timer.start(self.speed, self)
        self.ballPreviousPositionY = self.ball.y1 - 1.1
        self.ballPreviousPositionX = self.ball.x1 - 1.1

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.platform.setCoordinates(self.platformX, self.platformY - 10, self.platformX + 40, self.platformY)

        self.platform.paintWidget(painter)

        self.ball.paintWidget(painter)

        self.paintWidgetsInBox(painter)
        painter.end()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            shiftX = self.ball.x1 - self.ballPreviousPositionX
            shiftY = self.ball.y1 - self.ballPreviousPositionY

            self.tryMove(shiftX, shiftY)
            self.ballPreviousPositionX = self.ball.x1
            self.ballPreviousPositionY = self.ball.y1
            self.ball.setCoordinates(self.ball.x1 + shiftX, self.ball.y1 + shiftY)

        self.update()

    def tryMove(self, shiftX, shiftY):
        pass
    def paintWidgetsInBox(self, painter):
        x = self.geometry().width() / 10

        for i in xrange(10):
            self.box[i].setCoordinates(x * i + 2, 3, x * (i + 1) - 2, 13)

        self.update()

    def addWidgetsToBox(self, level):
        if level == 1:
            for i in xrange(0, 10):
                rect = Rect(self)
                self.box.append(rect)

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Left:
            self.platformX -= 10

        elif key == QtCore.Qt.Key_Right:
            self.platformX += 10

        self.update()
