from uuid import uuid4
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QLine, QPoint
from utils import point_between_points
from game.components import rectangle

class Relation:
    def __init__(self, rect_start: rectangle.Rectangle, rect_end: rectangle.Rectangle):
        self.id = uuid4()

        self.rect_start = rect_start
        self.rect_end = rect_end

        self.start_point = rect_start.getCenter()
        self.end_point = rect_end.getCenter()

    def checkPointOnRelation(self, point: QPoint):
        return point_between_points.checkPointBetweenPoints(
            (self.start_point.x(), self.start_point.y()),
            (self.end_point.x(), self.end_point.y()),
            (point.x(), point.y()),
            calc_error = 0.5
        )

    def draw(self, painter: QPainter):
        rel = QLine(self.start_point, self.end_point)
        painter.drawLine(rel)