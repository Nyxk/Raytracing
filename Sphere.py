import Couleur 
from Objet import Objet 
import numpy as np

class Sphere(Objet):
    def __init__(self,direction,color,frd,frs,fdr,shadow,rayon):
        super().__init__(direction,color,frd,frs,fdr,shadow)
        self.rayon = rayon

    def intersection(self, rayon):
        # Implémentation de la méthode intersection pour une sphère
        # Retourne le point d'intersection le plus proche avec le rayon
        # Calculer les coefficients de l'équation quadratique pour l'intersection
        oc = rayon.origine - self.position
        a = np.dot(rayon.direction, rayon.direction)
        b = 2.0 * np.dot(oc, rayon.direction)
        c = np.dot(oc, oc) - self.rayon ** 2
        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return None  # Pas d'intersection

        # Trouver la plus petite racine positive de l'équation quadratique
        t = (-b - np.sqrt(discriminant)) / (2.0 * a)
        if t < 0:
            t = (-b + np.sqrt(discriminant)) / (2.0 * a)

        # Calculer le point d'intersection
        intersection_point = rayon.origine + t * rayon.direction
        return intersection_point

    def normale(self, point):
        # Implémentation de la méthode normale pour une sphère
        # Retourne la normale à la surface de la sphère au point donné
        return (point - self.position) / self.rayon