




class Camera:
    def __init__(self,largeur,hauteur,position,direction,orientation,df):
        self.largeur=largeur
        self.hauteur=hauteur
        self.position=position
        self.direction=direction
        self.orientation=orientation
        self.df=df

    def rayon(self,x,y):
        ar= self.largeur/self.hauteur
        vw= 2*ar
        vwh=2
        x_normalized = (x - 0.5) * vw
        y_normalized = (y - 0.5) * vwh
        right = self.orientation.cross(self.direction).normalize()
        up = self.direction.cross(right).normalize()
        direction = (self.direction +
                     right * x_normalized +
                     up * y_normalized).normalize()

        # Calcul de l'origine du rayon
        origin = self.position

        return origin, direction