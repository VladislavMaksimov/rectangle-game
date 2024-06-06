from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent
from PyQt6.QtWidgets import QWidget
from game import constants
from game.components import rectangle, rectangle_collection, relation_collection, relation

class GameField(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = constants.WINDOW_WIDTH
        self.window_height = constants.WINDOW_HEIGHT
        self.setFixedWidth(self.window_width)
        self.setFixedHeight(self.window_height)
        self.setWindowTitle('Rectangle game')

        self.rectangles = rectangle_collection.RectangleCollection()
        self.relations = relation_collection.RelationCollection()
        self.relation_rect_start: rectangle.Rectangle | None = None
    
    def paintEvent(self, _: QPaintEvent | None):
        painter = QPainter(self)
        self.rectangles.draw(painter)
        self.relations.draw(painter)

    def checkRectOutOfBorders(self, rect: rectangle.Rectangle):
        if (
            self.window_width < rect.end.x() 
            or self.window_height < rect.end.y()
            or rect.begin.x() < 0
            or rect.begin.y() < 0
        ):
          return True
        return False  

    def mouseDoubleClickEvent(self, event: QMouseEvent | None):
        x = event.pos().x()
        y = event.pos().y()
        rect = rectangle.Rectangle(x, y)
        if (self.rectangles.checkCollisions(rect) or self.checkRectOutOfBorders(rect)):
            return
        self.rectangles.addRectangle(rect)
        self.update()

    def mousePressEvent(self, event: QMouseEvent | None):
        clicked_rect = self.rectangles.getRectangleByPoint(event.pos())

        if clicked_rect is None:
            return
        
        if self.relation_rect_start is None:
            self.relation_rect_start = clicked_rect
            return
        
        rel = relation.Relation(self.relation_rect_start, clicked_rect)
        self.relations.addRelation(rel)
        self.relation_rect_start = None
        self.update()