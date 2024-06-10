from PyQt6.QtCore import Qt, QRect, QSize, QPoint
from utils import random_color

RECTANGLE_WIDTH = 200
RECTANGLE_HEIGHT = 100

class Rectangle(QRect):
    def __init__(self, creation_point: QPoint):
        atopLeft = QPoint(
            creation_point.x() - round(RECTANGLE_WIDTH / 2),
            creation_point.y() - round(RECTANGLE_HEIGHT / 2)
        )
        asize = QSize(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
        super().__init__(atopLeft, asize)

        self.__background_color = random_color.getRandomRGB()

        self.__dragging = False
        self.__drag_offset = QPoint()
    
    def backgroundColor(self):
        return self.__background_color
    
    def dragOffset(self):
        return self.__drag_offset
    
    def startDragging(self, cursor_position: QPoint):
        self.__dragging = True
        self.__drag_offset = cursor_position - self.topLeft()

    def drag(self, cursor_position: QPoint):
        if self.__dragging:
            new_top_left = cursor_position - self.__drag_offset
            self.moveTopLeft(new_top_left)

    def stopDragging(self):
        self.__dragging = False
