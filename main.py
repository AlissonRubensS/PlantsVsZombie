import glfw
from OpenGL.GL import *
from OpenGL.GLU import * 

from Obj import ObjRender
from Player import Player
from Peashooter import Peashooter

# Variáveis Globais
limite_x_positivo = 15
limite_x_negativo = -15
limite_z_positivo = 15
limite_z_negativo = -15


x, y, z = 0, 0, 0 
veloc = 0.050

plantas = []

# Init
def initialize():
    glClearColor(1,1,1,1)
    glLineWidth(5)
    glEnable(GL_DEPTH_TEST) # habilitando o algoritmo z-buffer (remoÃ§Ã£o correta de superfÃ­cies ocultadas por outras. Essencial em cenas 3d)

# Função que desenha na tela
def render():
    # Definição do espaço
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
    glMatrixMode(GL_PROJECTION)      
    glLoadIdentity()                 
    glFrustum(-1, 1, -1, 1, 2, 100)  

    # Configuração de câmera
    glMatrixMode(GL_MODELVIEW)     
    glLoadIdentity()              
    gluLookAt(  60,20, 0,       # Posição da Câmera
                0, 0 , 0,       # Foco da camera
                0, 1 , 0)       # Vetor Up

    # Renderização de objetos na cena
    chao = ObjRender(0, -3, 0)
    chao.RenderCube(20, 1.5, 20, 165, 245, 96)
    player = Player(x, y, z)
    player.spawn()

    for p in plantas:
        p.Spawn()

def mover(eixo, polaridade):
    global x,y,z

    distancia_movimento = 5
    if eixo:
        if polaridade:
            x = min(distancia_movimento + x, limite_x_positivo)
        else:
            x = max( x - distancia_movimento,limite_x_negativo)
    else:
        if polaridade:
            z = min(distancia_movimento + z,limite_z_positivo)
        else:
            z = max(z - distancia_movimento,limite_z_negativo)


def keyboard(window, key, scancode, action, mods):
    global keys

    if action == glfw.PRESS:
        if key == glfw.KEY_S:
            mover(True, True)
        if key == glfw.KEY_W:
            mover(True, False)
        if key == glfw.KEY_A:
            mover(False, True)
        if key == glfw.KEY_D:
            mover(False, False)

    if action == glfw.PRESS and key == glfw.KEY_1:
        plantar()

def plantar():
    planta = Peashooter(x, y, z, 100, 10, 5)
    plantas.append(planta)
    
def main():
    glfw.init()                                                      
    window = glfw.create_window(800,800,'PVZ',None,None)
    glfw.make_context_current(window)       
    glfw.set_key_callback(window,keyboard)                        
    initialize()                                                    
    while not glfw.window_should_close(window):                     
        glfw.poll_events()                                          
        render()                                                    
        glfw.swap_buffers(window)                                   
    glfw.terminate()                                                

if __name__ == '__main__':
    main()