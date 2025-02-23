from OpenGL.GL import *
from PIL import Image
import os

class TextureLoader:
    @staticmethod
    def load_texture(caminho):
        """
        Carrega uma textura a partir de um arquivo de imagem.
        Retorna o ID da textura ou None em caso de erro.
        """
        try:
            # Verifica se o arquivo existe
            if not os.path.exists(caminho):
                print(f"🚨 ERRO: Arquivo '{caminho}' não encontrado!")
                return None

            # Abre a imagem com PIL
            img = Image.open(caminho)
            img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Inverte a imagem para o OpenGL
            img_data = img.tobytes()  # Converte a imagem para bytes

            # Gera uma textura OpenGL
            textura_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, textura_id)

            # Configura os parâmetros da textura
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

            # Define o formato da textura com base no modo da imagem
            if img.mode == "RGB":
                formato = GL_RGB
            elif img.mode == "RGBA":
                formato = GL_RGBA
            else:
                img = img.convert("RGB")  # Converte para RGB se não for RGB ou RGBA
                formato = GL_RGB

            # Envia os dados da imagem para o OpenGL
            glTexImage2D(GL_TEXTURE_2D, 0, formato, img.width, img.height, 0, formato, GL_UNSIGNED_BYTE, img_data)

            print(f"✅ Textura carregada com sucesso: {caminho}")
            return textura_id

        except Exception as e:
            print(f"🚨 Erro ao carregar textura {caminho}: {e}")
            return None