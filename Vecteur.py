import numpy as np


class Vecteur:
    def __init__(self,origin,extremite): #x,y,z coords
        self.origin = origin 
        self.extremite = extremite
        vect = np.array([self.extremite[0]-self.origin[0],
                            self.extremite[1]-self.origin[1],
                            self.extremite[2]-self.origin[2]])
        self.vector= vect

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
        ori=(x_n,y_n,z_n)
        ze=(0,0,0)
        return Vecteur(ze,ori)
    
    
    