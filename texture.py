from PIL import Image
import numpy as np
from OpenGL.GL import*

def load_texture(filename):
    image = Image.open(filename)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.array(image.convert("RGBA"), np.uint8)
    
    texture_id = glGenTextures(1)  #ID para a textura
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Define a imagem da textura
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
    # Define os parâmetros para repetir a textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    
    # Define os filtros de textura para escalonamento
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    # Desvincula a textura
    glBindTexture(GL_TEXTURE_2D, 0)
    
    return texture_id
