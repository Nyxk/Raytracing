
from point import Point
from vecteur import Vecteur

class Droite:
    def __init__(self, pt:Point, v:Vecteur):
        self.point, self.vect = pt, v.normalize()
    
    def get_point(self, t):
        return Point(self.point.x + self.vect.dx*t,
                     self.point.y + self.vect.dy*t,
                     self.point.z + self.vect.dz*t)
