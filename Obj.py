from OpenGL.GL import *

# Classe "Mãe"
class ObjRender:

    def __init__(self, x, y, z):
        # Adicionar os pontos centrais 
        self.x = x
        self.y = y
        self.z = z
        
    def getPos(self):
        return (self.x, self.y, self.z)
    
    def RenderCube(self, width, height, depth, r, g, b, material):
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

        normal = [
            [ 0,  0, -1], # Frente
            [ 0,  0,  1], # Trás
            [ 0,  1,  0], # Topo
            [ 0, -1,  0], # Fundo
            [ 1,  0,  0], # Lado direito
            [-1,  0,  0], # Lado esquerdo
        ]

        # Coordenadas de textura para cada face
        tex_coords = [
            [0, 0], [1, 0], [1, 1], [0, 1]  # Coordenadas de textura para cada vértice
        ]

        # Adicionar as propriedades do material
        glMaterialfv(GL_FRONT, GL_AMBIENT, material.coeficiente_ambiente)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, material.coeficiente_difuso)
        glMaterialfv(GL_FRONT, GL_SPECULAR, material.coeficiente_especular)
        glMaterialf(GL_FRONT, GL_SHININESS, material.brilho)
        
        # Transformações
        glPushMatrix()
        glTranslatef(self.x, self.y + height, self.z)
        glScalef(width, height, depth)

        # Renderizar tiras de preenchimento
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        for strip, n in zip(faces, normal):
            glNormal3fv(n)
            for i, vid in enumerate(strip):
                glTexCoord2fv(tex_coords[i])  # Define as coordenadas de textura
                glVertex3fv(vertex[vid])
        glEnd()
        glPopMatrix()

    def RenderPrismaTriangular(self, base, depth, height, r, g, b, material):
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

        normal = [
            [0, 0, -1], [0, 0, 1],  # Bases triangulares
            [0, -1, 0], [1, 0, 0], [0, 1, 0]  # Faces retangulares
        ]

        # Adicionar as propriedades do material
        glMaterialfv(GL_FRONT, GL_AMBIENT, material.coeficiente_ambiente)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, material.coeficiente_difuso)
        glMaterialfv(GL_FRONT, GL_SPECULAR, material.coeficiente_especular)
        glMaterialf(GL_FRONT, GL_SHININESS, material.brilho)

        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)    

        # Preenchimento
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(r, g, b)
        glBegin(GL_TRIANGLES)
        for face, n in zip(faces[:2], normal[:2]):  # Desenha as bases triangulares
            glNormal3fv(n)
            for vid in face:
                glVertex3fv(vertex[vid])
        glEnd()

        glBegin(GL_QUADS)
        for face, n in zip(faces[2:], normal[2:]):  # Desenha as faces retangulares
            glNormal3fv(n)
            for vid in face:
                glVertex3fv(vertex[vid])
        glEnd()
        glPopMatrix()