from OpenGL.GL import *
from Obj import *

class Peashooter(ObjRender):
    def __init__(self, x, y, z, hp, demage, cooldown):
        super().__init__(x, y, z)
        self.hp = hp
        self.demage = demage
        self.coolsdown = cooldown

    def Spawn(self):
        # Cabo da planta
        self.RenderCube(0.5, 3, 0.5, 187, 105, 47)

        # Cabaça da planta
        glPushMatrix()
        glTranslatef(0, 4.5, 0)
        self.RenderCube(1, 1, 1, 95, 235, 92)
        glPopMatrix()

    def Shooter(self):
        shoot = ObjRender(self.x, self.y, self.z)
        shoot.RenderCircle(30, 30, 1)
        return shoot