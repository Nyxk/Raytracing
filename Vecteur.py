import numpy as np


class Vecteur:
    def __init__(self,origin,extremite): #x,y,z coords
        self.origin = origin 
        self.extremite = extremite
        self.vector = np.array([extremite[0]-origin[0],
                                extremite[1]-origin[1],
                                extremite[2]-origin[2]])

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
        norm = self.norme()
        x_n, y_n, z_n = self.vector[0] / norm,self.vector[1] / norm,self.vector[2] / norm
        return Vecteur(x_n,y_n,z_n)
