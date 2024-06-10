from PyQt6.QtCore import QPoint
from game.components import relation, rectangle

class RelationCollection:
    def __init__(self, initial_collection: list[relation.Relation] = []):
        self.__collection = initial_collection

    def getRelations(self):
        return self.__collection
    
    def getRelationsByRect(self, rect: rectangle.Rectangle):
        relations = []
        for rel in self.__collection:
            if rel.checkConnectRect(rect):
                relations.append(rel)
        return relations
    
    def getRelationByPoint(self, point: QPoint):
        for rel in self.__collection:
            if rel.checkPointOnRelation(point):
                return rel
        return None

    def __checkRelationExists(self, rel_check: relation.Relation):
        for rel in self.__collection:
            if rel_check == rel:
                return True
        return False
    
    def addRelation(self, rel: relation.Relation):
        relation_exists = self.__checkRelationExists(rel)
        if relation_exists:
            return False
        
        self.__collection.append(rel)
        return True

    def removeRelation(self, rel: relation.Relation):
        self.__collection.remove(rel)