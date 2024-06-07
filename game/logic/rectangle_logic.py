from collections.abc import Callable
from PyQt6.QtCore import QPoint
from game.components import rectangle, rectangle_collection

class RectangleLogicController():
    def __init__(self):
        pass

    def createRectangleAtPoint(
        self,
        point: QPoint,
        rectangles: rectangle_collection.RectangleCollection,
        checkRectOutOfBorders: Callable[[rectangle.Rectangle], bool],
        update: Callable[[], None]
    ):
        rect = rectangle.Rectangle(point.x(), point.y())
        if (rectangles.checkCollisions(rect) or checkRectOutOfBorders(rect)):
            return
        rectangles.addRectangle(rect)
        update()