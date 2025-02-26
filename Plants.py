from Obj import *
from time import time

class Plants(ObjRender):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z)
        self.hp = hp
        self.demage = demage
        self.time_init = time()

    def apply_damage(self, zumbie, current_time, cooldown_demage):
        if current_time - self.time_init >= cooldown_demage:
            zumbie.hp -= self.demage
            self.time_init = current_time  # Atualiza o cooldown