from collections.abc import Callable
from PyQt6.QtCore import QPoint
from game.components import rectangle, rectangle_collection, relation, relation_collection, constants as component_constants

class DragDropRectLogicController:
    def __init__(self):
        self.dragged_rect: rectangle.Rectangle | None = None
        self.dragged_rect_relations: list[relation.Relation] | None = None
        self.initial_begin_point: QPoint | None = None
        self.initial_end_point: QPoint | None = None
        self.cursor_offset_x: int | None = None
        self.cursor_offset_y: int | None = None

    def startDragging(
            self,
            cursor_position: QPoint,
            dragged_rect: rectangle.Rectangle,
            relations: relation_collection.RelationCollection
        ):
        self.dragged_rect = dragged_rect
        
        self.initial_begin_point = QPoint(dragged_rect.begin)
        self.initial_end_point = QPoint(dragged_rect.end)

        self.cursor_offset_x =  cursor_position.x() - dragged_rect.begin.x() 
        self.cursor_offset_y =  cursor_position.y() - dragged_rect.begin.y()

        self.dragged_rect_relations = relations.getRelationsByRectId(dragged_rect.id)

    def moveRelations(self):
        if self.dragged_rect_relations is None:
            return
            
        for rel in self.dragged_rect_relations:
            rel.move()

    def drag(self, cursor_position: QPoint, update: Callable[[], None]):
        if self.dragged_rect is None:
            return

        new_begin_x = cursor_position.x() - self.cursor_offset_x
        new_begin_y = cursor_position.y() - self.cursor_offset_y

        self.dragged_rect.begin.setX(new_begin_x)
        self.dragged_rect.begin.setY(new_begin_y)
        self.dragged_rect.end.setX(new_begin_x + component_constants.RECTANGLE_WIDTH)
        self.dragged_rect.end.setY(new_begin_y + component_constants.RECTANGLE_HEIGHT)

        self.moveRelations()

        update()

    def clearDragging(self):
        self.dragged_rect = None
        self.initial_begin_point = None
        self.initial_end_point = None
        self.cursor_offset_x = None
        self.cursor_offset_y = None

    def abortDragging(self, update):
        self.dragged_rect.begin = self.initial_begin_point
        self.dragged_rect.end = self.initial_end_point
        self.moveRelations()
        update()

        self.clearDragging()

    def endDragging(
            self,
            rectangles: rectangle_collection.RectangleCollection,
            update,
            checkRectOutOfBorders
        ):
        if self.dragged_rect is None:
            self.clearDragging()
            return

        if (
            rectangles.checkCollisions(self.dragged_rect)
            or checkRectOutOfBorders(self.dragged_rect)
        ):
            self.abortDragging(update)
        else:
            self.clearDragging()