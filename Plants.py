from Obj import *
import time

class Plants(ObjRender):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z)
        self.hp = hp
        self.demage = demage
        self.time_init = time.time()
