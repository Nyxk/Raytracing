import numpy as np


class Couleur:
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b


    def sum(self,col):
        self.r += col.r
        self.g += col.g
        self.b += col.b

    def multiply(self,col):
        self.r *= col.r
        self.g *= col.g
        self.b *= col.b
