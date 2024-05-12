
from couleur import Couleur
from droite import Droite
from point import Point
from vecteur import Vecteur


class Objet:
    def __init__(self, pos:Point, clr:Couleur, amb=0.1, diff=0, spec=0, refl=0, shad=0):
        self.position = pos
        self.color = clr
        self.ambient = amb
        self.diffuse = diff
        self.specular = spec
        self.reflect = refl
        self.shadow = shad
    
    def intersection(self, d:Droite) -> Point:
        pass

    def normalVect(self, p:Point) -> Vecteur:
        pass

    
