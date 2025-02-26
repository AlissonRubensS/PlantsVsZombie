from OpenGL.GL import *
from Obj import ObjRender
from Material import Material
import random


class ZombieMini(ObjRender):
    SpawnPositions = [
        ((-15, 2, -38), (-15, 2, 22)),
        ((-10, 2, -40), (-10, 2, 22)),
        ((-5, 2, -37), (-5, 2, 22)),
        ((0, 2, -39), (0, 2, 22)),
        ((5, 2, -40), (5, 2, 22)),
        ((15, 2, -37), (10, 2, 22)),
        ((15, 2, -38), (15, 2, 22)),

    ]

    def __init__(self, hp, damage, speed):
        (spawn_pos, target_pos) = random.choice(self.SpawnPositions)  # Sorteia spawn e destino
        super().__init__(*spawn_pos)
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.target_x, self.target_y, self.target_z = target_pos
        self.cooldown = 0

        # Criando um material para o zumbi (valores ajustáveis)
        self.material = Material(
            ambiente=(0.2, 0.2, 0.2, 1.0),
            difuso=(0.0, 0.5, 0.0, 1.0),  # Verde escuro
            especular=(0.3, 0.3, 0.3, 1.0),
            brilho=1
        )

    def render(self):
        """Renderiza o zumbi na cena"""

        # Corpo do zumbi mini
        self.RenderCube(0.5, 0.75, 0.25, 150, 0, 0, self.material, 0)

        # Cabeça do zumbi mini
        glPushMatrix()
        glTranslatef(0, 1.875, 0)  
        self.RenderCube(0.25, 0.25, 0.25, 150, 0, 0, self.material, 0)
        glPopMatrix()

        # Braços do zumbi mini
        for dx in [-0.625, 0.625]:
            glPushMatrix()
            glTranslatef(dx, 0.5, 0)
            self.RenderCube(0.15, 0.5, 0.15, 150, 0, 0, self.material, 0)
            glPopMatrix()

        # Pernas do zumbi mini
        for dx in [-0.25, 0.25]:
            glPushMatrix()
            glTranslatef(dx, -1, 0)
            self.RenderCube(0.15, 0.75, 0.15, 150, 0, 0, self.material, 0)
            glPopMatrix()


    def move(self):
        """Movimenta o zumbi em direção ao alvo"""
        dx = self.target_x - self.x
        dz = self.target_z - self.z
        distancia_quadrado = dx * dx + dz * dz

        if distancia_quadrado > 0:
            inv_distancia = 1 / (distancia_quadrado ** 0.5)  # Normalização

            dx *= inv_distancia
            dz *= inv_distancia

            self.x += dx * self.speed
            self.z += dz * self.speed