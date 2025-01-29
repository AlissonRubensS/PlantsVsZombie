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
    glFrustum(-1, 1, -1, 1, 2, 150)  

    # Configuração de câmera
    glMatrixMode(GL_MODELVIEW)     
    glLoadIdentity()              
    gluLookAt(  100, 20, 0,       # Posição da Câmera
                0, 0 , 0,       # Foco da camera
                0, 1 , 0)       # Vetor Up

    # Renderização de objetos na cena
    
    field = ObjRender(0, -3, 0)
    field.RenderCube(20, 1.5, 20, 165, 245, 96)

    
    fence = ObjRender(-19, 0, 0)
    fence.RenderCube(1, 2, 20, 255, 255, 255)
    bush_back= ObjRender(-19, 0, -40)
    bush_back.RenderCube(1, 1.5, 10, 31, 48, 32)
    bush_front= ObjRender(19, 0, -40)
    bush_front.RenderCube(1, 1.5, 10, 31, 48, 32)
    

    house = ObjRender(0,0, 25)
    house.RenderCube(20, 5, 5, 238, 223, 190)

    roof = ObjRender(0,10,25)
    roof.RenderPrismaTriangular(20,5,8, 191, 62, 33)
    
    road = ObjRender(0, -3, -25)
    road.RenderCube(20, 1.5, 5, 128, 128, 128)
    
    underground = ObjRender(0,-3, 25)
    underground.RenderCube(20, 1.5, 5, 64, 59, 19)
    
    cemetery = ObjRender(0, -3, -40)
    cemetery.RenderCube(20, 1.5, 10, 64, 59, 19)

    player = Player(x, y, z)
    player.spawn()

    for p in plantas:
        p.Spawn()

def mover(eixo, polaridade):
    global x,y,z
    print(z,y,z)

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