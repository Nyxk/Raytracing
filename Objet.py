import numpy as np


class Objet:
    def __init__(self,position,color,frd,frs,fdr,shadow):
        self.position =position 
        self.color = color
        self.frd = frd #facteur de réflexion diffus
        self.frs = frs #facteur de réflexion spéculaire
        self.fdr = fdr #facteur de réflexion (reflets)
        self.shadow = shadow

    def intersection(self,droite,camera):
        pass
    def normale(self):
        pass
