from Vecteur import Vecteur
import numpy as np



class Camera:
    def __init__(self,largeur,hauteur,position,direction,orientation,df):
        self.largeur=largeur
        self.hauteur=hauteur
        self.position=position
        v1=Vecteur(self.position,direction)
        self.direction=v1.normalization() #VVect
        v2=Vecteur((0,0,0),(0,1,0))
        self.orientation=v2.normalization() #Hvect
        self.Dvect=self.direction.prod_vectoriel(self.orientation)
        self.df=df

    def ray(self,obj_pos):
        ray_vect= Vecteur(self.position,obj_pos)
        return ray_vect.normalization()


