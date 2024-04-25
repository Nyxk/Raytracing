from Vecteur import Vecteur

class Ray(Vecteur):
    def __init__(self,p_coord,origin,extremite):
        super().__init__(origin,extremite)
        self.p_coord=p_coord