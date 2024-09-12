
from Couleur import Couleur
from droite import Droite
from Objet import Objet
from point import Point
from Vecteur import Vecteur

class Plan(Objet):
    def __init__(self, pos:Point, v:Vecteur, clr:Couleur, amb=0.1, diff=0, spec=0, refl=0, shad=0):
        Objet.__init__(self, pos, clr, amb, diff, spec, refl, shad)
        self.normal = v.normalize()

    def intersection(self, d:Droite):
        x, y, z = self.position.x, self.position.y, self.position.z #point du plan
        x1, y1, z1 = d.point.x, d.point.y, d.point.z # origine droite (focal ou pt ecran)
        A, B, C = self.normal.dx, self.normal.dy, self.normal.dz # vecteur normal plan
        D = -1*(A*x+B*y+C*z)
        i, j, k = d.vect.dx, d.vect.dy, d.vect.dz #vecteur dir droite
        
        t = -1*((A*x1+B*y1+C*z1+D)/(A*i+B*j+C*k))

        if t>0:
            return d.get_point(t)
        else:
            return None
    
    def normalVect(self, p:Point):
        return self.normal
        
if __name__ == "__main__":
    d = Droite(Point(3,0,0), Vecteur(-1,-1,0))
    p = Plan(Point(0,0,0), Vecteur(1,0,0), Couleur(1,1,1))

    print(p.intersection(d).array)
        

