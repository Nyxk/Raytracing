
from droite import Droite
from point import Point
from vecteur import Vecteur


class Camera:
    def __init__(self, pos:Point, w, h, lookat:Point, fdist, ):
        self.position = pos
        self.width, self.height = w, h  

        self.viewVect = Vecteur(lookat.x-self.position.x,
                                lookat.y-self.position.y,
                                lookat.z-self.position.z).normalize()
        
        self.Fpoint = Point(self.position.x-self.viewVect.dx*fdist,
                            self.position.y-self.viewVect.dy*fdist,
                            self.position.z-self.viewVect.dz*fdist)
        
        self.Hvect = Vecteur(1,0,0)
        self.Dvect = (self.viewVect*self.Hvect).normalize()

    def ray(self, p:Point):
        return Droite(p, Vecteur(p.x-self.Fpoint.x,
                                 p.y-self.Fpoint.y,
                                 p.z-self.Fpoint.z).normalize())
    
    def get_point(self, x, y, screenW, screenH):
        pxX, pxY = self.width/screenW, self.height/screenH
        Phg = self.position.array + self.Hvect.array*(self.height/2 - pxY/2) - self.Dvect.array*(self.width/2 - pxX/2)
        Pxy = Phg - self.Hvect.array*(y*pxY) + self.Dvect.array*(x*pxX)
        
        return Point(Pxy[0], Pxy[1], Pxy[2])

if __name__ == "__main__":
    c = Camera(Point(0,0,5), 10,10, Point(0,0,0), 1)
    print(c.Fpoint.array)
    for i in range(10):
        for j in range(10):
            print(c.get_point(i, j, 10,10).array)



