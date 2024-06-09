from PyQt6.QtGui import QPainter
from PyQt6.QtCore import QPoint
from game.components import rectangle

class RectangleCollection:
    def __init__(self, initial_collection: list[rectangle.Rectangle] = []):
        self.collection = initial_collection

    def getRectangles(self):
        return self.collection
    
    def getRectangleByPoint(self, point: QPoint):
        for rect in self.collection:
            if rect.checkPointInsideRectangle(point):
                return rect
        return None

    def addRectangle(self, rect: rectangle.Rectangle):
        self.collection.append(rect)

    def checkCollisions(self, rect_check: rectangle.Rectangle):
        for rect in self.collection:
            if rect.id == rect_check.id:
                continue
            if rect.checkCollision(rect_check):
                return True
        return False

    def draw(self, painter: QPainter):
        for rect in self.collection:
            rect.draw(painter)