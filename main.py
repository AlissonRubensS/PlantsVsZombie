import glfw
from OpenGL.GL import *
from OpenGL.GLU import * 

from Obj import ObjRender

x, y, z = 0, 0, 0 
veloc = 0.050
keys = {
    glfw.KEY_A: False,
    glfw.KEY_D: False,
    glfw.KEY_S: False,
    glfw.KEY_W: False,
    glfw.KEY_1: False
}

plantas = []

def initialize():
    glClearColor(1,1,1,1)
    glLineWidth(5)
    glEnable(GL_DEPTH_TEST) # habilitando o algoritmo z-buffer (remoÃ§Ã£o correta de superfÃ­cies ocultadas por outras. Essencial em cenas 3d)

def movePoint():
    global x, y, z
    if keys[glfw.KEY_A]: z += veloc
    if keys[glfw.KEY_D]: z -= veloc
    if keys[glfw.KEY_S]: x += veloc
    if keys[glfw.KEY_W]: x -= veloc

def plantar():
    if keys[glfw.KEY_1]:    # Verificar se já existe alguma planta no local       
        planta = ObjRender(x, y, z, 0, 0, 1)
        plantas.append(planta)

def render():
    movePoint()
    plantar()

    # algoritmo z-buffer utiliza um depth buffer que precisa ser limpo a cada frame, assim como o frame buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   

    glMatrixMode(GL_PROJECTION)      # modo de matriz: matriz de projeÃ§Ã£o
    glLoadIdentity()                 # carregando a matriz identidade
    glFrustum(-1, 1, -1, 1, 2, 100)  # definindo a matriz de projeÃ§Ã£o perspectiva
                                     # glFrustum(left, right, bottom, top, near, far)

    glMatrixMode(GL_MODELVIEW)     # modo de matriz: matriz de cÃ¢mera e de transformaÃ§Ã£o local
    glLoadIdentity()               # carregando matriz identidade
    gluLookAt(60,20, 0,   # definindo a posiÃ§Ã£o da cÃ¢mera
               0, 0, 0,   # definindo o alvo da cÃ¢mera (origem do sistema de coordenadas global)
               0, 1, 0)   # definindo a direÃ§Ã£o up da cÃ¢mera (direÃ§Ã£o do eixo y do sistema de coordenadas global)                

    chao = ObjRender(0, -5, 0, 1, 0, 0)
    chao.RenderCube(40, 4, 40)

    player = ObjRender(x, y, z, 0, 1, 0)
    player.RenderCube(5, 10, 5)

    for p in plantas:
        p.RenderCube(5, 10, 5)

def keyboard(window, key, scancode, action, mods):
    global keys
    if action == glfw.PRESS:     keys[key] = True
    elif action == glfw.RELEASE: keys[key] = False

    if action == glfw.PRESS:    keys[key] = True
    elif action == glfw.RELEASE: keys[key] = False

def main():
    glfw.init()                                                      
    window = glfw.create_window(800,800,'08 - Teste',None,None)
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