from __future__ import annotations
from uuid import uuid4
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect, QPoint
from utils import random_color
from game.components import constants

class Rectangle:
    def __init__(self, x: int, y: int):
        self.id = uuid4()

        self.width = constants.RECTANGLE_WIDTH
        self.height = constants.RECTANGLE_HEIGHT

        self.begin = QPoint()
        self.end = QPoint()

        offset_x = round(constants.RECTANGLE_WIDTH / 2)
        offset_y = round(constants.RECTANGLE_HEIGHT / 2)

        self.begin.setX(x - offset_x)
        self.begin.setY(y - offset_y)
        self.end.setX(x + offset_x)
        self.end.setY(y + offset_y)

        rgb = random_color.getRandomRGB()
        self.color = QColor(*rgb)

    def getCenter(self):
        center_x = round(self.begin.x() + self.width / 2)
        center_y = round(self.begin.y() + self.height / 2)
        return QPoint(center_x, center_y)

    def checkPointInsideRectangle(self, point: QPoint):
        pointX = point.x()
        pointY = point.y()
        if (
            self.begin.x() <= pointX 
            and self.end.x() >= pointX 
            and self.begin.y() <= pointY 
            and self.end.y() >= pointY
        ):
            return True
        else:
            return False
        
    def checkCollision(self, rect_check: Rectangle):
        x_delta = abs(self.begin.x() - rect_check.begin.x())
        y_delta = abs(self.begin.y() - rect_check.begin.y())
        
        if (
             x_delta < constants.RECTANGLE_WIDTH
             and y_delta < constants.RECTANGLE_HEIGHT
        ):
            return True
        return False
    
    def draw(self, painter: QPainter):
        painter.setBrush(self.color)
        rect = QRect(self.begin, self.end)
        painter.drawRect(rect)