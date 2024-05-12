import math as m
import numpy as np

class Couleur:
    def __init__(self, r, v, b):
        self.r, self.v, self.b = r,v,b
    
    @property
    def array(self):
        return np.array((self.r, self.v, self.b))

    @property
    def norm(self):
        return m.sqrt(self.r*self.r+self.v*self.v+self.b*self.b)
    
    def __add__(self, clr):
        return Couleur(self.r+clr.r, self.v+clr.v, self.b+clr.b)
    
    def __mul__(self, clr):
        return Couleur(self.r*clr, self.v*clr, self.b*clr)
        
    def normalize(self):
        arr = self.array/self.norm
        return Couleur(arr[0], arr[1], arr[2])

def multcolor(A:Couleur, B:Couleur):
        return Couleur(A.r*B.r, A.v*B.v, A.b*B.b)

if __name__ == "__main__":
    VERT = Couleur(0.1,1,0)
    ROUGE = Couleur(1,0,0)
    print( (VERT+ROUGE).array)