from OpenGL.GL import *
from Obj import ObjRender

class Player(ObjRender):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
    
    def spawn(self):
        vertex = [
            [self.x - 2, self.y, self.z - 2],
            [self.x + 2, self.y, self.z - 2],
            [self.x + 2, self.y + 8, self.z - 2],
            [self.x - 2, self.y + 8, self.z - 2],
            [self.x - 2, self.y, self.z + 2],
            [self.x + 2, self.y, self.z + 2],
            [self.x + 2, self.y + 8, self.z + 2],
            [self.x - 2, self.y + 8, self.z + 2],
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
        glColor(0, 1, 0)
        glBegin(GL_QUADS)
        for f in faces:
            for vid in f:
                glVertex3fv(vertex[vid])
        glEnd()