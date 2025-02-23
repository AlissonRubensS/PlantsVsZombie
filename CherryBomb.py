# Importando bibliotecas
from OpenGL.GL import *
from time import time

# Importando classes
from Plants import Plants
from Material import Material

class CherryBomb(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "CherryBomb"

    def render(self):
        material = Material([0.01, 0.03, 0.01, 1.0],
                    [0.02, 0.06, 0.02, 1.0],  
                    [0.01, 0.01, 0.01, 1.0],  
                    0.01 )
        
        scale_size = time() - self.time_init

        glPushMatrix()
        glScalef(scale_size, scale_size, scale_size)
        self.RenderCube(0.5, 0.5, 0.5, 255, 0, 0, material)
        glPopMatrix()    

        glPushMatrix()
        glTranslatef(0.8, 0.8, 0.8)
        glScalef(scale_size, scale_size, scale_size)
        self.RenderCube(0.5, 0.5, 0.5, 255, 0, 0, material)
        glPopMatrix()    