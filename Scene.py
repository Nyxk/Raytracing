
import numpy as np
import math as m
import time 
from camera import Camera
from couleur import Couleur, multcolor
from droite import Droite
from lumiere import Lumiere
from objet import Objet
from plan import Plan
from point import Point
from sphere import Sphere
from vecteur import Vecteur, dotprod

from PIL import Image



BLACK  = Couleur(0,0,0)
class Scene:
    def __init__(self, cam:Camera, listObj: list[Objet], listLight: list[Lumiere], bgcolor=BLACK):
        self.camera = cam
        self.listObj = listObj
        self.listLight = listLight
        self.background = bgcolor

    def create_image(self, imageW, imageH):
        # INIT IMAGE A FAIRE ---------
        image = np.zeros((imageH, imageW, 3), dtype=np.uint8)
        # ----------------------------

        nbLights = len(self.listLight)

        #  parcours de l'image
        for i in range(imageW):
            #print((i/imageW)*100)
            for j in range(imageH):
                ray = self.camera.ray(self.camera.get_point(i, j, imageW, imageH)) # rayon de vue
                I = None # init intersection

                # parcours des objets 
                for obj in self.listObj:
                    tmp = obj.intersection(ray) # intersection avec l'objet
                    # si intersection
                    if tmp!=None:
                        # si aucune intersection enregistree ou si intersection plus proche
                        if I==None or tmp.z>I[0].z:
                            I = (tmp, obj) # (intersection, objet)

                pxColor = self.background # init couleur de fond
                
                if I!=None:
                    # point d'intersection, objet
                    p, obj = I[0], I[1]
                    lum = 0 # "quantité de lumiere au point"
                    N = obj.normalVect(p) # vecteur normal
                    print(N.array)
                    #speculaire = self.calc_spec(obj,self.listLight[0].position,p,N)
                    # pour chaque lumiere
                    for l in self.listLight:
                        # vecteur intersection->lumiere
                        L = Vecteur(l.position.x-p.x,
                                    l.position.y-p.y,
                                    l.position.z-p.z).normalize()
                        # droite vecteur lumiere
                        shadowray = Droite(p+N*0.0001, L)
                        shadow = False # bool ombre
                        # pour chaque objet
                        for O in self.listObj:
                            if O.intersection(shadowray)!=None: # si intersection
                                shadow = True #lumiere l cachée
                        # Si lumiere pas cachée
                        if shadow==False:
                            # ajout intensité lumineuse
                            lum += max(dotprod(L, N), 0)*(1/nbLights)
                        # PAS DE SINON CAR +0 donc omis

                        """o, Ia = obj.color, Couleur(1,1,1)
                        kd, ka, ks = 0.1, obj.ambient, 0.7
                        I = ray.vect
                        R = 2*dotprod(I*-1, N)*N + I
                        #print(R.array)
                        n = 100"""

                    R = 2*dotprod(ray.vect*-1, N)*N + ray.vect

                    pxColor = (obj.color*lum)


                #print(pxColor.array)
                image[i, j] = (pxColor.r*255, pxColor.v*255, pxColor.b*255)



                """# si rayon de vue intersecte un objet
                if I!=None:
                    # intersection, objet intersecté
                    p, obj, l= I[0], I[1], self.listLight[0]
                    L = Vecteur(l.position.x-p.x,
                                l.position.y-p.y,
                                l.position.z-p.z).normalize()
                    N = obj.normalVect(p)
                    lightRay = Droite(p+N*0.00001, L)

                    shadow = False
                    for O in self.listObj:
                        if O.intersection(lightRay)!=None:
                            shadow = True
                    
                    if shadow:
                        image[i,j] = (0,0,0)
                    else:
                        Io, Ia = obj.color, Couleur(1,1,1)
                        kd, ka, ks = 0.1, obj.ambient, 0.7
                        I = ray.vect
                        R = 2*dotprod(I*-1, N)*N + I
                        #print(R.array)
                        n = 100

                        pxColor = Io*max(dotprod(L, N),0) + Io*(ks*(dotprod(R, ray.vect)**100))

                        image[i, j] = (pxColor.r*255, pxColor.v*255, pxColor.b*255)"""

        image = Image.fromarray(image)
        image.save("image_.png")



    def calc_spec(self,obj:Sphere,point_intersect:Point,N:Vecteur,L:Vecteur,Ii):
        #Vecteur de lumiere I(vecteur directeur I) plus tard devient paramettre 
        #Vecteur V(vue)
        N= N.array
        V_normalized = Vecteur(point_intersect.x-self.camera.position.x,
                    point_intersect.y-self.camera.position.y,
                    point_intersect.z-self.camera.position.z).normalize()
        #Vecteur R
        R = (np.dot(2 * (np.dot(-V_normalized.array,-N)),-N)+V_normalized.array)
        R_normalized = Vecteur(R[0],R[1],R[2]).normalize()
        #resultat final a multiplier par Ii
        comp_spec = Ii *obj.specular * np.power(np.dot(R_normalized.array,V_normalized.array),50)
        return Couleur(comp_spec[0],comp_spec[1],comp_spec[2]),R_normalized
    
        

    #N vecteur surface normalized
    def calc_diffuse(self,obj:Sphere,N:Vecteur,L:Vecteur,Ii:Couleur):
        L_prod_N = np.maximum(np.dot(N.array,L.normalize().array),0)
        kd=obj.diffuse
        comp_diffuse =  Ii * kd * L_prod_N 
        return Couleur(comp_diffuse[0],comp_diffuse[1],comp_diffuse[2]) 
    

    def ambiant(self,I_obj:Couleur,I_a:Couleur,k_a):
        amb = I_a * k_a * I_obj.array
        return Couleur(amb[0],amb[1],amb[2])



    #point lum: point ou la lumiere se situe, N: normale au point de la surface
    # n1 indice propagation du milieu,n2 indice propagation du milieu
    def rayon_refracted(self,point_lum:Point,point_intersect:Point,N,n1,n2):
        I = Vecteur(point_lum.x-point_intersect.x,
                    point_lum.y-point_intersect.y,
                    point_lum.z-point_intersect.z) 
        th_i = N.calcul_angle(I)
        n_div = (n1 / n2)
        th_p = n_div * np.sin(np.deg2rad(th_i))
        th_p = np.rad2deg(np.arcsin(th_p))
        X = np.dot((n1 * np.cos(np.deg2rad(th_i)) -n2 * np.cos(np.deg2rad(th_p))),N.array)
        I = Vecteur(point_intersect.x-point_lum.x,
                    point_intersect.y-point_lum.y,
                    point_intersect.z-point_lum.z)
        R= n_div * (I.array + X)
        return R
    
     
    def Lancer_ray(self,rayon,depth): 
        nbLights = len(self.listLight)
        lum=0
        Ii=np.array([0.7,0.7,0.7])
        if depth >= 2:
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
                N = obj.normalVect(P)
                L = Vecteur(self.listLight[0].position.x-P.x,
                            self.listLight[0].position.y-P.y,
                            self.listLight[0].position.z-P.z)
                
                Cs,R =  self.calc_spec(obj,P+0.0001*N,N,L,Ii)
                Ia=np.array([0.7,0.7,0.7])
                k_a=0.7
                Rr = Droite(P+0.0001*N,R)
                kr=obj.reflect
                Cr= self.Lancer_ray(Rr,depth+1)
                if Cr is None:
                    Cr=self.background
                n1=1
                kt= 1.52
                #Rt=self.rayon_refracted(self.listLight[0],P,N,n1,kt)
                #Ct = self.Lancer_ray(Rt,depth+1)
                Cd=self.background
                for Lumiere in self.listLight:
                    L = Vecteur(Lumiere.position.x-P.x,
                                    Lumiere.position.y-P.y,
                                    Lumiere.position.z-P.z).normalize()
                        #speculaire = self.calc_spec(obj,Lumiere.position,P,N,L)
                    shadowray = Droite(P+0.0001*N, L)
                    shadow = False # bool ombre
                    for O in self.listObj:
                        if O.intersection(shadowray)!=None: # si intersection
                                shadow = True #lumiere l cachée
                        # Si lumiere pas cachée
                        if shadow==False:
                            # ajout intensité lumineuse
                            lum += max(dotprod(L, N), 0)*(1/nbLights)
                    Rd = Droite(P,L)
                    inter_o = obj.intersection(Rd)
                    #COMP DIFFUSE 
                    Cd= Cd + self.calc_diffuse(obj,N,L,Ii)
                #LUMIERE AMB 
                Ca=self.ambiant(obj.color,Ia,0.7) 
                Phong=   (Cd.array + Ca.array + Cs.array + Cr.array*0.4)*lum#+ Ct.array)
                Phong= np.clip(Phong,0,1) 
                return Couleur(Phong[0],Phong[1],Phong[2])
                #return Couleur(coul[0],coul[1],coul[2])
        

    def Gen_img_rec(self, imageW, imageH):
        image = np.zeros((imageH, imageW, 3), dtype=np.uint8)
        #print(imageW)
        C=self.camera.position
        h=self.camera.height
        l=self.camera.width
        H=self.camera.Hvect
        D=self.camera.Dvect
        V=self.camera.viewVect
        dx, dy = l/imageW, h/imageH
        Phg = C+H*(h/2-dy/2)-D*(l/2-dx/2) # Point "origine" de la camera
        start_time = time.time()
        for i in range(imageH):
            #print((i/imageW)*100)
            for j in range(imageW):
                Pxy = Phg-H*(j*dy)+D*(i*dx)
                ray=self.camera.ray(Pxy)#self.camera.get_point(i,j,imageW,imageH))
                p=self.Lancer_ray(ray,0)
                if p is None:
                    image[i, j] = (self.background.r,self.background.v,self.background.b)   
                else:
                    image[i, j] = (p.r*255, p.v*255, p.b*255)
        image = Image.fromarray(image)
        image.save("image_.png")
        print(time.time()-start_time)


    def reflected(self, r:Droite, p:Point, obj:Objet, n):
        angle = m.acos( (dotprod(r.vect*-1, obj.normalVect(p))) / (r.vect.norm*obj.normalVect(p).norm) )*(180/m.pi)
        print(angle)


if __name__ == "__main__":

    cam = Camera(Point(0,0,5), 10,10, Point(0,0,0), 5)
    #LEFT HAND 
    S1 = Sphere(Point(-20,0,0), 2, Couleur(1,0,0))
    S2 = Sphere(Point(-4,0,0), 2, Couleur(0,1,0)) 
    S3 = Sphere(Point(4,0,0), 3, Couleur(0,0,1))
    S4 = Sphere(Point(0,0,-3), 2, Couleur(0,1,1)) 

    P1 = Plan(Point(0,-5,0), Vecteur(0,1,0), Couleur(1,1,1))

    L0 = Lumiere("L0", Point(0,0,10), Couleur(1,1,1))
    L1 = Lumiere("L1", Point(-10,0,20), Couleur(1,1,1))
    L2 = Lumiere("L2", Point(10,0,20), Couleur(1,1,1))

    cam = Camera(Point(0,3,10), 5,5, Point(0,0,0), 5)

    main = Scene(cam, [S1,S3,S2,S4,P1], [L1])
    main.Gen_img_rec(1024,1024)
    #main.create_image(256,256)

    #print("S1", S1)
    #print("S2", S2)

                

        




