from PyQt6.QtCore import QPoint
from PyQt6.QtGui import QPainter
from game.components import relation

class RelationCollection:
    def __init__(self, initial_collection: list[relation.Relation] = []):
        self.collection = initial_collection

    def getRelations(self):
        return self.collection
    
    def getRelationByPoint(self, point: QPoint):
        for rel in self.collection:
            if rel.checkPointOnRelation(point):
                return rel
        return None

    def checkRelationExists(self, rel_checked: relation.Relation):
        for rel in self.collection:
            if ((
                    rel.rect_start.id == rel_checked.rect_start.id
                    and rel.rect_end.id == rel_checked.rect_end.id
                )
                or (
                    rel.rect_start.id == rel_checked.rect_end.id
                    and rel.rect_end.id == rel_checked.rect_start.id
                )
            ):
                return True
        return False

    def addRelation(self, rel: relation.Relation):
        relation_exists = self.checkRelationExists(rel)
        if relation_exists:
            return
        self.collection.append(rel)

    def removeRelation(self, rel: relation.Relation):
        self.collection.remove(rel)

    def draw(self, painter: QPainter):
        for rel in self.collection:
            rel.draw(painter)