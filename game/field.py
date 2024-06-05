from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPoint
from game import constants
from game.components import rectangle

class GameField(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = constants.WINDOW_WIDTH
        self.window_height = constants.WINDOW_HEIGHT
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle('Rectangle game')
        self.begin = QPoint()
        self.end = QPoint()
        self.rectangle = None
    
    def paintEvent(self, _: QPaintEvent | None) -> None:
        if self.rectangle is None:
            return
        painter = QPainter(self)
        self.rectangle.draw(painter)

    def mouseDoubleClickEvent(self, event: QMouseEvent | None) -> None:
        x = event.pos().x()
        y = event.pos().y()
        self.rectangle = rectangle.Rectangle(x, y)
        self.update()
        return