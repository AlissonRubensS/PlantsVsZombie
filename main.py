# Description: Jogo Plants vs Zombies em 3D
# Authors: Alisson, Fernando e Samara

# Bibliotecas
import glfw
from OpenGL.GL import *
from OpenGL.GLU import * 
from math import sqrt
import time
import random

# Classes
from Obj import ObjRender
from Material import Material
from Player import Player
from Peashooter import Peashooter
from Shoot import Shoot
from Potato import Potato
from HerbThorn import HerbThorn
from Zombie import Zombie
from ZombieMini import ZombieMini
from texture import load_texture


# Variáveis Globais

# Limites de movimento
limite_x_positivo = 15
limite_x_negativo = -15
limite_z_positivo = 15
limite_z_negativo = -15
limite_z_gameover = 20

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
    global grass_texture, fence_texture, bush_texture, house_texture, roof_texture, underground_texture, cemetery_texture, tomb_texture, road_texture, skybox
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
    
    grass_texture = load_texture("texturas\grama.jpg")
    fence_texture = load_texture("texturas\cerca.jpg")
    bush_texture = load_texture("texturas\moitas.jpg")
    house_texture = load_texture("texturas\casa.jpg")
    roof_texture = load_texture("texturas\cerca.jpg")
    underground_texture = load_texture("texturas\cemiterio.jpg")
    cemetery_texture =load_texture("texturas\cemiterio.jpg")
    tomb_texture =load_texture("texturas/tumba.png")
    road_texture = load_texture("texturas\estrada.jpg")
    skybox = load_texture("texturas/Skybox.jpg")
    
def Skybox(size = 5):
    glEnable(GL_TEXTURE_2D)
    # glBindTexture(GL_TEXTURE_2D, skybox)

    skybox_textures = {
        "left":   ([0.0, 0.33], [0.25, 0.33], [0.0, 0.66], [0.25, 0.66]),
        "right":  ([0.5, 0.33], [0.75, 0.33], [0.5, 0.66], [0.75, 0.66]),
        "front":  ([0.25, 0.33], [0.5, 0.33], [0.25, 0.66], [0.5, 0.66]),
        "back":   ([0.75, 0.33], [1, 0.33], [0.75, 0.66], [1, 0.66]),
        "top":    ([0.25, 0.66], [0.5, 0.66], [0.25, 1], [0.5, 1]),
        "bottom": ([0.25, 0], [0.5, 0], [0.25, 0.33], [0.5, 0.33]),
    }

    faces = [
        ("right",  [size, -size, -size],  [size, -size, size],  [size, size, size],  [size, size, -size]),  
        ("left",   [-size, -size, size],  [-size, -size, -size],  [-size, size, -size],  [-size, size, size]),  
        ("front",  [-size, -size, -size],  [size, -size, -size],  [size, size, -size],  [-size, size, -size]), 
        ("back",   [size, -size, size],  [-size, -size, size],  [-size, size, size],  [size, size, size]), 
        ("top",    [-size, size, -size],  [size, size, -size],  [size, size, size],  [-size, size, size]),  
        ("bottom", [-size, -size, size],  [size, -size, size],  [size, -size, -size],  [-size, -size, -size]),  
    ]

    for face, v1, v2, v3, v4 in faces:
        glTexCoord2fv(skybox_textures[face][0])
        glVertex3fv(v1)
        glTexCoord2fv(skybox_textures[face][1])
        glVertex3fv(v2)
        glTexCoord2fv(skybox_textures[face][2])
        glVertex3fv(v3)
        glTexCoord2fv(skybox_textures[face][3])
        glVertex3fv(v4)

    # glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
    
