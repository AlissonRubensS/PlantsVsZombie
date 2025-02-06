from Obj import *

class Plants(ObjRender):
    def __init__(self, x, y, z, hp, demage, cooldown):
        super().__init__(x, y, z)
        self.hp = hp
        self.demage = demage
        self.coolsdown = cooldown
