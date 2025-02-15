from OpenGL.GL import *
from Obj import *
import time

class Shoot(ObjRender):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.veloc = 2
        self.start_time = time.time()

    def render(self):
        glPushMatrix()
        z_position = (time.time() - self.start_time) * self.veloc
        glTranslatef(0, 4, -z_position)
        self.RenderCube(0.3, 0.3, 0.3, 0, 0, 0)

        glPopMatrix()