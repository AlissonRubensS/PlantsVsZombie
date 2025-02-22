from OpenGL.GL import *
from Plants import *

class Potato(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "Potato"

    def render(self):
        # Cabo da planta
        self.RenderCube(1.5, 3, 1.5, 187, 105, 47)

    def getPos(self):
        return (self.x, self.y, self.z)