# Description: Jogo Plants vs Zombies em 3D
# Authors: Alisson, Fernando e Samara

# Bibliotecas
import glfw
from OpenGL.GL import *
from OpenGL.GLU import * 
from math import sqrt
import time

# Classes
from Obj import ObjRender
from Player import Player
from Peashooter import Peashooter
from Potato import Potato
from Shoot import Shoot
from CherryBomb import CherryBomb
from Material import Material
from Zombie import Zombie


# Variáveis Globais

# Limites de movimento
limite_x_positivo = 15
limite_x_negativo = -15
limite_z_positivo = 15
limite_z_negativo = -15

# temporizadores
spawn_cooldown = 10
last_zumbie_spawn = 0

# Posições iniciais
x, y, z = 0, 0, 0 
Cams = {
    "1" : [40, 30, -40, -40, 0, 40],
    "2" : [0, 50, 40, 0, 10, 0],
    "3" : [-40, 15, 30, 40, 0, -40],
}
index = "2"

posicao_atual_camera = list(Cams[index])
posicao_alvo_camera = list(Cams[index])
velociade_camera = 0.005

# Vetores de Objetos
shoots = []
plants = []
zumbies = []

# Iluminação
luz_ambiente  =  [0.5, 0.5, 0.5, 1.0]  # Luz ambiente mais forte
luz_difusa    =  [0.5, 0.5, 0.5, 1.0]  # Luz difusa no máximo
luz_especualr =  [0.5, 0.5, 0.5, 1.0] # Luz especular
posicao_luz   =  [40, 30, -40, 1.0]  # Posição da luz

# Init
def initialize():
    glClearColor(1,1,1,1)
    glLineWidth(5)
    glEnable(GL_DEPTH_TEST) 
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especualr)

# Função para alterações do código
def update():
    global last_zumbie_spawn, spawn_cooldown
    current_time = time.time()

    # Lógica dos tiros
    for s in shoots.copy():
        if s.z < -25:
            shoots.remove(s)
        else:
            for zumbie in zumbies.copy():
                if colision(s, zumbie, 5):
                    if s in shoots: shoots.remove(s)
                    zumbie.hp -= s.demage
                    print(zumbie.hp)
                    if zumbie.hp <= 0:
                        zumbies.remove(zumbie)

    # Lógica das plantas
    for p in plants.copy():
        if p.type == "Peashooter" and current_time - p.time_init  > 10:
            px, py, pz = p.getPos()
            shoots.append(Shoot(px, py + 4, pz, p.demage))
            p.time_init = time.time()
        if p.type == "CherryBomb" and current_time - p.time_init  > 2:
            plants.remove(p) 

    # Lógica dos Zumbies
    dps = time.time()
    for zumbie in zumbies.copy():
        colidiu = False  # Flag para verificar se o zumbi colidiu com alguma planta
        for p in plants.copy():
            if colision(p, zumbie, 5):
                colidiu = True  # O zumbi colidiu, então ele não deve se mover
                if time.time() - dps >= 1:
                    p.hp -= zumbie.damage
                    dps = time.time()

                if p.hp <= 0:
                    plants.remove(p)
        
        if not colidiu:  # Só move se não colidiu com nenhuma planta
            zumbie.move()

            
    if current_time - last_zumbie_spawn >= spawn_cooldown:
        zumbies.append(Zombie(100, 20, 0.01))
        last_zumbie_spawn = time.time()

    mover_camera_posicao()
    
