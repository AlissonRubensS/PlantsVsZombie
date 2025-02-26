from OpenGL.GL import *


#importando classes
from Plants import Plants
from Material import Material

class HerbThorn(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "HerbThorn"
        

    def render(self):
        material =  Material([0.01, 0.03, 0.01, 1.0],
                    [0.02, 0.06, 0.02, 1.0],
                    [0.01, 0.01, 0.01, 1.0],
                    0.01 )


        self.RenderCube(1.5, 0.3, 1.5, 153, 76, 0, material, 0)

