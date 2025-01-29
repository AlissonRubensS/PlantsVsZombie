from OpenGL.GL import *

class ObjRender:
    def __init__(self, x, y, z):
        # Adicionar os pontos centrais 
        self.x = x
        self.y = y
        self.z = z

    def RenderCube(self, width, height, depth, r, g, b):
        # Adicionar as cores
        r = r / 255
        g = g / 255
        b = b / 255

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

        # Renderizar tiras de preenchimento
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(r, g, b)
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

    def RenderTriangle(self, base, height, r, g, b):
        # Adicionar as cores
        r = r / 255
        g = g / 255
        b = b / 255

        vertex = [
            [ 1, -1,  0],
            [ 1,  1,  0],
            [-1,  0,  0],
            [ 0,  0,  1],
        ]

        faces = [
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3],
        ]

        glPushMatrix()

        glTranslatef(r, g, b)
        glScalef(base/2, height, base/2)
        glRotatef(-90, 1, 0, 0)

        # Renderizar preenchimentos
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(self.r, self.g, self.b)
        glBegin(GL_TRIANGLES)
        for strip in faces:
            for vid in strip:
                glVertex3fv(vertex[vid])
        glEnd()

        # Renderizar contornos
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3f(0, 0, 0)
        glBegin(GL_TRIANGLES)
        for strip in faces:
            for vid in strip:
                glVertex3fv(vertex[vid])

        glEnd()
        glPopMatrix()

    