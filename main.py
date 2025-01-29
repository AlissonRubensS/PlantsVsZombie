import glfw
from OpenGL.GL import *
from OpenGL.GLU import * 

from Obj import ObjRender
from Player import Player
from Peashooter import Peashooter

# Variáveis Globais
x, y, z = 0, 0, 0 
veloc = 0.025
keys = {
    glfw.KEY_A: False,
    glfw.KEY_D: False,
    glfw.KEY_S: False,
    glfw.KEY_W: False,
}
plantas = []

# Init
def initialize():
    glClearColor(1,1,1,1)
    glLineWidth(5)
    glEnable(GL_DEPTH_TEST) # habilitando o algoritmo z-buffer (remoÃ§Ã£o correta de superfÃ­cies ocultadas por outras. Essencial em cenas 3d)

# Função que desenha na tela
def render():
    # Chamadas de funções recorrentes
    movePoint()

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

def keyboard(window, key, scancode, action, mods):
    global keys
    if action == glfw.PRESS:     keys[key] = True
    elif action == glfw.RELEASE: keys[key] = False

    if action == glfw.PRESS and key == glfw.KEY_1:
        plantar()

def movePoint():
    global x, y, z
    if keys[glfw.KEY_A]: z += veloc
    if keys[glfw.KEY_D]: z -= veloc
    if keys[glfw.KEY_S]: x += veloc
    if keys[glfw.KEY_W]: x -= veloc

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