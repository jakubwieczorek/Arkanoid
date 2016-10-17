# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from platform import *
from ball import *
from backgrounditem import *

class GameView(QtWidgets.QGraphicsView):
    msgToStatusBar = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        QtWidgets.QGraphicsView.__init__(self)

        self.msgToStatusBar[str].connect(parent.statusBar.showMessage)

        self.setMouseTracking(True) # thanks to this, mouseMoveEvent works, without pressing a key on mouse

        self.box = [] # container for all items

        self.setWindowTitle("Game")

        self.sceneRect = QtCore.QRectF(0,0,600,300)

        self.createGameScene()
        self.createWelcomeScene()

        self.setScene(self.welcomeScene)

        # timer and speed
        self.speed = 3
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timeEvent)

        self.ball.setPreviousPosition(QtCore.QPointF(self.ball.x() + 0.5, self.ball.y() + 0.5))
        self.addShapes()

        self.points = 0
        self.isPaused = False

    def createGameScene(self):
        # game scene with all items: ball, slabs, etc...
        self.scene = QtWidgets.QGraphicsScene()

        self.scene.setSceneRect(self.sceneRect)

        self.ball = Ball(self)
        self.scene.addItem(self.ball)

        self.platform = Platform(self, self.sceneRect.width() / 2, self.sceneRect.height() - Platform.getHeight())
        self.scene.addItem(self.platform)

    def createWelcomeScene(self):
        self.welcomeScene = QtWidgets.QGraphicsScene()
        self.welcomeScene.setSceneRect(self.sceneRect)

        startButton = QtWidgets.QPushButton("Start")
        startButton.setGeometry(QtCore.QRect(self.sceneRect.width() / 2 - 75, 50, 150, 50))
        self.welcomeScene.addWidget(startButton)

        self.nameEdit = QtWidgets.QLineEdit()
        self.nameEdit.setGeometry(QtCore.QRect(self.sceneRect.width() / 2 - 75, 100, 150, 50))
        self.welcomeScene.addWidget(self.nameEdit)

        quitButton = QtWidgets.QPushButton("Quit")
        quitButton.setGeometry(QtCore.QRect(self.sceneRect.width() / 2 - 75, 250, 150, 50))
        self.welcomeScene.addWidget(quitButton)

        background = BackgroundItem(self, "../Game/backwelcome.jpg")
        self.welcomeScene.addItem(background)

        startButton.clicked.connect(self.start)
        quitButton.clicked.connect(QtWidgets.QApplication.quit)

    def timeEvent(self):
        self.moveBall()

    def mouseMoveEvent(self, event):
        if event.pos().x() < self.sceneRect.width() - self.platform.getWidth() and self.isPaused == False:
            self.platform.setPos(event.pos().x(), self.platform.pos().y())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_P:
            self.pause()

        if event.key() == QtCore.Qt.Key_S:
            self.start()

    def pause(self):
        self.timer.stop()
        self.msgToStatusBar.emit("Pause")
        self.isPaused = True

    def start(self):
        self.timer.start(self.speed)
        if self.isPaused == True:
            self.msgToStatusBar.emit("Go")
        self.setScene(self.scene)
        self.isPaused = False

    def moveBall(self):
        if self.ball.collidingEvent() == False: # if isn't collision check is it collision with one of the wall's
            # ball is returning from left or right wall
            if  self.sceneRect.right() - (self.ball.x() + 2 * self.ball.r) < 1 or self.ball.x() < 1:
                shiftX = -self.ball.x() + self.ball.getPreviousPosition().x()
                shiftY = self.ball.y() - self.ball.getPreviousPosition().y()

            # ball is returning from bottom or top
            elif self.ball.y() < 1:
                shiftX = self.ball.x() - self.ball.getPreviousPosition().x()
                shiftY = -self.ball.y() + self.ball.getPreviousPosition().y()

            elif self.sceneRect.bottom() - (self.ball.y() + 2 * self.ball.r) < 1:
                self.ball.hide()
                shiftY = shiftX = 0

            else:
                shiftX = self.ball.x() - self.ball.getPreviousPosition().x()
                shiftY = self.ball.y() - self.ball.getPreviousPosition().y()

            self.ball.setPreviousPosition(QtCore.QPointF(self.ball.x(), self.ball.y()))
            self.ball.setPos(self.ball.x() + shiftX, self.ball.y() + shiftY)

        self.scene.update()

    def addShapes(self):

        rawAmount = 600 / Rect.getWidth()
        columnAmount = 6

        rectAmount = 0
        for i in xrange(0, int(rawAmount)):
            for j in xrange(0, columnAmount):
                self.box.append(Rect(self, Rect.getWidth() * i, j * Rect.getHeight()))
                self.scene.addItem(self.box[rectAmount])
                rectAmount = rectAmount + 1

        self.background = BackgroundItem(self, "../Game/back1.jpg")
        self.scene.addItem(self.background)
