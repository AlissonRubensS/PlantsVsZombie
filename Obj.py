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
    
    def RenderCube(self, width, height, depth, r, g, b, material, textura_Tam):
        # Converte as cores para o intervalo [0,1]
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

        # Propriedades do material
        glMaterialfv(GL_FRONT, GL_AMBIENT, material.coeficiente_ambiente)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, material.coeficiente_difuso)
        glMaterialfv(GL_FRONT, GL_SPECULAR, material.coeficiente_especular)
        glMaterialf(GL_FRONT, GL_SHININESS, material.brilho)
        
        glPushMatrix()
        glTranslatef(self.x, self.y + height, self.z)
        glScalef(width, height, depth)

        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glColor3f(r, g, b)
        
        # Se textura_Tam for 0, use_texture será False automaticamente
        use_texture = bool(textura_Tam)
        
        glBegin(GL_QUADS)
        for strip, n in zip(faces, normal):
            glNormal3fv(n)
            
            if use_texture:
                glTexCoord2f(0.0, 0.0)
            glVertex3fv(vertex[strip[0]])
            
            if use_texture:
                glTexCoord2f(textura_Tam, 0.0)
            glVertex3fv(vertex[strip[1]])
            
            if use_texture:
                glTexCoord2f(textura_Tam, textura_Tam)
            glVertex3fv(vertex[strip[2]])
            
            if use_texture:
                glTexCoord2f(0.0, textura_Tam)
            glVertex3fv(vertex[strip[3]])
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