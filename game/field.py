from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent
from PyQt6.QtWidgets import QWidget
from game import constants
from game.components import rectangle, rectangle_collection, relation_collection
from game.logic import rectangle_logic, relation_logic, drag_drop_logic

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

        self.rectangle_logic_controller = rectangle_logic.RectangleLogicController()
        self.relation_logic_controller = relation_logic.RelationLogicController()
        self.rect_drag_drop_logic_controller = drag_drop_logic.DragDropRectLogicController()

        self.setAcceptDrops(True)
    
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
        self.rectangle_logic_controller.createRectangleAtPoint(
            event.pos(),
            self.rectangles,
            self.checkRectOutOfBorders,
            self.update
        )

    def mousePressEvent(self, event: QMouseEvent | None):
        clicked_point = event.pos()

        if event.button() == Qt.MouseButton.LeftButton:
            clicked_rect = self.rectangles.getRectangleByPoint(clicked_point)
            if clicked_rect:
                self.relation_logic_controller.createRelation(
                    clicked_rect,
                    self.relations,
                    self.update
                )
                self.rect_drag_drop_logic_controller.startDragging(
                    clicked_point,
                    clicked_rect,
                    self.relations
                )
            return
        
        if event.button() == Qt.MouseButton.RightButton:
            self.relation_logic_controller.removeRelation(
                clicked_point,
                self.relations,
                self.update
            )
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        cursor_position = event.pos()
        self.rect_drag_drop_logic_controller.drag(cursor_position, self.update)
    
    def mouseReleaseEvent(self, _: QMouseEvent) -> None:
        self.rect_drag_drop_logic_controller.endDragging(
            self.rectangles,
            self.update,
            self.checkRectOutOfBorders
        )