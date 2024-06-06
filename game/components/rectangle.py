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

    def draw(self, painter: QPainter):
        painter.setBrush(self.color)
        rect = QRect(self.begin, self.end)
        painter.drawRect(rect)