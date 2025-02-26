from OpenGL.GL import *
from Plants import *
from Material import Material

class Potato(Plants):
    def __init__(self, x, y, z, hp, demage):
        super().__init__(x, y, z, hp, demage)
        self.type = "Potato"

    def render(self):
        # Cabo da planta
                
        material = Material([0.0, 0.0, 0.0, 1.0], 
                            [0.0, 0.0, 0.0, 1.0], 
                            [0.0, 0.0, 0.0, 1.0], 
                            50)
        
        self.RenderCube(1.5, 3, 1.5, 187, 105, 47, material, 0)