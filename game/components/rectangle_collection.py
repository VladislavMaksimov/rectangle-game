from PyQt6.QtGui import QPainter
from game.components import rectangle

class RectangleCollection:
    def __init__(self, initialCollection: list[rectangle.Rectangle] = []):
        self.collection = initialCollection

    def draw(self, painter: QPainter):
        for rect in self.collection:
            rect.draw(painter)