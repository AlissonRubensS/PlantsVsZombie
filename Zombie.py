from OpenGL.GL import *
from Obj import ObjRender
from Material import Material
import random
<<<<<<< HEAD

# Classe de material para armazenar coeficientes de iluminação
class Material:
    def __init__(self, ambiente, difuso, especular, brilho):
        self.coeficiente_ambiente = ambiente
        self.coeficiente_difuso = difuso
        self.coeficiente_especular = especular
        self.brilho = brilho
=======
>>>>>>> main

class Zombie(ObjRender):
    
    SpawnPositions = [
        ((0, 2, -40), (0, 2, 22)),
        ((5, 2, -40), (5, 2, 22)),
        ((10, 2, -40), (10, 2, 22)),
        ((15, 2, -40), (15, 2, 22))   
    ]

    def __init__(self, hp, damage, speed):
        (spawn_pos, target_pos) = random.choice(self.SpawnPositions)  # Sorteia spawn e destino
        super().__init__(*spawn_pos)
        self.hp = hp 
        self.damage = damage
        self.speed = speed
        self.target_x, self.target_y, self.target_z = target_pos

        # Criando um material para o zumbi (valores ajustáveis)
        self.material = Material(
<<<<<<< HEAD
            ambiente=(0.2, 0.2, 0.2, 1.0),
            difuso=(0.0, 0.5, 0.0, 1.0),  # Verde escuro
            especular=(0.3, 0.3, 0.3, 1.0),
            brilho=10
        )

    def spawn(self):
        """Renderiza o zumbi na cena"""

=======
            ambiente  = (0.2, 0.2, 0.2, 1.0),
            difuso    = (0.0, 0.5, 0.0, 1.0),  # Verde escuro
            especular = (0.3, 0.3, 0.3, 1.0),
            brilho    = 1
        )

    def render(self):
        """Renderiza o zumbi na cena"""

>>>>>>> main
        # Corpo do zumbi
        self.RenderCube(1, 1.5, 0.5, 0, 100, 0, self.material)

        # Cabeça do zumbi
        glPushMatrix()
        glTranslatef(0, 3.75, 0)  
        self.RenderCube(0.5, 0.5, 0.5, 0, 150, 0, self.material)
        glPopMatrix()

        # Braços
        for dx in [-1.25, 1.25]:
            glPushMatrix()
            glTranslatef(dx, 1, 0)
            self.RenderCube(0.3, 1, 0.3, 0, 100, 0, self.material)
            glPopMatrix()

        # Pernas
        for dx in [-0.5, 0.5]:
            glPushMatrix()
            glTranslatef(dx, -2, 0)
            self.RenderCube(0.3, 1.5, 0.3, 0, 100, 0, self.material)
            glPopMatrix()

    def move(self):
        """Movimenta o zumbi em direção ao alvo"""
        dx = self.target_x - self.x
        dz = self.target_z - self.z
<<<<<<< HEAD
        distancia_quadrado = dx * dx + dz * dz  # Evita sqrt()
=======
        distancia_quadrado = dx * dx + dz * dz
>>>>>>> main

        if distancia_quadrado > 0:
            inv_distancia = 1 / (distancia_quadrado ** 0.5)  # Normalização

            dx *= inv_distancia
            dz *= inv_distancia

            self.x += dx * self.speed
            self.z += dz * self.speed
