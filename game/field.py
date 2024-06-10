from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPainter, QPaintEvent, QColor
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPoint
from game.components import rectangle_collection, relation_collection, rectangle
from game.logic import relation_logic, drag_drop_logic

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class GameField(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT
        self.setFixedWidth(self.window_width)
        self.setFixedHeight(self.window_height)
        self.setWindowTitle('Rectangle game')

        self.rectangles = rectangle_collection.RectangleCollection()
        self.relations = relation_collection.RelationCollection()

        self.relation_logic_controller = relation_logic.RelationLogicController()
        self.drag_drop_logic_controller = drag_drop_logic.DragDropRectLogicController()

    def __addRelationOnClick(self, clicked_point: QPoint):
        clicked_rect = self.rectangles.getRectangleByPoint(clicked_point)
        if clicked_rect is None:
            return
        
        created_rel = self.relation_logic_controller.createRelation(clicked_rect)
        if created_rel is None:
            return
        
        is_success = self.relations.addRelation(created_rel)
        if is_success:
            self.update()

    def __removeRelationOnClick(self, clicked_point: QPoint):
        is_success = self.relation_logic_controller.removeRelation(
            clicked_point,
            self.relations
        )

        if is_success:
            self.update()

    def checkRectOutOfBorders(self, rect: rectangle.Rectangle):
        left_border = 0
        top_border = 0
        right_border = self.width()
        bottom_border = self.height()

        if (
            rect.topLeft().x() < left_border
            or rect.topLeft().y() < top_border
            or rect.bottomRight().x() > right_border
            or rect.bottomRight().y() > bottom_border
        ):
            return True
        return False

    def mousePressEvent(self, event: QMouseEvent | None):
        clicked_point = event.pos()

        if event.button() == Qt.MouseButton.LeftButton:
           self.__addRelationOnClick(clicked_point)
           self.drag_drop_logic_controller.startDragging(
               clicked_point,
               self.rectangles,
               self.relations
           )

        if event.button() == Qt.MouseButton.RightButton:
            self.__removeRelationOnClick(clicked_point)

    def mouseMoveEvent(self, event: QMouseEvent):
        is_success = self.drag_drop_logic_controller.drag(
            event.pos(),
            self.rectangles,
            self.checkRectOutOfBorders,
            self.width(),
            self.height(),
        )
        if is_success:
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_drop_logic_controller.stopDragging()

    def mouseDoubleClickEvent(self, event: QMouseEvent | None):
        new_rect = rectangle.Rectangle(event.pos())

        if self.checkRectOutOfBorders(new_rect):
            return
        
        is_success = self.rectangles.addRectangle(new_rect)
        if is_success:
            self.update()
   
    def paintEvent(self, _: QPaintEvent | None):
        painter = QPainter(self)

        for rect in self.rectangles.getRectangles():
            color = QColor(*rect.backgroundColor())
            painter.setBrush(color)
            painter.drawRect(rect)

        painter.setBrush(QColor(0, 0, 0))

        for rel in self.relations.getRelations():
            painter.drawLine(rel)