# Função que desenha na tela
def render():
    # Definição do espaço
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
    glMatrixMode(GL_PROJECTION)      
    glLoadIdentity()                 
    glFrustum(-1, 1, -1, 1, 2, 400)  

    # Configuração de câmera
    glMatrixMode(GL_MODELVIEW)     
    glLoadIdentity()    
         
    gluLookAt( *posicao_atual_camera[:3],     # Posição da Câmera
               *posicao_atual_camera[3:],     # Foco da camera
                0,   1 , 0  )                 # Vetor Up
   
    # Renderização de objetos na cena
    grass_matirial = Material([0.1, 0.3, 0.1, 1.0], 
                              [0.2, 0.6, 0.2, 1.0], 
                              [0.1, 0.1, 0.1, 1.0],
                              10)
    
    grass = ObjRender(0, -3, 0)
    grass.RenderCube(20, 1.5, 20, 165, 245, 96, grass_matirial)
    
    
    fence_material = Material(
    [0.2, 0.15, 0.1, 1.0],  # Ambiente (marrom escuro)
    [0.4, 0.3, 0.2, 1.0],   # Difusa (marrom médio)
    [0.1, 0.1, 0.1, 1.0],   # Especular (pouco brilho)
    20.0                    # Brilho (baixo)
    )

    fence = ObjRender(-19, 0, 0)
    fence.RenderCube(1, 2, 20, 100, 100, 100, fence_material)
    
    bush_material = Material(
    [0.1, 0.2, 0.1, 1.0],  # Ambiente (verde escuro)
    [0.2, 0.4, 0.2, 1.0],  # Difusa (verde médio)
    [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
    10.0                   # Brilho (muito baixo)
    )

    bush_back = ObjRender(-19, 0, -40)
    bush_back.RenderCube(1, 1.5, 10, 31, 48, 32, bush_material)

    bush_front = ObjRender(19, 0, -40)
    bush_front.RenderCube(1, 1.5, 10, 31, 48, 32, bush_material)

    house_material = Material(
        [0.3, 0.3, 0.3, 1.0],  # Ambiente (cinza claro)
        [0.8, 0.8, 0.8, 1.0],  # Difusa (branco suave)
        [0.2, 0.2, 0.2, 1.0],  # Especular (brilho moderado)
        50.0                   # Brilho (moderado)
    )

    house = ObjRender(0, 0, 25)
    house.RenderCube(20, 5, 5, 238, 223, 190, house_material)

    roof_material = Material(
        [0.3, 0.1, 0.1, 1.0],  # Ambiente (vermelho escuro)
        [0.6, 0.2, 0.2, 1.0],  # Difusa (vermelho médio)
        [0.3, 0.3, 0.3, 1.0],  # Especular (brilho moderado)
        30.0                   # Brilho (moderado)
    )

    roof = ObjRender(0, 10, 25)
    roof.RenderPrismaTriangular(20, 5, 8, 191, 62, 33, roof_material)
    
    road_material = Material(
        [0.1, 0.1, 0.1, 1.0],  # Ambiente (cinza escuro)
        [0.3, 0.3, 0.3, 1.0],  # Difusa (cinza médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    road = ObjRender(0, -3, -25)
    road.RenderCube(20, 1.5, 5, 128, 128, 128, road_material)
    
    underground_material = Material(
        [0.2, 0.15, 0.1, 1.0],  # Ambiente (marrom escuro)
        [0.4, 0.3, 0.2, 1.0],   # Difusa (marrom médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    underground = ObjRender(0, -3, 25)
    underground.RenderCube(20, 1.5, 5, 64, 59, 19, underground_material)
    
    cemetery_material = Material(
        [0.1, 0.1, 0.1, 1.0],  # Ambiente (cinza escuro)
        [0.2, 0.2, 0.2, 1.0],  # Difusa (cinza médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    cemetery = ObjRender(0, -3, -40)
    cemetery.RenderCube(20, 1.5, 10, 64, 59, 19, cemetery_material)

    player = Player(x, y, z)
    player.render()

    for p in plants:
        p.render()

    for s in shoots:
        s.render()

    for zombie in zumbies:
        zombie.render()

# Função de mover o player        
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

# Função de mover Câmera
def mover_camera_posicao():
    global posicao_atual_camera

    for i in range(6):
        posicao_atual_camera[i] += (posicao_alvo_camera[i] - posicao_atual_camera[i]) * velociade_camera

def moveCam():
    global index, posicao_alvo_camera

    if index == "1":
        index = "2"
    elif index == "2":
        index = "3"
    elif index == "3":
        index = "1"

    posicao_alvo_camera = Cams[index]

# Função para plantar
def planting(type):
    # Verifica se a alguma planta no local
    for p in plants:
        if p.getPos() == (x, y, z) :
            return
    
    # Se não tiver planta
    if type == "Peashooter":
        new_plant = Peashooter(x, y, z, 100, 25)
    elif type == "Potato":
        new_plant = Potato(x, y, z, 250, 0)
    elif type == "CherryBomb":
        new_plant = CherryBomb(x, y, z, 1, 1000)

    plants.append(new_plant)

# função para detectar colisão
def colision(obj1, obj2, distance_min):
    x1, y1, z1 = obj1.getPos()
    x2, y2, z2 = obj2.getPos()
    distance = sqrt( (x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)
    if distance <= distance_min:
        return True
    return False

# Função de controle do teclado
def keyboard(window, key, scancode, action, mods):
    global keys

    # Funções acionadas por teclas
    if action == glfw.PRESS:
        # Movimentação
        if key == glfw.KEY_A:
            mover(True, True)
        if key == glfw.KEY_D:
            mover(True, False)
        if key == glfw.KEY_S:
            mover(False, True)
        if key == glfw.KEY_W:
            mover(False, False)

        # Plantar
        if key == glfw.KEY_1:
            planting("Peashooter")
        if key == glfw.KEY_2:
            planting("Potato")
        if key == glfw.KEY_3:
            planting("CherryBomb")
        
        # Câmera
        if key == glfw.KEY_ENTER:
            moveCam()    
    
def main():
    glfw.init()                                                      
    window = glfw.create_window(800,800,'PVZ',None,None)
    glfw.make_context_current(window)       
    glfw.set_key_callback(window,keyboard)                        
    initialize()       

    # Looping principal do código                                
    while not glfw.window_should_close(window):                     
        glfw.poll_events()                                                          
        update()
        render()
        glfw.swap_buffers(window)                                   
    glfw.terminate()                                                

if __name__ == '__main__':
    main()