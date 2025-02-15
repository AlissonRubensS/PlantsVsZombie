from OpenGL.GL import *
from Plants import *

class Peashooter(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "Peashooter"

    def render(self):
        # Cabo da planta
        self.RenderCube(0.5, 3, 0.5, 187, 105, 47)

        # Cabaça da planta
        glPushMatrix()
        glTranslatef(0, 4.5, 0)
        self.RenderCube(1, 1, 1, 95, 235, 92)
        glPopMatrix()

    def getPos(self):
        return (self.x, self.y, self.z)