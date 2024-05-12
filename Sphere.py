import math as m
import numpy as np
from couleur import Couleur
from droite import Droite
from objet import Objet
from point import Point
from vecteur import Vecteur, dotprod



class Sphere(Objet):   
    def __init__(self, pos:Point, r, clr:Couleur, amb=0, diff=0.7, spec=0.7, refl=0.3, shad=0):
        Objet.__init__(self, pos, clr, amb, diff, spec, refl, shad)
        self.radius = r

    def intersection(self, d:Droite):
        #  vecteur point droite -> sphere        
        CP = Vecteur(d.point.x-self.position.x, 
                     d.point.y-self.position.y,
                     d.point.z-self.position.z)

        #  calcul delta
        a, b, c = 1, 2*dotprod(d.vect, CP), dotprod(CP, CP)-self.radius*self.radius
        delta = (b*b)-(4*a*c)

        #print(delta)
        #  tests intersections
        if delta>0: #  deux intersections
            t = (-b-m.sqrt(delta))/2*a
            
        elif delta==0: #  une intersection
            t = (-b)/(2*a)
            if t<=0:
                return None
        else: #  pas d'intersection
            return None

        return d.get_point(t)
    
    def normalVect(self, p:Point):
        return Vecteur(p.x-self.position.x,
                       p.y-self.position.y,
                       p.z-self.position.z).normalize()


if __name__ == "__main__":
    S = Sphere(Point(0,0,0), 1, Couleur(1,1,1))
    print(S.normalVect(Point(1,0,0)).array)