# Description: Jogo Plants vs Zombies em 3D
# Authors: Alisson, Fernando e Samara

# Bibliotecas
import glfw
from OpenGL.GL import *
from OpenGL.GLU import * 
<<<<<<< HEAD
=======
from math import sqrt
>>>>>>> main
import time

# Classes
from Obj import ObjRender
from Player import Player
from Peashooter import Peashooter
from Potato import Potato
from Shoot import Shoot
from CherryBomb import CherryBomb
from Material import Material
<<<<<<< HEAD
from textura import Textura



# Variáveis Globais
=======
from Zombie import Zombie


# Variáveis Globais

>>>>>>> main
# Limites de movimento
limite_x_positivo = 15
limite_x_negativo = -15
limite_z_positivo = 15
limite_z_negativo = -15

<<<<<<< HEAD
# Posições iniciais
x, y, z = 0, 0, 0 
plants = []
shoots = []
=======
# temporizadores
spawn_cooldown = 10
last_zumbie_spawn = 0
>>>>>>> main

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

<<<<<<< HEAD
# Iluminação

=======
# Vetores de Objetos
shoots = []
plants = []
zumbies = []

# Iluminação
>>>>>>> main
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
<<<<<<< HEAD
    for p in plants:
        if p.type == "Peashooter" and time.time() - p.time_init  > 10:
            px, py, pz = p.getPos()
            shoots.append(Shoot(px, py + 4, pz))
            p.time_init = time.time()
        if p.type == "CherryBomb" and time.time() - p.time_init  > 2:
            plants.remove(p)

    
    for s in shoots:
        if s.z < -45:
=======
    global last_zumbie_spawn, spawn_cooldown
    current_time = time.time()

    # Lógica dos tiros
    for s in shoots.copy():
        if s.z < -25:
>>>>>>> main
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
<<<<<<< HEAD

=======
    
>>>>>>> main
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
<<<<<<< HEAD
    
    # Renderização do skybox
    # skybox = ObjRender(0, 0, 0)  # Posição do skybox (centro da cena)
    # skybox.RenderSkybox(skybox_textures, 50)  # Tamanho do skybox
    
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, grass_texture)
    grass_material = Material([0.1, 0.3, 0.1, 1.0], 
                              [0.2, 0.6, 0.2, 1.0], 
                              [0.1, 0.1, 0.1, 1.0],
                              10)
    
    grass = ObjRender(0, -3, 0)
    grass.RenderCube(20, 1.5, 20, 165, 245, 96, grass_material)
    glDisable(GL_TEXTURE_2D)
    
    # casa e campo de batalha
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, fence_texture)
    fence_material = Material(
        [0.2, 0.15, 0.1, 1.0],  # Ambiente (marrom escuro)
        [0.4, 0.3, 0.2, 1.0],   # Difusa (marrom médio)
        [0.1, 0.1, 0.1, 1.0],   # Especular (pouco brilho)
        20.0                    # Brilho (baixo)
    )

    fence_d = ObjRender(-19.8, 0, 0)
    fence_d.RenderCube(0.2, 2, 20, 250, 250, 250, fence_material)    
    fence_e = ObjRender(19.8, 0, 0)
    fence_e.RenderCube(0.2, 2, 20, 250, 250, 250, fence_material)
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, house_texture)
    house_material = Material(
        [0.3, 0.3, 0.3, 1.0],  # Ambiente (cinza claro)
        [0.8, 0.8, 0.8, 1.0],  # Difusa (branco suave)
        [0.2, 0.2, 0.2, 1.0],  # Especular (brilho moderado)
        50.0                   # Brilho (moderado)
    )

    house = ObjRender(0, 0, 25)
    house.RenderCube(20, 5, 5, 238, 223, 190, house_material)
    glDisable(GL_TEXTURE_2D)

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, roof_texture)
    roof_material = Material(
        [0.3, 0.1, 0.1, 1.0],  # Ambiente (vermelho escuro)
        [0.6, 0.2, 0.2, 1.0],  # Difusa (vermelho médio)
        [0.3, 0.3, 0.3, 1.0],  # Especular (brilho moderado)
        30.0                   # Brilho (moderado)
    )

    roof = ObjRender(0, 10, 25)
    roof.RenderPrismaTriangular(20, 5, 8, 191, 62, 33, roof_material)
    glDisable(GL_TEXTURE_2D)   
    
    
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, road_texture)
=======
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
    
