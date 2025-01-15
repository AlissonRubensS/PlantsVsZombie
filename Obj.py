from OpenGL.GL import *

class ObjRender:
    def __init__(self, x, y, z, r, g, b):
        # Adicionar os pontos centrais 
        self.x = x
        self.y = y
        self.z = z

        # Adicionar as cores
        self.r = r
        self.g = g
        self.b = b

    def RenderCube(self, heigth, width, deph):
        vertex = [
            [self.x - heigth/2, self.y - width/2, self.z - deph/2],
            [self.x + heigth/2, self.y - width/2, self.z - deph/2],
            [self.x + heigth/2, self.y + width/2, self.z - deph/2],
            [self.x - heigth/2, self.y + width/2, self.z - deph/2],
            [self.x - heigth/2, self.y - width/2, self.z + deph/2],
            [self.x + heigth/2, self.y - width/2, self.z + deph/2],
            [self.x + heigth/2, self.y + width/2, self.z + deph/2],
            [self.x - heigth/2, self.y + width/2, self.z + deph/2],
        ]

        faces = [
            [0,1,2,3],
            [0,1,5,4],
            [1,2,6,5],
            [2,3,7,6],
            [3,0,4,7],
            [4,5,6,7]
        ]

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor(self.r, self.g, self.b)
        glBegin(GL_QUADS)
        for f in faces:
            for vid in f:
                glVertex3fv(vertex[vid])
        glEnd()
        
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor(0, 0, 0)
        glBegin(GL_QUADS)
        for f in faces:
            for vid in f:
                glVertex3fv(vertex[vid])
        glEnd()
