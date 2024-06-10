from collections import namedtuple
from collections.abc import Callable
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import QPoint
from game.components import rectangle, relation, relation_collection, rectangle_collection

class DragDropRectLogicController:
    def __init__(self):
        self.__dragged_rect: rectangle.Rectangle | None = None
        self.__dragged_rect_relations: list[relation.Relation] | None = None
        self.__prev_cursor_pos: QPoint | None = None

    # Меняем координаты связей после переноса прямоугольника
    def __moveRelations(self):
        for rel in self.__dragged_rect_relations:
            rel.move()

    # Находим отступ от коллизии
    def __getDragOffset(
        self,
        initial_top_left: QPoint,
        intersected_rect: rectangle.Rectangle
    ):
        offset_x = 0
        offset_y = 0

        if initial_top_left.x() < intersected_rect.topLeft().x():
            offset_x = intersected_rect.topLeft().x() - (initial_top_left.x() + self.__dragged_rect.width())
        else:
            offset_x = intersected_rect.bottomRight().x() - initial_top_left.x()

        if initial_top_left.y() < intersected_rect.topLeft().y():
            offset_y = intersected_rect.topLeft().y() - (initial_top_left.y() + self.__dragged_rect.height())
        else:
            offset_y = intersected_rect.bottomRight().y() - initial_top_left.y()

        Offset = namedtuple('Offset', ['x', 'y'])
        return Offset(offset_x, offset_y)

    def startDragging(
        self,
        cursor_position: QPoint,
        rectangles: rectangle_collection.RectangleCollection,
        relations: relation_collection.RelationCollection
    ):
        self.__dragged_rect = rectangles.getRectangleByPoint(cursor_position)
        if self.__dragged_rect is None:
            return
        self.__dragged_rect_relations = relations.getRelationsByRect(self.__dragged_rect)
        self.__dragged_rect.startDragging(cursor_position)

    def drag(
        self,
        to_point: QPoint,
        rectangles: rectangle_collection.RectangleCollection,
        checkRectOutOfBounds: Callable[[rectangle.Rectangle], bool],
        field_width: int,
        field_height: int,
    ):
        if self.__dragged_rect is None:
            return False
                
        initial_top_left = QPoint(self.__dragged_rect.topLeft())
        self.__dragged_rect.drag(to_point)

        if checkRectOutOfBounds(self.__dragged_rect):
            new_top_left_x = max(
                0,
                min(
                    self.__dragged_rect.topLeft().x(),
                    field_width - self.__dragged_rect.width()
                )
            )
            new_top_left_y = max(
                0,
                min(
                    self.__dragged_rect.topLeft().y(),
                    field_height - self.__dragged_rect.height()
                )
            )
            new_top_left = QPoint(new_top_left_x, new_top_left_y)

            # Делаем так, чтобы прямоугольник упирался в границу
            self.__dragged_rect.drag(
                new_top_left + self.__dragged_rect.dragOffset()
            )

            # Держим курсор на месте
            if self.__prev_cursor_pos:
                QCursor.setPos(self.__prev_cursor_pos)

        # Проверяем пересечение переносимого прямоугольника с каждым прямоугольником  из коллекции
        for rect in rectangles.getRectangles():
            if self.__dragged_rect != rect and self.__dragged_rect.intersects(rect):
                drag_offset = self.__getDragOffset(
                    initial_top_left,
                    rect
                )

                # Смещаем прямоугольник по оси минимального пересечения
                if (abs(drag_offset.x) < abs(drag_offset.y)):
                    new_top_left = QPoint(
                        initial_top_left.x() + drag_offset.x,
                        initial_top_left.y()
                    )
                else:
                    new_top_left = QPoint(
                        initial_top_left.x(),
                        initial_top_left.y() + drag_offset.y
                    )

                # Держим курсор на месте, чтобы нельзя было "перескочить" через коллизию
                if self.__prev_cursor_pos:
                    QCursor.setPos(self.__prev_cursor_pos)

                # Делаем так, чтобы прямоугольник упирался в коллизию
                self.__dragged_rect.drag(
                    new_top_left + self.__dragged_rect.dragOffset()
                )

                self.__moveRelations()
                self.__prev_cursor_pos = QPoint(QCursor.pos())

                return True

        self.__moveRelations()

        self.__prev_cursor_pos = QPoint(QCursor.pos())
        return True

    def stopDragging(self):
        if self.__dragged_rect is None:
            return
        
        self.__dragged_rect.stopDragging()
        self.__dragged_rect = None
        self.__dragged_rect_relations = None