>>>>>>> main
    road_material = Material(
        [0.1, 0.1, 0.1, 1.0],  # Ambiente (cinza escuro)
        [0.3, 0.3, 0.3, 1.0],  # Difusa (cinza médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )
<<<<<<< HEAD

    road = ObjRender(0, -3, -25)
    road.RenderCube(20, 1.5, 5, 112, 124, 77, road_material)

    glDisable(GL_TEXTURE_2D)
    
    underground_material = Material(
        [0.2, 0.15, 0.1, 1.0],  # Ambiente (marrom escuro)
        [0.4, 0.3, 0.2, 1.0],   # Difusa (marrom médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )
    

    underground = ObjRender(0, -3, 25)
    underground.RenderCube(20, 1.5, 5, 64, 59, 19, underground_material)


    glEnable(GL_TEXTURE_2D)

    # cemiterio e os tumulos
    glBindTexture(GL_TEXTURE_2D, cemetery_texture)   
    cemetery_material = Material(
        [0.1, 0.1, 0.1, 1.0],  # Ambiente (cinza escuro)
        [0.2, 0.2, 0.2, 1.0],  # Difusa (cinza médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    cemetery = ObjRender(0, -3, -40)
    cemetery.RenderCube(20, 1.5, 10, 64, 59, 19, cemetery_material)
    glDisable(GL_TEXTURE_2D)
    
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, bush_texture)
    bush_material = Material(
    [0.1, 0.2, 0.1, 1.0],  # Ambiente (verde escuro)
    [0.2, 0.4, 0.2, 1.0],  # Difusa (verde médio)
    [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
    10.0                   # Brilho (muito baixo)
    )

    bush_d = ObjRender(-19, 0, -40)
    bush_d.RenderCube(1, 1.5, 10, 255, 255, 255, bush_material)    
    
    bush_back = ObjRender(0, 0, -50)
    bush_back.RenderCube(20, 1.5, 1, 255, 255, 255, bush_material)

    bush_e = ObjRender(19, 0, -40)
    bush_e.RenderCube(1, 1.5, 10, 255, 255, 255, bush_material)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBindTexture(GL_TEXTURE_2D, tombs_texture)

    tomb_positions = [
        (-15, 0, -38),
        (-10, 0, -40),
        (-5, 0, -37),
        (0, 0, -39),
        (5, 0, -40),
        (10, 0, -37),
        (15, 0, -38)
    ]

    
    tombs_material = Material(
    [0.1, 0.2, 0.1, 1.0],     # Ambiente (verde escuro)
    [0.2, 0.4, 0.2, 1.0],     # Difusa (verde médio)
    [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
    10.0                      # Brilho (muito baixo)
    )

    for pos in tomb_positions:
        tomb = ObjRender(*pos)
        tomb.RenderCube(3, 3, 0.01, 0, 0, 0, tombs_material)  

    glDisable(GL_BLEND)  
    glDisable(GL_TEXTURE_2D)

=======

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
>>>>>>> main

    player = Player(x, y, z)
    player.render()

    for p in plants:
        p.render()

    for s in shoots:
        s.render()

<<<<<<< HEAD
=======
    for zombie in zumbies:
        zombie.render()

>>>>>>> main
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
<<<<<<< HEAD
        new_plant = Peashooter(x, y, z, 100, 10)
    elif type == "Potato":
        new_plant = Potato(x, y, z, 1000, 0)
=======
        new_plant = Peashooter(x, y, z, 100, 25)
    elif type == "Potato":
        new_plant = Potato(x, y, z, 250, 0)
>>>>>>> main
    elif type == "CherryBomb":
        new_plant = CherryBomb(x, y, z, 1, 1000)

    plants.append(new_plant)
<<<<<<< HEAD
=======

# função para detectar colisão
def colision(obj1, obj2, distance_min):
    x1, y1, z1 = obj1.getPos()
    x2, y2, z2 = obj2.getPos()
    distance = sqrt( (x2-x1) ** 2 + (y2-y1) ** 2 + (z2-z1) ** 2)
    if distance <= distance_min:
        return True
    return False
>>>>>>> main

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

    # Carregando as texturas
    global grass_texture, fence_texture, house_texture, bush_texture, road_texture, cemetery_texture, tombs_texture, roof_texture, skybox
    # Carregando as texturas
    texture_manager = Textura()  # Instância da classe Textura

    grass_texture = texture_manager.carregaTextura("texturas/grama.jpg")
    fence_texture = texture_manager.carregaTextura("texturas/cerca.jpg")
    bush_texture = texture_manager.carregaTextura("texturas/moitas.jpg")
    road_texture = texture_manager.carregaTextura("texturas/estrada.jpg")
    cemetery_texture = texture_manager.carregaTextura("texturas/cemiterio.jpg")
    tombs_texture = texture_manager.carregaTextura("texturas/tumba.png")
    roof_texture = texture_manager.carregaTextura("texturas/telhado.jpg")
    house_texture = texture_manager.carregaTextura("texturas/casa.jpg")

    # skybox_textures = texture_manager.carregaSkybox([
    #     "texturas/skybox_front.jpg",
    #     "texturas/skybox_back.jpg",
    #     "texturas/skybox_left.jpg",
    #     "texturas/skybox_right.jpg",
    #     "texturas/skybox_top.jpg",
    #     "texturas/skybox_bottom.jpg"
    # ])



    # Looping principal do código                                
    while not glfw.window_should_close(window):                     
        glfw.poll_events()                                                          
        update()
        render()
        glfw.swap_buffers(window)                                   
    glfw.terminate()                                                

if __name__ == '__main__':
    main()