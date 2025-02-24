from OpenGL.GL import *
from Obj import *
from Material import Material
import time

class Shoot(ObjRender):
    def __init__(self, x, y, z, demage):
        super().__init__(x, y, z)
        self.demage = demage
        self.veloc = 5
        self.start_time = time.time()

    def render(self):
        material = Material([0.01, 0.03, 0.01, 1.0],
                            [0.02, 0.06, 0.02, 1.0],  
                            [0.01, 0.01, 0.01, 1.0],  
                            0.01 )

        self.z = -1 *(time.time() - self.start_time) * self.veloc
        self.RenderCube(0.3, 0.3, 0.3, 150, 75, 0, material)