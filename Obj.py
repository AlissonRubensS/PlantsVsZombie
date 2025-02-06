from OpenGL.GL import *

# Classe "Mãe"
class ObjRender:
<<<<<<< Updated upstream
    def __init__(self, x, y, z):
=======
    def _init_(self, x, y, z):
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        glColor3f(r, g, b)
=======
        glColor3f(self.r, self.g, self.b)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        glPopMatrix()

    def RenderPrismaTriangular(self, base, depth, height, r, g, b):
        r, g, b = r / 255, g / 255, b / 255

        # Vértices do prisma triangular
        vertex = [
            [-base, 0, -depth],  # Base frontal esquerda
            [ base, 0, -depth],  # Base frontal direita
            [ 0, height, -depth],    # Topo frontal
            [-base, 0, depth],   # Base traseira esquerda
            [ base, 0, depth ],   # Base traseira direita
            [ 0, height, depth]      # Topo traseiro
        ]

        faces = [
            [0, 1, 2], [3, 4, 5],  # Bases triangulares (frontal e traseira)
            [0, 1, 4, 3],  # Face retangular inferior
            [1, 2, 5, 4],  # Face retangular direita
            [2, 0, 3, 5],  # Face retangular esquerda
        ]

        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)

        # Preenchimento
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(r, g, b)
        glBegin(GL_TRIANGLES)
        for face in faces[:2]:  # Desenha as bases triangulares
            for vid in face:
                glVertex3fv(vertex[vid])
        glEnd()

        glBegin(GL_QUADS)
        for face in faces[2:]:  # Desenha as faces retangulares
            for vid in face:
                glVertex3fv(vertex[vid])
        glEnd()

        # Contornos
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glColor3f(0, 0, 0)
        glBegin(GL_TRIANGLES)
        for face in faces[:2]:  
            for vid in face:
                glVertex3fv(vertex[vid])
        glEnd()

        glBegin(GL_QUADS)
        for face in faces[2:]:
            for vid in face:
                glVertex3fv(vertex[vid])
        glEnd()

=======
>>>>>>> Stashed changes
        glPopMatrix()