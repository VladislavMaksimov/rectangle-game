from PyQt6.QtCore import QLine, QPoint
from utils import point_between_points
from game.components import rectangle

class Relation(QLine):
    def __init__(self, rect_start: rectangle.Rectangle, rect_end: rectangle.Rectangle):
        self.__rect_start = rect_start
        self.__rect_end = rect_end
        super().__init__(self.__rect_start.center(), self.__rect_end.center())

    def checkPointOnRelation(self, point: QPoint):
        rel_p1 = (self.x1(), self.y1())
        rel_p2 = (self.x2(), self.y2())
        point_to_check = (point.x(), point.y())
            
        return point_between_points.checkPointBetweenPoints(
            rel_p1,
            rel_p2,
            point_to_check,
            0.5
        )
    
    def checkConnectRect(self, rect: rectangle.Rectangle):
        if self.__rect_start == rect or self.__rect_end == rect:
            return True
        return False

    def move(self):
        self.setPoints(
            self.__rect_start.center(),
            self.__rect_end.center()
        )