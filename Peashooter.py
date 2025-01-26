from OpenGL.GL import *
from Obj import *

class Peashooter(ObjRender):
    def __init__(self, x, y, z, r, g, b, hp, demage, cooldown):
        super().__init__(x, y, z, r, g, b)
        self.hp = hp
        self.demage = demage
        self.coolsdown = cooldown

    def Spawn(self):
        pass