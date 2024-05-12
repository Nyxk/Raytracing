import numpy as np

class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x,y,z

    @property
    def array(self):
        return np.array((self.x, self.y, self.z))
    
    def __add__(self, V):
        return Point(self.x+V.dx, self.y+V.dy, self.z+V.dz)
    
    def __sub__(self, V):
        return Point(self.x-V.dx, self.y-V.dy, self.z-V.dz)
    
    