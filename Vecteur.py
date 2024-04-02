import numpy as np


class Vecteur:
    def __init__(self,x,y,z):
        self.vector = np.array([x,y,z])

    def addition(self,vector1):
        return np.add(self.vector,vector1.vector)

    def soustraction(self,vector1):
        return np.subtract(self.vector,vector1.vector)

    def multiplication_scalaire(self,vector1):
        return np.multiply(self.vector,vector1.vector)

    def prod_scalaire(self,vector1):
        return np.dot(self.vector,vector1.vector)

    def prod_vectoriel(self,vector1):
        return np.cross(self.vector,vector1.vector)

    def norme(self):
        return np.linalg.norm(self.vector)

    def normalization(self):
        return

vect= Vecteur(1,2,3)
vect2= Vecteur(3,5,9)
print(vect.prod_scalaire(vect2))
