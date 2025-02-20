from OpenGL.GL import *
from Obj import ObjRender
import random
import math

class Zombie(ObjRender):
    
    SpawnPositions = [
        ((0, 2, -30), (0, 2, 22)),
        ((5, 2, -30), (5, 2, 22)),
        ((10, 2, -30), (10, 2, 22)),
        ((15, 2, -30), (15, 2, 22))   
    ]

    def __init__(self, hp, damage, speed):
        (spawn_pos, target_pos) = random.choice(self.SpawnPositions)  # Sorteia de onde nasce e para onde vai
        super().__init__(*spawn_pos)
        self.hp = hp 
        self.damage = damage
        self.speed = speed
        self.target_x, self.target_y, self.target_z = target_pos


    def spawn(self):
        # Corpo do zumbi
        self.RenderCube(1, 1.5, 0.5, 0, 100, 0)  # Corpo verde escuro

        # Cabeça do zumbi
        glPushMatrix()
        glTranslatef(0, 3.75, 0)  # Posiciona a cabeça acima do corpo
        self.RenderCube(0.5, 0.5, 0.5, 0, 150, 0)  # Cabeça verde mais claro
        glPopMatrix()

        # Braços do zumbi
        glPushMatrix()
        glTranslatef(-1.25, 1, 0)  # Braço esquerdo
        self.RenderCube(0.3, 1, 0.3, 0, 100, 0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1.25, 1, 0)  # Braço direito
        self.RenderCube(0.3, 1, 0.3, 0, 100, 0)
        glPopMatrix()

        # Pernas do zumbi
        glPushMatrix()
        glTranslatef(-0.5, -2, 0)  # Perna esquerda
        self.RenderCube(0.3, 1.5, 0.3, 0, 100, 0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.5, -2, 0)  # Perna direita
        self.RenderCube(0.3, 1.5, 0.3, 0, 100, 0)
        glPopMatrix()

    def move(self):
        # Calcula a direção do movimento
        dx = self.target_x - self.x
        dz = self.target_z - self.z
        distancia = math.sqrt(dx**2 + dz**2)

        if distancia > 0:  # Evita divisão por zero
            # Normaliza o vetor direção
            dx /= distancia
            dz /= distancia

            # Move o zumbi com velocidade constante
            self.x += dx * self.speed
            self.z += dz * self.speed