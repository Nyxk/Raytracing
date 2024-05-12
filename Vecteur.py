import math as m
import numpy as np


from point import Point


class Vecteur:
    def __init__(self, dx, dy, dz):
        self.dx, self.dy, self.dz = dx, dy, dz
    
    @property
    def array(self):
        return np.array((self.dx, self.dy, self.dz))
    
    @property
    def norm(self):
        return np.sqrt(self.dx*self.dx+self.dy*self.dy+self.dz*self.dz)
    
    def __add__(self, V):
        return Vecteur(self.dx+V.dx, self.dy+V.dy, self.dz+V.dz)
    
    def __sub__(self, V):
        return Vecteur(self.dx-V.dx, self.dy-V.dy, self.dz-V.dz)
    
    def __mul__(self, V):
        if isinstance(V, (float, int)):
            return Vecteur(self.dx*V, self.dy*V, self.dz*V)
        elif isinstance(V, Vecteur):
            return Vecteur(self.dy*V.dz-self.dz*V.dy,
                           self.dz*V.dx-self.dx*V.dz,
                           self.dx*V.dy-self.dy*V.dx)


    def __rmul__(self, val):
        return self * val
        
    def normalize(self):
        arr = self.array/self.norm
        return Vecteur(arr[0], arr[1], arr[2])
    

    def calcul_angle(self,vect_2):
        nomina = np.dot(self.array,vect_2.array)
        denomina = self.norm * vect_2.norm
        return np.degrees(np.arccos(nomina/denomina))

    


def dotprod(u:Vecteur, v:Vecteur):
    return u.dx*v.dx + u.dy*v.dy + u.dz*v.dz


if __name__ == "__main__":
    V = Vecteur(0,1/np.sqrt(2),1/np.sqrt(2))
    U = Vecteur(0,0,1)
    print(U.calcul_angle(V))

    


