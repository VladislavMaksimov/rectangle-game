from PyQt6.QtCore import QPoint, QRect
from PyQt6.QtGui import QCursor
from game.components import rectangle, relation, relation_collection, rectangle_collection, constants as component_constants
from game import constants as game_constants

class DragDropRectLogicController:
    def __init__(self):
        self.dragged_rect: rectangle.Rectangle | None = None
        self.dragged_rect_relations: list[relation.Relation] | None = None
        self.initial_begin_point: QPoint | None = None
        self.initial_end_point: QPoint | None = None
        self.cursor_offset_x: int | None = None
        self.cursor_offset_y: int | None = None
        self.prev_cursor_position: QPoint | None = None

    def startDragging(
        self,
        cursor_position: QPoint,
        dragged_rect: rectangle.Rectangle,
        relations: relation_collection.RelationCollection
    ):
        self.dragged_rect = dragged_rect

        self.initial_begin_point = QPoint(dragged_rect.begin)
        self.initial_end_point = QPoint(dragged_rect.end)

        self.prev_cursor_position = QPoint(cursor_position)
        self.cursor_offset_x = cursor_position.x() - dragged_rect.begin.x()
        self.cursor_offset_y = cursor_position.y() - dragged_rect.begin.y()

        self.dragged_rect_relations = relations.getRelationsByRectId(dragged_rect.id)

    def __moveRelations(self):
        if self.dragged_rect_relations is None:
            return

        for rel in self.dragged_rect_relations:
            rel.move()

    def drag(
        self,
        cursor_position: QPoint,
        rectangles: rectangle_collection.RectangleCollection,
        update
    ):
        if self.dragged_rect is None:
            return

        new_begin_x = cursor_position.x() - self.cursor_offset_x
        new_begin_y = cursor_position.y() - self.cursor_offset_y

        # Ограничиваем перемещение прямоугольников внутри границ сцены
        new_begin_x = max(
            0,
            min(
                new_begin_x,
                game_constants.WINDOW_WIDTH - component_constants.RECTANGLE_WIDTH
            )
        )
        new_begin_y = max(
            0,
            min(
                new_begin_y,
                game_constants.WINDOW_HEIGHT - component_constants.RECTANGLE_HEIGHT
            )
        )

        new_rect = QRect(
            new_begin_x,
            new_begin_y,
            component_constants.RECTANGLE_WIDTH,
            component_constants.RECTANGLE_HEIGHT
        )

        for rect in rectangles.getRectangles():
            if (
                rect.id != self.dragged_rect.id
                # Проверяем пересечение переносимого прямоугольника с каждым прямоугольником  из коллекции
                and new_rect.intersects(
                    QRect(
                        rect.begin.x(),
                        rect.begin.y(),
                        component_constants.RECTANGLE_WIDTH,
                        component_constants.RECTANGLE_HEIGHT
                    )
                )
            ):
                offset_x = 0
                offset_y = 0
                if new_begin_x < rect.begin.x():
                    offset_x = rect.begin.x() - (new_begin_x + component_constants.RECTANGLE_WIDTH)
                else:
                    offset_x = rect.end.x() - new_begin_x
                if new_begin_y < rect.begin.y():
                    offset_y = rect.begin.y() - (new_begin_y + component_constants.RECTANGLE_HEIGHT)
                else:
                    offset_y = rect.end.y() - new_begin_y

                # Смещаем прямоугольник по оси минимального пересечения
                # Смещаем вместе с ним курсор, чтобы перетаскиваемый прямоугольник упирался в другой
                if abs(offset_x) < abs(offset_y):
                    new_begin_x += offset_x
                    QCursor.setPos(QCursor.pos().x() + offset_x, QCursor.pos().y())
                else:
                    new_begin_y += offset_y
                    QCursor.setPos(QCursor.pos().x(), QCursor.pos().y() + offset_y)

                self.dragged_rect.begin.setX(new_begin_x)
                self.dragged_rect.begin.setY(new_begin_y)
                self.dragged_rect.end.setX(new_begin_x + component_constants.RECTANGLE_WIDTH)
                self.dragged_rect.end.setY(new_begin_y + component_constants.RECTANGLE_HEIGHT)

        self.dragged_rect.begin.setX(new_begin_x)
        self.dragged_rect.begin.setY(new_begin_y)
        self.dragged_rect.end.setX(new_begin_x + component_constants.RECTANGLE_WIDTH)
        self.dragged_rect.end.setY(new_begin_y + component_constants.RECTANGLE_HEIGHT)

        self.__moveRelations()

        self.prev_cursor_position = QPoint(cursor_position)

        update()


    def endDragging(self):
        self.dragged_rect = None
        self.initial_begin_point = None
        self.initial_end_point = None
        self.cursor_offset_x = None
        self.cursor_offset_y = None
        self.prev_cursor_position = None