from PyQt6.QtGui import QPainter
from game.components import rectangle

class RectangleCollection:
    def __init__(self, initialCollection: list[rectangle.Rectangle] = []):
        self.collection = initialCollection

    def checkCollisions(self, rectToCheck: rectangle.Rectangle):
        for rect in self.collection:
            if (
                rect.end.x() < rectToCheck.begin.x()
                or rect.end.y() < rectToCheck.begin.y()
                or rect.begin.x() > rectToCheck.end.x()
                or rect.begin.y() > rectToCheck.end.y()
            ):
                continue
            return True
        return False

    def draw(self, painter: QPainter):
        for rect in self.collection:
            rect.draw(painter)