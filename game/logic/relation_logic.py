from collections.abc import Callable
from game.components import rectangle, relation, relation_collection

class RelationLogicController():
    def __init__(self):
        self.relation_rect_start = None

    def createRelation(
        self,
        clicked_rect: rectangle.Rectangle,
        relations: relation_collection.RelationCollection,
        update: Callable[[], None]
    ):        
        if self.relation_rect_start is None:
            self.relation_rect_start = clicked_rect
            return
            
        if self.relation_rect_start.id == clicked_rect.id:
            self.relation_rect_start = None
            return
        
        rel = relation.Relation(self.relation_rect_start, clicked_rect)
        relations.addRelation(rel)
        self.relation_rect_start = None
        print(len(relations.collection))
        update()