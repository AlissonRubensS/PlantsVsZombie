from Plants import Plants
from OpenGL.GL import *
from time import time

class CherryBomb(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "CherryBomb"

    def render(self):
        scale_size = time() - self.time_init

        glPushMatrix()
        glScalef(scale_size, scale_size, scale_size)
        self.RenderCube(0.5, 0.5, 0.5, 255, 0, 0)
        glPopMatrix()    

        glPushMatrix()
        glTranslatef(0.8, 0.8, 0.8)
        glScalef(scale_size, scale_size, scale_size)
        self.RenderCube(0.5, 0.5, 0.5, 255, 0, 0)
        glPopMatrix()    