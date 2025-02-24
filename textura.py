from OpenGL.GL import *
from PIL import Image
import os  # Importe o módulo os para manipulação de caminhos

class Textura:
    def __init__(self):
        self.texturas = {}

    def carregaTextura(self, filename):
        """
        Carrega uma textura a partir de um arquivo de imagem.
        Retorna o ID da textura ou None em caso de erro.
        """
        try:
            # Converte o caminho relativo em absoluto
            caminho_absoluto = os.path.join(os.path.dirname(__file__), filename)

            # Verifica se o arquivo existe
            if not os.path.exists(caminho_absoluto):
                print(f"🚨 ERRO: Arquivo '{caminho_absoluto}' não encontrado!")
                return None

            # Abre a imagem com PIL
            img = Image.open(caminho_absoluto)
            img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Inverte a imagem para o OpenGL
            imgData = img.convert("RGBA").tobytes()  # Converte para formato RGBA

            texId = glGenTextures(1)  # Gera um ID para a textura
            glBindTexture(GL_TEXTURE_2D, texId)  # Ativa a textura

            # Configuração da textura (filtragem e repetição)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

            # Envia os dados da textura para o OpenGL
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imgData)

            glBindTexture(GL_TEXTURE_2D, 0)  # Desativa a textura
            self.texturas[filename] = texId  # Armazena a textura no dicionário
            return texId  # Retorna o ID da textura

        except Exception as e:
            print(f"🚨 Erro ao carregar textura {filename}: {e}")
            return None

    def carregaSkybox(self, texturas):
        """
        Carrega as texturas do skybox e retorna uma lista com os IDs das texturas.
        """
        skybox_textures = []
        for tex in texturas:
            tex_id = self.carregaTextura(tex)
            if tex_id is None:
                print(f"Erro ao carregar textura do skybox: {tex}")
                return None
            skybox_textures.append(tex_id)
        return skybox_textures