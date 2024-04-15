import numpy as np


class Objet:
    def __init__(self,direction,color,frd,frs,fdr,shadow):
        self.direction =direction 
        self.color = color
        self.frd = frd #facteur de réflexion diffus
        self.frs = frs #facteur de réflexion spéculaire
        self.fdr = fdr #facteur de réflexion (reflets)
        self.shadow = shadow

    def intersection(self,droite,camera):
        pass
    def normale(self):
        pass
