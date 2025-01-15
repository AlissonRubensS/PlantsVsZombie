from OpenGL.GL import *
from Obj import ObjRender

class Player(ObjRender):
    def __init__(self, x, y, z, r, g, b):
        super().__init__(x, y, z, r, g, b)
    
    def spawn(self):
        vertex = [
            [self.x - 2.5, self.y - 5, self.z - 2.5],
            [self.x + 2.5, self.y - 5, self.z - 2.5],
            [self.x + 2.5, self.y + 5, self.z - 2.5],
            [self.x - 2.5, self.y + 5, self.z - 2.5],
            [self.x - 2.5, self.y - 5, self.z + 2.5],
            [self.x + 2.5, self.y - 5, self.z + 2.5],
            [self.x + 2.5, self.y + 5, self.z + 2.5],
            [self.x - 2.5, self.y + 5, self.z + 2.5],
        ]

        faces = [
            [0,1,2,3],
            [0,1,5,4],
            [1,2,6,5],
            [2,3,7,6],
            [3,0,4,7],
            [4,5,6,7]
        ]

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor(self.r, self.g, self.b)
        glBegin(GL_QUADS)
        for f in faces:
            for vid in f:
                glVertex3fv(vertex[vid])
        glEnd()