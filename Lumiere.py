
from point import Point
from Couleur import Couleur

class Lumiere:
    def __init__(self, name, pos:Point, clr:Couleur):
        self.name = name
        self.position = pos
        self.color = clr