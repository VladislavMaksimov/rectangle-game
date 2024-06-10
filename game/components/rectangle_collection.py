from PyQt6.QtCore import QPoint
from game.components import rectangle

class RectangleCollection:
    def __init__(self, initial_collection: list[rectangle.Rectangle] = []):
        self.__collection = initial_collection

    def getRectangles(self):
        return self.__collection
    
    def getRectangleByPoint(self, point: QPoint):
        for rect in self.__collection:
            if rect.contains(point):
                return rect
        return None
    
    def checkCollisions(self, rect_check: rectangle.Rectangle):
        for rect in self.__collection:
            if rect_check == rect:
                continue
            if rect_check.intersects(rect):
                return True
        return False

    def addRectangle(self, rect: rectangle.Rectangle):
        if not self.checkCollisions(rect):
            self.__collection.append(rect)
            return True
        return False

