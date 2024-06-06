from uuid import uuid4
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine
from game.components import rectangle

class Relation:
    def __init__(self, rect_start: rectangle.Rectangle, rect_end: rectangle.Rectangle):
        self.id = uuid4()
        self.rect_start = rect_start
        self.rect_end = rect_end

    def draw(self, painter: QPainter):
        start_point = self.rect_start.getCenter()
        end_point = self.rect_end.getCenter()
        rel = QLine(start_point, end_point)
        painter.drawLine(rel)