# Função para alterações do código
def update():
    global last_zumbie_spawn, spawn_cooldown, window
    current_time = time.time()
            
    # Lógica dos tiros
    for s in shoots.copy():
        if s.z < -25:
            shoots.remove(s)
        else:
            for zumbie in zumbies.copy():
                if colision(s, zumbie, 5):
                    shoots.remove(s)
                    zumbie.hp -= s.demage
                    if zumbie.hp <= 0:
                        zumbies.remove(zumbie)
                    

    # Lógica das plantas
    for p in plants.copy():
        if p.type == "Peashooter" and current_time - p.time_init  > 5:
            shoots.append(Shoot(*p.getPos(), p.demage))
            p.time_init = current_time

    # Lógica dos Zumbies
    for zumbie in zumbies.copy():
        if zumbie.z >= limite_z_gameover:
            print("Game Over! Um zumbi chegou ao fim do cenário.")
            glfw.set_window_should_close(window, True)  # Fecha a janela e encerra o jogo
        colidiu = False
        
        if zumbie.hp <= 0:
            zumbies.remove(zumbie)
        for p in plants.copy():
            if p.hp <= 0:
                plants.remove(p)
            elif colision(p, zumbie, 5):
                if p.type == "HerbThorn":
                    p.apply_damage(zumbie, current_time, 2)
                else:
                    colidiu = True  # O zumbi colidiu, então ele não deve se mover
                    p.apply_damage(zumbie, current_time, 0)

                    if current_time - zumbie.cooldown >= 1:
                        p.hp -= zumbie.damage
                        zumbie.cooldown  = current_time

        if not colidiu:  # Só move se não colidiu com nenhuma planta
            zumbie.move()

            
    if current_time - last_zumbie_spawn >= spawn_cooldown:
        if random.random() < 0.5:  # 50% de chance para cada
            zumbies.append(Zombie(100, 20, 0.01))  
        else:
            zumbies.append(ZombieMini(50, 10, 0.03))  

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
    
    Skybox()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, grass_texture) 
    
    # Supondo que você queira repetir a textura 5 vezes por face:
    grass = ObjRender(0, -3, 0)
    grass.RenderCube(20, 1.5, 20, 165, 245, 96, grass_matirial, 1)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)
     
    
    fence_material = Material(
    [0.2, 0.15, 0.1, 1.0],  # Ambiente (marrom escuro)
    [0.4, 0.3, 0.2, 1.0],   # Difusa (marrom médio)
    [0.1, 0.1, 0.1, 1.0],   # Especular (pouco brilho)
    20.0                    # Brilho (baixo)
    )
    
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, fence_texture) 

    fence_positions = [
        (-19, 0, 0),
        (19, 0, 0)
    ]

    for pos in fence_positions:
        fence = ObjRender(*pos)
        fence.RenderCube(1, 2, 20, 100, 100, 100, fence_material, 1)  
    
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    bush_material = Material(
    [0.1, 0.2, 0.1, 1.0],  # Ambiente (verde escuro)
    [0.2, 0.4, 0.2, 1.0],  # Difusa (verde médio)
    [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
    10.0                   # Brilho (muito baixo)
    )

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, bush_texture) 

    bush_d = ObjRender(-19, 0, -40)
    bush_d.RenderCube(1, 1.5, 10, 255, 255, 255, bush_material, 1)    
    
    bush_back = ObjRender(0, 0, -50)
    bush_back.RenderCube(20, 1.5, 1, 255, 255, 255, bush_material, 1)

    bush_e = ObjRender(19, 0, -40)
    bush_e.RenderCube(1, 1.5, 10, 255, 255, 255, bush_material, 1)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    house_material = Material(
        [0.3, 0.3, 0.3, 1.0],  # Ambiente (cinza claro)
        [0.8, 0.8, 0.8, 1.0],  # Difusa (branco suave)
        [0.2, 0.2, 0.2, 1.0],  # Especular (brilho moderado)
        50.0                   # Brilho (moderado)
    )

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, house_texture) 
    
    house = ObjRender(0, 0, 25)
    house.RenderCube(20, 5, 5, 238, 223, 190, house_material, 1)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    roof_material = Material(
        [0.3, 0.1, 0.1, 1.0],  # Ambiente (vermelho escuro)
        [0.6, 0.2, 0.2, 1.0],  # Difusa (vermelho médio)
        [0.3, 0.3, 0.3, 1.0],  # Especular (brilho moderado)
        30.0                   # Brilho (moderado)
    )

    # glEnable(GL_TEXTURE_2D)
    # glBindTexture(GL_TEXTURE_2D, roof_texture) 
    
    roof = ObjRender(0, 10, 25)
    roof.RenderPrismaTriangular(20, 5, 8, 191, 62, 33, roof_material)
    
    # glBindTexture(GL_TEXTURE_2D, 0)
    # glDisable(GL_TEXTURE_2D)

    road_material = Material(
        [0.1, 0.1, 0.1, 1.0],  # Ambiente (cinza escuro)
        [0.3, 0.3, 0.3, 1.0],  # Difusa (cinza médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, road_texture)

    road = ObjRender(0, -3, -25)
    road.RenderCube(20, 1.5, 5, 128, 128, 128, road_material, 1)
    
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    underground_material = Material(
        [0.2, 0.15, 0.1, 1.0],  # Ambiente (marrom escuro)
        [0.4, 0.3, 0.2, 1.0],   # Difusa (marrom médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, underground_texture)

    underground = ObjRender(0, -3, 25)
    underground.RenderCube(20, 1.5, 5, 64, 59, 19, underground_material, 1)
    
    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    cemetery_material = Material(
        [0.1, 0.1, 0.1, 1.0],  # Ambiente (cinza escuro)
        [0.2, 0.2, 0.2, 1.0],  # Difusa (cinza médio)
        [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
        10.0                   # Brilho (muito baixo)
    )

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, cemetery_texture)

    cemetery = ObjRender(0, -3, -40)
    cemetery.RenderCube(20, 1.5, 10, 64, 59, 19, cemetery_material, 1)

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

    tombs_material = Material(
    [0.1, 0.2, 0.1, 1.0],     # Ambiente (verde escuro)
    [0.2, 0.4, 0.2, 1.0],     # Difusa (verde médio)
    [0.05, 0.05, 0.05, 1.0],  # Especular (quase sem brilho)
    10.0                      # Brilho (muito baixo)
    )
    
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tomb_texture)

    tomb_positions = [
        (-15, 0, -38),
        (-10, 0, -40),
        (-5, 0, -37),
        (0, 0, -39),
        (5, 0, -40),
        (10, 0, -37),
        (15, 0, -38)
    ]

    for pos in tomb_positions:
        tomb = ObjRender(*pos)
        tomb.RenderCube(3, 3, 0.01, 0, 0, 0, tombs_material, 1)  

    glBindTexture(GL_TEXTURE_2D, 0)
    glDisable(GL_TEXTURE_2D)

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
    elif type == "HerbThorn":
        new_plant = HerbThorn(x, y, z, 10, 5)

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
            planting("HerbThorn")
        if key == glfw.KEY_R:
            plants.pop()
        
        # Câmera
        if key == glfw.KEY_ENTER:
            moveCam()    
    
def main():
    global window
    
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