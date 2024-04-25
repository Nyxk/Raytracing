from Couleur import Couleur
from Objet import Objet 
import numpy as np
from Vecteur import Vecteur
from Camera import Camera
from Ray import Ray

class Sphere(Objet):
    def __init__(self,position,color,frd,frs,fdr,shadow,rayon):
        super().__init__(position,color,frd,frs,fdr,shadow)
        self.rayon = rayon


    def intersection(self, ray:Ray):
        oc = Vecteur(ray.origin,self.position)
        ac=oc.vector
        A = 1
        B = 2.0 * (np.dot(ray.vector,ac))
        C = np.dot(ac, ac) - self.rayon ** 2
        delta = (B ** 2) - (4 * A * C)
        #2 solutions
        if delta > 0:
        # Trouver la plus petite racine positive de l'équation quadratique
            t1 = (-B - np.sqrt(delta)) / (2.0 * A)
            t2 = (-B + np.sqrt(delta)) / (2.0 * A)
            if t1 > 0 and t2 <=0 :
                t = t1
            elif t2 > 0 and t1 <0:
                t = t2
            elif t1 <= 0 and t2 <= 0:
                return None
            else:
                t=min(t1,t2)
        #Une seule solution/droite tangente au cercle 
        elif delta == 0: 
            t = (-B)/(2*A)
        #Aucune solution
        else:
            return 1
        # Calculer le point d'intersection et le renvoyer
        return ray.origin + t * ray.extremite
    

    def normale(self, point):
        # Implémentation de la méthode normale pour une sphère
        # Retourne la normale à la surface de la sphère au point donné
        return (point - self.position) / self.rayon
    

pos_cam=(0,0,5)
largeur,hauteur=10,10
look_at=(0,0,0)
orient=(0,1,0)
camy = Camera(largeur,hauteur,pos_cam, look_at, orient,-5)
print(camy.largeur,camy.hauteur,camy.position,camy.direction.vector,camy.orientation.vector,camy.df)
