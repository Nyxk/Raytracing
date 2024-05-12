
import numpy as np
import math as m

from camera import Camera
from couleur import Couleur, multcolor
from droite import Droite
from lumiere import Lumiere
from objet import Objet
from plan import Plan
from point import Point
from sphere import Sphere
from vecteur import Vecteur, dotprod


"""
def calc_spec(cam:Point,spek):
        #Vecteur de lumiere I 
        L_i = Point(0.9,0.1,0.1).array
        #Vecteur V(vue)
        V_normalized = Vecteur(0,0,-1).array
        #R = (np.dot(2 * (np.dot(-I,N)),N)+I)
        R_normalized = Vecteur(0,1,0).array
        comp_spec =  np.power(np.dot(R_normalized,V_normalized),100)
        return comp_spec

"""



def rayon_refracted(n1,n2):
        I = Vecteur(0,0,1)
        N=  Vecteur(0,1/np.sqrt(2),1/np.sqrt(2))
        th_i = N.calcul_angle(I)
        n_div = (n1 / n2)
        th_p = n_div * np.sin(np.deg2rad(th_i))
        th_p = np.rad2deg(np.arcsin(th_p))
        X = np.dot((n1 * np.cos(np.deg2rad(th_i)) -n2 * np.cos(np.deg2rad(th_p))),N.array)
        I = Vecteur(0,0,-1)
        R= n_div * (I.array + X)
        return R



a=Vecteur(0,1,3).array
b=Vecteur(4,0,1).array
print(np.dot(a,b))


def Lancer_ray(self,rayon,depth): 
        if depth >= 3:
            return self.background
        else:
            I=None
            for obj in self.listObj:
                tmp = obj.intersection(rayon) # intersection avec l'objet
                if tmp != None:
                    if I==None or tmp.z>I[0].z:
                        I=(tmp,obj)
            if I is not None:
                P,obj=I[0],I[1]
                pxColor = self.background
                #N normal au point de la surface
                N = obj.normalVect(P)
                #L = Vecteur(point_lum.x-point_intersect.x,
                        #point_lum.y-point_intersect.y,
                        #point_lum.z-point_intersect.z).array
                
                #speculaire = self.calc_spec(obj,self.listLight[0].position,P,N)
                Ia=np.array([1,0,0])
                k_a=0.7
                amb = self.ambiant(obj.color,Ia,k_a)
                #Rr = Droite(P,speculaire[1])
                #kr=obj.reflect
                #Cr=self.Lancer_ray(Rr,depth+1) * kr 
                n1=1
                kt= 1.52
                #Rt=self.rayon_refracted(self.listLight[0],P,N,n1,kt)
                #Ct = self.Lancer_ray(Rt,depth=depth+1)
                Cd=self.background
                for Lumiere in self.listLight:
                    L = Vecteur(Lumiere.position.x-P.x,
                                Lumiere.position.y-P.y,
                                Lumiere.position.z-P.z)
                    
                    for obj in self.listObj:
                        vect_pl=Vecteur(Lumiere.position.x - P.x,
                                    Lumiere.position.y - P.y,
                                    Lumiere.position.z - P.z).normalize()
                        Rd = Droite(P,vect_pl)
                        inter_o = obj.intersection(Rd)
                        if inter_o is None:
                            Cd= Cd.__add__(self.calc_diffuse(obj,Lumiere.position,P,N,L.normalize().array))
                Ca=self.ambiant(obj.color,np.array((0.7,0.7,0.7)),0.2)
                Phong= Ca.__add__(Cd)
                return Phong