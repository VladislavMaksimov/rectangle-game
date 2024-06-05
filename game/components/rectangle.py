from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent, QColor
from PyQt6.QtCore import QRect, QPoint
from utils import random_color
from game.components import constants

class Rectangle:
    def __init__(self, x: int, y: int):
        self.width = constants.RECTANGLE_WIDTH
        self.height = constants.RECTANGLE_HEIGHT

        self.begin = QPoint()
        self.end = QPoint()

        offsetX = round(constants.RECTANGLE_WIDTH / 2)
        offsetY = round(constants.RECTANGLE_HEIGHT / 2)

        self.begin.setX(x - offsetX)
        self.begin.setY(y - offsetY)
        self.end.setX(x + offsetX)
        self.end.setY(y + offsetY)

    def draw(self, painter: QPainter):
        rgb = random_color.getRandomRGB()
        painter.setBrush(QColor(*rgb))
        rect = QRect(self.begin, self.end)
        painter.drawRect(rect)