from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent, QColor
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QRect, QPoint
from utils import random_color
from game import constants

class GameField(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = 640
        self.window_height = 480
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle('Rectangle game')
        self.begin = QPoint()
        self.end = QPoint()
    
    def paintEvent(self, _: QPaintEvent | None) -> None:
        if self.begin.isNull() or self.end.isNull():
            return
        painter = QPainter(self)
        rgb = random_color.getRandomRGB()
        painter.setBrush(QColor(*rgb))
        rect = QRect(self.begin, self.end)
        painter.drawRect(rect)

    def mouseDoubleClickEvent(self, event: QMouseEvent | None) -> None:
        x = event.pos().x()
        y = event.pos().y()
        offsetX = round(constants.RECTANGLE_WIDTH / 2)
        offsetY = round(constants.RECTANGLE_HEIGHT / 2)
        self.begin.setX(x - offsetX)
        self.begin.setY(y - offsetY)
        self.end.setX(x + offsetX)
        self.end.setY(y + offsetY)
        self.update()
        return