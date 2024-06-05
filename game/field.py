from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent
from PyQt6.QtWidgets import QWidget
from game import constants
from game.components import rectangle, rectangle_collection

class GameField(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = constants.WINDOW_WIDTH
        self.window_height = constants.WINDOW_HEIGHT
        self.setFixedWidth(self.window_width)
        self.setFixedHeight(self.window_height)
        self.setWindowTitle('Rectangle game')

        self.rectangles = rectangle_collection.RectangleCollection()
    
    def paintEvent(self, _: QPaintEvent | None) -> None:
        painter = QPainter(self)
        self.rectangles.draw(painter)

    def checkRectOutOfBorders(self, rect: rectangle.Rectangle):
        if (
            self.window_width < rect.end.x() 
            or self.window_height < rect.end.y()
            or rect.begin.x() < 0
            or rect.begin.y() < 0
        ):
          return True
        return False  

    def mouseDoubleClickEvent(self, event: QMouseEvent | None) -> None:
        x = event.pos().x()
        y = event.pos().y()
        rect = rectangle.Rectangle(x, y)
        if (self.rectangles.checkCollisions(rect) or self.checkRectOutOfBorders(rect)):
            return
        self.rectangles.collection.append(rect)
        self.update()