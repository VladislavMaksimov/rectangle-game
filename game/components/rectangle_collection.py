from PyQt6.QtGui import QPainter
from game.components import rectangle

class RectangleCollection:
    def __init__(self, initial_collection: list[rectangle.Rectangle] = []):
        self.collection = initial_collection

    def getRectangles(self):
        return self.collection

    def addRectangle(self, rect: rectangle.Rectangle):
        self.collection.append(rect)

    def checkCollisions(self, rect_check: rectangle.Rectangle):
        for rect in self.collection:
            if (
                rect.end.x() < rect_check.begin.x()
                or rect.end.y() < rect_check.begin.y()
                or rect.begin.x() > rect_check.end.x()
                or rect.begin.y() > rect_check.end.y()
            ):
                continue
            return True
        return False

    def draw(self, painter: QPainter):
        for rect in self.collection:
            rect.draw(painter)