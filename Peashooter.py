from OpenGL.GL import *
from Plants import *
from Material import Material

class Peashooter(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "Peashooter"

    def render(self):
        # Cabo da planta
        wood_material = Material([0.2, 0.15, 0.1, 1.0],    # Ambiente (marrom escuro)
                                 [0.4, 0.3, 0.2, 1.0],     # Difusa (marrom médio)
                                 [0.01, 0.01, 0.01, 1.0],  # Especular (quase sem brilho)
                                 0.01)                      # Brilho (muito baixo)
                
        self.RenderCube(0.5, 3, 0.5, 187, 105, 47, wood_material, 0)

        # Cabaça da planta
        leaf_material = Material([0.01, 0.03, 0.01, 1.0],
                                [0.02, 0.06, 0.02, 1.0],  
                                [0.01, 0.01, 0.01, 1.0],  
                                5.0 )

        glPushMatrix()
        glTranslatef(0, 4.5, 0)
        self.RenderCube(1, 1, 1, 95, 235, 92, leaf_material, 0)
        glPopMatrix()