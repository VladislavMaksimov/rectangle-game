from PyQt6.QtGui import QPainter
from game.components import relation

class RelationCollection:
    def __init__(self, initial_collection: list[relation.Relation] = []):
        self.collection = initial_collection

    def getRelations(self):
        return self.collection

    def addRelation(self, rel: relation.Relation):
        self.collection.append(rel)

    def removeRelation(self, rel: relation.Relation):
        self.collection.remove(rel)

    def draw(self, painter: QPainter):
        for rel in self.collection:
            rel.draw(painter)