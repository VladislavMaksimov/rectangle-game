from PyQt6.QtCore import QPoint
from game.components import rectangle, relation, relation_collection

class RelationLogicController():
    def __init__(self):
        self.__relation_rect_start: rectangle.Rectangle | None = None

    def createRelation(self, clicked_rect: rectangle.Rectangle):
        if self.__relation_rect_start is None:
            self.__relation_rect_start = clicked_rect
            return
        
        if clicked_rect == self.__relation_rect_start:
            return

        created_rel = relation.Relation(
            self.__relation_rect_start,
            clicked_rect
        )

        self.__relation_rect_start = None
        return created_rel
    
    def removeRelation(
        self,
        clicked_point: QPoint,
        relations: relation_collection.RelationCollection,
    ):
        rel = relations.getRelationByPoint(clicked_point)
        if rel is None:
            return False
        
        relations.removeRelation(rel)
        return True