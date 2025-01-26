from OpenGL.GL import *

class ObjRender:
    def __init__(self, x, y, z, r, g, b):
        # Adicionar os pontos centrais 
        self.x = x
        self.y = y
        self.z = z

        # Adicionar as cores
        self.r = r / 255
        self.g = g / 255
        self.b = b / 255

    def RenderCube(self, width, height, depth):
        vertex = [
            [ 1,  1, -1], # Vértice superior frontal direito
            [ 1, -1, -1], # Vértice inferior frontal direito
            [-1, -1, -1], # Vértice inferior frontal esquerdo
            [-1,  1, -1], # Vértice superior frontal esquerdo
            [ 1,  1,  1], # Vértice superior traseiro direito
            [ 1, -1,  1], # Vértice inferior traseiro direito
            [-1, -1,  1], # Vértice inferior traseiro esquerdo
            [-1,  1,  1], # Vértice superior traseiro esquerdo
        ]

        faces = [
            [0, 1, 2, 3], # Frente
            [4, 5, 6, 7], # Trás
            [0, 4, 7, 3], # Topo
            [1, 5, 6, 2], # Fundo
            [0, 1, 5, 4], # Lado direito
            [3, 2, 6, 7], # Lado esquerdo
        ]

        # Transformações
        glPushMatrix()
        glTranslatef(self.x, self.y + height, self.z)
        glScalef(width, height, depth)

        # Renderizar tiras de triângulos
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(self.r, self.g, self.b)
        glBegin(GL_QUADS)
        for strip in faces:
            for vid in strip:
                glVertex3fv(vertex[vid])
        glEnd()

        # Renderizar contornos
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3f(0, 0, 0)
        glBegin(GL_QUADS)
        for strip in faces:
            for vid in strip:
                glVertex3fv(vertex[vid])
        glEnd()
        glPopMatrix()
