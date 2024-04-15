import numpy as np


class Rayon:
    def __init__(self, origine, direction):
        self.origine = origine
        self.direction = direction / np.linalg.norm(direction)

