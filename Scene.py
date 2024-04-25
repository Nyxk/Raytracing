from PIL import Image
import numpy as np

from Couleur import Couleur 
from Camera import Camera
from Sphere import Sphere
from Objet import Objet 
from Lumiere import Lumiere
from Vecteur import Vecteur
class Scene:
    def __init__(self, camera, list_objs, list_light, lumiere_ambiente = 0, Image = None):

        self.camera = camera
        self.list_objs=list_objs
        self.list_light=list_light
        self.lumiere_ambiante = lumiere_ambiente
        self.Image = Image



    

if __name__ == "__main__":
    pos_cam=(0,0,5)
    largeur,hauteur=10,10
    look_at=(0,0,0)
    orient=(0,1,0)
    camy = Camera(largeur,hauteur,pos_cam, look_at, orient,-5)
    cyan = Couleur(0,255,255)
    pos_sphere = (0, 0, 0)
    pos_sphere2 = (3, 0, 0)
    reflexion_diffus = 0.8
    reflexion_speculaire = 0.2
    reflexion = 0.5
    ombre = True
    rayon = 4.0
    sphere_1= Sphere(pos_sphere,cyan,reflexion_diffus,
                     reflexion_speculaire,reflexion,ombre,rayon)
    sphere_2= Sphere(pos_sphere2,cyan,reflexion_diffus,
                     reflexion_speculaire,reflexion,ombre,rayon)
    
    lmny=Lumiere(0,0,-10,cyan)
    obj=[sphere_1,sphere_2]

    src_lumi=[lmny]




    def raycast(objet_scene,src_lum,cam,img_height,img_widht):
        img = np.zeros((img_widht, img_height, 3), dtype=np.uint8) # dimensions image
        dx, dy = cam.largeur/img_widht, cam.hauteur/img_height
        C= cam.position 
        h=cam.hauteur 
        l=cam.largeur 
        H, D = cam.orientation.vector, cam.Dvect # vecteurs camera
        print(cam.orientation.vector,cam.direction.vector)
        print(D)
        MAX_DIST= 20
        Phg = C+H*(h/2-dx/2)-D*(l/2-dx/2) # Point "origine" de la camera
        print(Phg)
        for y in range(len(img)):
            for x in range(len(img)):
                Pxy = Phg-H*(y*dy)+D*(x*dx)
                print(Pxy)
                #posxy=(x,y)
                i = MAX_DIST
                cam.ray()



    



    img_pix_x, img_pix_y = 600,600 
    imageMatrix = np.zeros((img_pix_x, img_pix_y, 3), dtype=np.uint8)
    raycast(obj,lmny,camy,img_pix_x, img_pix_y)



    img = Image.fromarray(imageMatrix) 
    img.show()



    





    #mainCamera = Camera()