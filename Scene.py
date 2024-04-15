from PIL import Image
import numpy as np

from Couleur import Couleur 
from Camera import Camera
from Sphere import Sphere
from Objet import Objet 
from Lumiere import Lumiere
import Rayon
class Scene:
    def __init__(self, camera, list_objs, list_light, lumiere_ambiente = 0, Image = None):

        self.camera = camera
        self.list_objs=list_objs
        self.list_light=list_light
        self.lumiere_ambiante = lumiere_ambiente
        self.Image = Image



    

if __name__ == "__main__":
    pos_cam=(0,0,-10)
    camy = Camera((400,400),pos_cam,(0,0,0),(0,1,0),1)
    cyan = Couleur(0,255,255)
    x,y,z = 0, 0, 0
    reflexion_diffus = 0.8
    reflexion_speculaire = 0.2
    reflexion = 0.5
    ombre = True
    rayon = 40.0
    sphere_1= Sphere(x,y,z,cyan,reflexion_diffus,
                     reflexion_speculaire,reflexion,ombre,rayon)
    lmny=Lumiere(0,0,-10,cyan)
    obj=[sphere_1]
    src_lumi=[lmny]
    def generer_rayon_de_vue(position, x, y, largeur_image, hauteur_image):
        u = (x / largeur_image) * 2 - 1
        v = 1 - (y / hauteur_image) * 2
        direction_rayon = np.array([u, v, 0])
        origine_rayon = position
        return Rayon(origine_rayon, direction_rayon)



    def raycast(img,objet_scene,src_lum):
        MAX_DIST= 20
        for lingne in img:
            for colonne in img:
                i = MAX_DIST
                ray=generer_rayon_de_vue(camy.position,x,y,600,600)
                for obj in objet_scene:
                    a = obj.intersection(ray)
                    if i < a:
                        i = a
                if i != MAX_DIST:
                    obj.normale(i)
                    for lumi in src_lum:
                        l=(lumi.x,lumi.y,lumi.z)
                        generer_rayon_de_vue(i,l)







    img_pix_x, img_pix_y = 600,600 
    imageMatrix = np.zeros((img_pix_x, img_pix_y, 3), dtype=np.uint8)
    img = Image.fromarray(imageMatrix) 
    img.show()



    





    #mainCamera = Camera()