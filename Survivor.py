import pygame
import configparser as ConfigParser
import math
import random
#from scheduler import Scheduler
from ClaseJugador import*
from ClaseEnemigo import *
from ClaseFondo import *
from ClaseBloque import *
from ClaseBala import *
from Util import *
from ClaseSpawn import *
from ClaseBonus import *
from ClaseColision import *
from ClaseMenuInicial import *
from ClaseBoss import *

WIDTH=600
HEIGHT=600
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
ROJO=(255,0,0)
AZUL=(0,0,255)
origen=[WIDTH/2,HEIGHT/2]

NIVEL = 1

def recorte(archivo,filas,columnas,ancho,alto):
    imagen=pygame.image.load(archivo)
    ls=[]
    for i in range(filas):
        ls.append([])
        for j in range(columnas):
            cuadro=imagen.subsurface(j*ancho,i*alto,ancho,alto)
            ls[i].append(cuadro)
    return ls

def pausa():
    pantalla.fill(NEGRO)
    pausado = True
    menu_pausa = False
    for e in zombies:
        e.sonido_zombie.stop()
    for m in modificadores:
        m.sonido_equipar.stop()
    if (NIVEL == 1):
        for s in spawners:
            s.sonido_explosion.stop()
    fondomenupausa=pygame.image.load('survivor-logo.jpg')
    pygame.display.set_caption("Ejemplo de menu")
    ClaseMenuPausa=MenuInicial()
    opcionesp=['Continuar', 'Salir']
    ClaseMenuPausa.opciones=opcionesp
    while pausado and not menu_pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_pausa = True
                pausado = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ClaseMenuPausa.abajo()
                if event.key == pygame.K_UP:
                    ClaseMenuPausa.arriba()
                if event.key == pygame.K_RETURN:
                    ClaseMenuPausa.seleccion=ClaseMenuPausa.nop
        if ClaseMenuPausa.seleccion==1:
            pausado=True
            menu_pausa=True
            creditos=True
            preludio=True
            fin=False
        if ClaseMenuPausa.seleccion==2:
            menu_pausa=False
            pausado=True
            fin=False
            quit()
        reloj.tick(60)
        pantalla.fill(NEGRO)
        pantalla.blit(fondomenupausa,[0,0])
        ClaseMenuPausa.draw(pantalla)
        pygame.display.flip()

def controlesmenu():
    img=pygame.image.load('controles.jpg')
    controlesm=False
    sonido_controles=pygame.mixer.Sound('controles.ogg')
    sonido_controles.play()
    sonido_controles.set_volume(0.4)
    while not controlesm:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sonido_controles.stop()
                    controlesm=True
                    menu_inicial=False
                    pantalla.fill(NEGRO)
                    pygame.display.flip()
                    menuinicial.seleccion=0
                    menuinicial()
        pantalla.blit(img,[0,0])
        pygame.display.flip()
        pygame.display.update()
        reloj.tick(20)

def victory():
    fin_victoria = False
    #Musica victory
    sonido_nivel1.stop()
    sonido_nivel2.stop()
    for e in zombies:
        e.sonido_zombie.stop()
    for m in modificadores:
        m.sonido_equipar.stop()
    for b in bosses:
        b.sonido_memesis.stop()
    if (NIVEL == 1):
        for s in spawners:
            s.sonido_explosion.stop()
    sonido_victory=pygame.mixer.Sound('victory1.ogg')
    sonido_victory.play()
    fin=True
    img=pygame.image.load('victory.jpg')
    while not fin_victoria:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.quit()
                    quit()
        fuente=pygame.font.Font(None,25)
        pantalla.blit(img,[0,0])
        texto=fuente.render('Presione la tecla S para salir',True,NEGRO)
        pantalla.blit(texto,[180,570])
        pygame.display.update()

def gameover():
    fin_juego = False
    #Musica gameover
    sonido_nivel1.stop()
    sonido_nivel2.stop()
    for e in zombies:
        e.sonido_zombie.stop()
    for m in modificadores:
        m.sonido_equipar.stop()
    for b in bosses:
        b.sonido_memesis.stop()
    if NIVEL == 1:
        for s in spawners:
            s.sonido_explosion.stop()
    sonido_gameover=pygame.mixer.Sound('gameover.ogg')
    sonido_gameover.play()
    fin=True
    img=pygame.image.load('gameover.jpg')
    while not fin_juego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.quit()
                    quit()
        fuente=pygame.font.Font(None,25)
        pantalla.blit(img,[0,0])
        texto=fuente.render('Presione la tecla S para salir',True,NEGRO)
        pantalla.blit(texto,[180,570])
        pygame.display.update()

def preludio():
    img1=pygame.image.load('preludio1.jpg')
    img2=pygame.image.load('preludio2.jpg')
    preludio=False
    imgcon=0
    sonido_preludio=pygame.mixer.Sound('preludio.ogg')
    sonido_preludio.play()
    while not preludio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    imgcon+=1
        if imgcon==0:
            pantalla.fill(NEGRO)
            pantalla.blit(img1,[0,0])
            pygame.display.flip()
        elif imgcon==1:
            pantalla.fill(NEGRO)
            pantalla.blit(img2,[0,0])
            pygame.display.flip()
        elif imgcon==2:
            sonido_preludio.stop()
            preludio=True
            menu_inicial=True
            controles=True
            fin=False
            pantalla.fill(NEGRO)
            pygame.display.flip()
        pygame.display.flip()

def interludio():
    img=pygame.image.load('interludio.jpg')
    interludio=False
    imgcon2=0
    sonido_interludio=pygame.mixer.Sound('interludio.ogg')
    sonido_interludio.play()
    while not interludio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    imgcon2+=1
        if imgcon2==0:
            pantalla.fill(NEGRO)
            pantalla.blit(img,[0,0])
            pygame.display.flip()
        elif imgcon2==1:
            sonido_nivel1.stop()
            sonido_interludio.stop()
            interludio=True
            menu_inicial=True
            fin=False
        pygame.display.flip()

def menuinicial():
    pantalla.fill(NEGRO)
    menu_inicial=False
    fondomenuinicial=pygame.image.load('survivor-logo.jpg')
    pygame.display.set_caption("Survivor")
    ClaseMenuInicial=MenuInicial()
    opciones=['Controles', 'Nuevo juego', 'Creditos', 'Salir']
    ClaseMenuInicial.opciones=opciones
    sonido_menu=pygame.mixer.Sound('survivor.ogg')
    sonido_menu.play()
    sonido_menu.set_volume(0.3)
    while not menu_inicial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_inicial = True
                fin = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ClaseMenuInicial.abajo()
                if event.key == pygame.K_UP:
                    ClaseMenuInicial.arriba()
                if event.key == pygame.K_RETURN:
                    ClaseMenuInicial.seleccion=ClaseMenuInicial.nop
        if ClaseMenuInicial.seleccion==1:
            sonido_menu.stop()
            menu_inicial=True
            pantalla.fill(NEGRO)
            controlesmenu()
        if ClaseMenuInicial.seleccion==2:
            sonido_menu.stop()
            menu_inicial=True
            pantalla.fill(NEGRO)
            preludio()
        if ClaseMenuInicial.seleccion==3:
            sonido_menu.stop()
            menu_inicial=True
            credits()
        if ClaseMenuInicial.seleccion==4:
            menu_inicial=True
            fin=True
            quit()
        reloj.tick(60)
        pantalla.fill(NEGRO)
        pantalla.blit(fondomenuinicial,[0,0])
        ClaseMenuInicial.draw(pantalla)
        pygame.display.flip()

def credits():
    creditos=False
    txtposy=300
    txt1posy=340
    txt2posy=360
    txt3posy=380
    txt4posy=700
    #Musica creditos
    sonido_creditos=pygame.mixer.Sound('creditos.ogg')
    sonido_creditos.set_volume(0.5)
    sonido_creditos.play()
    while not creditos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                creditos=True
                fin=True
                menu_inicial=True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sonido_creditos.stop()
                    creditos=True
                    menu_inicial=False
                    pantalla.fill(NEGRO)
                    pygame.display.flip()
                    menuinicial()

        fuente=pygame.font.Font(None,25)
        creditostxt=fuente.render('Creditos:',True,BLANCO)
        creditos1=fuente.render('Daniel E Cortés Aguirre',True,BLANCO)
        pantalla.fill(NEGRO)
        pantalla.blit(creditostxt,[252,txtposy])
        pantalla.blit(creditos1,[175,txt1posy])
        pygame.display.flip()
        txtposy-=2
        txt1posy-=2
        txt2posy-=2
        txt3posy-=2
        txt4posy-=2
        pygame.display.update()
        reloj.tick(20)

def disparo(jugador):

    if jugador.arma == 0:
        if jugador.power ==1:
            pow = 5
        else:
            pow = 20
    else:
        if jugador.power ==1:
            pow = 15
        else:
            pow = 30


    if jugador.arma == 0:
        vel=40
    else:
        vel=100

    if jugador.direccion==0 or jugador.direccion == 4:
        p1=jugador.rect.bottomleft
        b=Bala([p1[0]+11,p1[1]-20],[1,10],pow)
        b.vely=vel
    if jugador.direccion==1 or jugador.direccion ==5:
        p2=jugador.rect.midleft
        b=Bala([p2[0],p2[1]-10],[10,1],pow)
        b.velx=-vel
    if jugador.direccion==2 or jugador.direccion == 6:
        p3=jugador.rect.midright
        b=Bala([p3[0]-10,p3[1]],[10,1],pow)
        b.velx=vel
    if jugador.direccion==3 or jugador.direccion == 7:
        p4=jugador.rect.topright
        b=Bala([p4[0]-15,p4[1]+10],[1,10],pow)
        b.vely=-vel
    balas.add(b)
    if jugador.arma == 0:
        b.disparo2.play()
    else:
        b.disparo.play()


def CargarNivel (mp, mapa, t, mod1, mod2, mod3):
    i=0
    c=0
    for filas in mp:
        for e in filas:
            if mapa.get(e,'tipo') == 'vacio':
                c+=1
            else:
                fl=int(mapa.get(e,'fil'))
                cl=int(mapa.get(e,"col"))
                if (NIVEL == 1):
                    elemento=Bloque(t[fl][cl],[c*32,i*32])
                    elementos_mapa.add(elemento)

                if (NIVEL == 2):
                    if (fl == 15) and (cl == 5):
                        print('cree un generador en el nivel 2')
                        elemento=Bloque(t[fl][cl],[c*32,i*32])
                        spawners.add(elemento)
                c+=1
        c=0
        i+=1
    bot=Bonus(mod1,1,[320,768])
    poc=Bonus(mod2,2,[896,768])
    fl=Bonus(mod3,3,[896,448])
    modificadores.add(bot)
    modificadores.add(poc)
    modificadores.add(fl)

    if NIVEL == 1:
        l=Pared([192,192],[256,64])
        bloques_colision.add(l)

        l2=Pared([768,192],[256,64])
        bloques_colision.add(l2)

        l3=Pared([192,576],[256,64])
        bloques_colision.add(l3)

        l4=Pared([512,384],[192,64])
        bloques_colision.add(l4)

        l5=Pared([512,758],[192,64])
        bloques_colision.add(l5)

        l6=Pared([192,960],[256,64])
        bloques_colision.add(l6)

        l7=Pared([768,960],[256,64])
        bloques_colision.add(l7)

        l8=Pared([576,608],[32,8])
        bloques_colision.add(l8)

        l9=Pared([576,480],[64,8])
        bloques_colision.add(l9)

        l10=Pared([704,576],[32,40])
        bloques_colision.add(l10)
    else:
        #CARGAR spawners EN MAPA
        print('lvl 2')


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([WIDTH,HEIGHT])
    fin = False
    reloj= pygame.time.Clock()

    #Menu inicial
    menuinicial()

    #Musica nivel1
    sonido_nivel1=pygame.mixer.Sound('nivel1.ogg')
    sonido_nivel1.set_volume(0.3)
    sonido_nivel1.play(2)

    sonido_nivel2=pygame.mixer.Sound('nivel2.ogg')
    sonido_nivel2.set_volume(0.3)

    zombies_azules = pygame.sprite.Group()
    zombies_rojos = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    bosses=pygame.sprite.Group()

    modificadores=pygame.sprite.Group()
    fondos=pygame.sprite.Group()
    spawners=pygame.sprite.Group()
    elementos_mapa = pygame.sprite.Group()
    bloques_colision=pygame.sprite.Group()

    jugadores=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_m=pygame.sprite.Group()

    #Recorte del jugador
    archivo='rambo_1.png'
    archivo_enemigo_1='zombie_1.png'
    archivo_enemigo_2='zombie_2.png'
    archivo_boss='Memesis.png'
    #recorte(archivo,filas,columnas,anchocolumna,anchofila)
    m=recorte(archivo,8,6,48,67)
    m2=recorte(archivo_enemigo_1,4,12,48,67)
    m3=recorte(archivo_enemigo_2,4,12,48,67)
    #m[fila][columna]

    #Carga del MAPA con los elementos pequenos
    #que tienen y no tienen colision
    mapa=ConfigParser.ConfigParser()
    mapa.read('mapa.map')
    #archivo=mapa.get('info','img')
    terreno= 'forest_tiles.png'
    t=recorte(terreno,16,16,32,32)

    mapa2=ConfigParser.ConfigParser()
    mapa2.read('lab1.map')
    archivo_lab = 'lab1.png'
    lab=recorte(archivo_lab,16,16,32,32)

    #Carga del mapa con tumbas
    mapa3=ConfigParser.ConfigParser()
    mapa3.read('mapa3.map')
    gen ='tumba.png'
    tomb=recorte(gen,7,7,32,32)

    mp=mapa.get('info','mapa')
    mp=mp.split('\n')

    mp2=mapa2.get('info','mapa')
    mp2=mp2.split('\n')

    #Objetos de tipo fondo
    f1=pygame.image.load('fondobosque.png')
    f=Fondo(f1,[0,0])
    fondos.add(f)

    #jugador
    j1=Jugador(m,[WIDTH/2,(HEIGHT/2)+50])
    jugadores.add(j1)

    mod1=pygame.image.load('botiquin.png')
    mod2=pygame.image.load('pocion.png')
    mod3=pygame.image.load('flash.png')

    CargarNivel(mp, mapa, t, mod1, mod2, mod3)

    explosion='boom.png'
    ex=recorte(explosion,1,3,48,48)
    mp3=mapa3.get('info','mapa')
    mp3=mp3.split('\n')

    #CARGAR spawners EN MAPA
    i=0
    c=0
    for filas in mp3:
        for e in filas:
            if mapa3.get(e,'tipo') == 'vacio':
                c+=1
            else:
                fl=int(mapa3.get(e,'fil'))
                cl=int(mapa3.get(e,"col"))
                g=Spawn(tomb[fl][cl],ex,[c*32,i*32])
                spawners.add(g)
                c+=1
        c=0
        i+=1
    limited=WIDTH-90
    limiteizq=WIDTH-510
    limitesup=HEIGHT-510
    limiteinf=HEIGHT-90
    fuente= pygame.font.Font(None, 32)
    estado_zombie=0
    cont = 0

    tasa=40
    seg=0
    con=0
    lim=120
    Fuente=pygame.font.Font(None,32)

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    j1.vely=5
                    j1.velx=0
                    if (j1.arma == 0):
                        j1.direccion=0
                    else:
                        j1.direccion=4
                if event.key == pygame.K_UP:
                    j1.vely=-5
                    j1.velx=0
                    if (j1.arma == 0):
                        j1.direccion=3
                    else:
                        j1.direccion=7
                if event.key == pygame.K_LEFT:
                    j1.velx=-5
                    j1.vely=0
                    if (j1.arma == 0):
                        j1.direccion=1
                    else:
                        j1.direccion=5
                if event.key == pygame.K_RIGHT:
                    j1.velx=5
                    j1.vely=0
                    if (j1.arma == 0):
                        j1.direccion=2
                    else:
                        j1.direccion=6

                if event.key == pygame.K_SPACE:
                    for j in jugadores:
                        disparo(j)
                if event.key == pygame.K_v:
                    j1.arma=1
                    if (j1.direccion == 0):
                        j1.direccion = 4
                    if (j1.direccion == 3):
                        j1.direccion = 7
                    if (j1.direccion == 1):
                        j1.direccion = 5
                    if (j1.direccion == 2):
                        j1.direccion = 6
                if event.key == pygame.K_b:
                    j1.arma=0
                    if (j1.direccion == 4):
                        j1.direccion = 0
                    if (j1.direccion == 7):
                        j1.direccion = 3
                    if (j1.direccion == 5):
                        j1.direccion = 1
                    if (j1.direccion == 6):
                        j1.direccion = 2

                if event.key == pygame.K_p:
                    pausa()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    j1.vely=0
                    j1.velx=0
                    f.velx=0
                if event.key == pygame.K_LEFT:
                    j1.vely=0
                    j1.velx=0
                    f.velx=0
                if event.key == pygame.K_DOWN:
                    j1.vely=0
                    j1.velx=0
                    f.vely=0
                if event.key == pygame.K_UP:
                    j1.vely=0
                    j1.velx=0
                    f.vely=0

        #Contrareloj
        seg=con/tasa
        val=lim-seg
        txt='Tiempo: '+str(val)
        if val<10:
            texto=Fuente.render(txt,True,ROJO)
        if val>=10:
            texto=Fuente.render(txt,True,BLANCO)
        if val<0:
            gameover()
        pantalla.blit(texto,[430,10])
        pygame.display.flip()
        con+=1

        #############LIMITES DEL MAPA###########################
        if j1.rect.right > limited:
            j1.rect.right=limited
            f.velx=-5
            #limite derecho jugador 1
            if (WIDTH - f.rect.width) >(f.rect.x):
                f.velx=0
        elif j1.rect.left < limiteizq:
            j1.rect.left=limiteizq
            f.velx=5
            #limite izquierdo jugador 1
            if f.rect.x==0:
                f.velx=0
        else:
            f.velx=0

        if j1.rect.bottom > limiteinf:
            j1.rect.bottom=limiteinf
            f.vely=-5
            #limite inferior
            if (HEIGHT - f.rect.height) > (f.rect.y):
                f.vely=0

        elif j1.rect.top < limitesup:
            j1.rect.top=limitesup
            f.vely=5
            #limite superior
            if f.rect.y==0:
                f.vely=0
        else:
            f.vely=0

        for elemento in elementos_mapa:
            elemento.velx=f.velx
            elemento.vely=f.vely

        for e in zombies:
            e.velx=f.velx
            e.vely=f.vely

        for n in bosses:
            n.velx=f.velx
            n.vely=f.vely

        for g in spawners:
            g.velx=f.velx
            g.vely=f.vely

        for m in modificadores:
            m.velx=f.velx
            m.vely=f.vely

        for p in bloques_colision:
            p.velx=f.velx
            p.vely=f.vely

        #########LIMPIEZA DE BALAS FUERA DE LA PANTALLA##################
        for b in balas:
            if b.rect.x > WIDTH + 10:
                balas.remove(b)
            if b.rect.x < WIDTH -610:
                balas.remove(b)
            if b.rect.y > HEIGHT + 10:
                balas.remove(b)
            if b.rect.y < HEIGHT -610:
                balas.remove(b)

        #Creacion de rivales desde spawn
        for s in spawners:
            if s.temp<=0:
                pos=s.rect.center
                e=Enemigo(m2,pos,5, 1.5)
                zombies.add(e)
                zombies_azules.add(e)
                e.sonido_zombie.play()
                s.temp=random.randrange(800)

        for s in spawners:
            if s.temp1<=0:
                pos=s.rect.center
                e=Enemigo(m3,pos,10, 3)
                zombies.add(e)
                zombies_rojos.add(e)
                s.temp1=random.randrange(2000)

        #Balas del Memesis
        for n in bosses:
            if n.temp <=0:
                if n.direccion==0:
                    p1=n.rect.bottomleft
                    b=Bala([p1[0]+11,p1[1]-20],[1,10],20)
                    b.vely=40
                if n.direccion==1:
                    p2=n.rect.midleft
                    b=Bala([p2[0],p2[1]-10],[10,1],20)
                    b.velx=-40
                if n.direccion==2:
                    p3=n.rect.midright
                    b=Bala([p3[0]-10,p3[1]],[10,1],20)
                    b.velx=40
                if n.direccion==3:
                    p4=n.rect.topright
                    b=Bala([p4[0]-15,p4[1]+10],[1,10],20)
                    b.vely=-40
                balas_m.add(b)
                b.disparo3.play()
                n.temp=random.randrange(100)

        #LIMPIEZA DE LAS BALAS DE MEMESIS
        for b in balas_m:
            if b.rect.x > WIDTH + 10:
                balas_m.remove(b)
            if b.rect.x < WIDTH -610:
                balas_m.remove(b)
            if b.rect.y > HEIGHT + 10:
                balas_m.remove(b)
            if b.rect.y < HEIGHT -610:
                balas_m.remove(b)
        #colision enemigos con jugador, ataque cercano
        #estado_zombie = 0
        #print cont
        if (estado_zombie == 1 and cont < 5):
            cont = cont + 1
            estado_zombie = 1
            #print cont
        else:
            cont = 0
            estado_zombie = 0
        for e in zombies:
            col_e=pygame.sprite.spritecollide(e,jugadores,False)
            for p in col_e:
                if (e.speed > 0) and (e.direccion == 2) and (e.rect.right-12 > p.rect.left):
                    e.rect.right = p.rect.left+12
                    p.rect.x = p.rect.x + 25
                    e.velx = 0
                    estado_zombie = 1

                    if p.salud > 0:
                        p.salud -= e.damage
                        print(p.salud)
                    else:
                        jugadores.remove(p)
                        gameover()

                if (e.speed > 0) and (e.direccion == 1) and (e.rect.left+12 < p.rect.right):
                    e.rect.left = p.rect.right-12
                    p.rect.x = p.rect.x - 25
                    e.velx = 0
                    estado_zombie = 1
                    if p.salud > 0:
                        p.salud -= e.damage
                        print(p.salud)
                    else:
                        jugadores.remove(p)
                        gameover()

                if (e.speed > 0) and (e.direccion == 0) and (e.rect.bottom-16 > p.rect.top):
                    e.rect.bottom = p.rect.top+16
                    p.rect.y = p.rect.y + 25
                    e.velx = 0
                    estado_zombie = 1
                    if p.salud > 0:
                        p.salud -= e.damage
                        print(p.salud)
                    else:
                        jugadores.remove(p)
                        gameover()

                if (e.speed > 0) and (e.direccion == 3) and (e.rect.top+16 < p.rect.bottom):
                    e.rect.top = p.rect.bottom-16
                    p.rect.y = p.rect.y - 25
                    e.velx = 0
                    estado_zombie = 1
                    if p.salud > 0:
                        p.salud -= e.damage
                        print(p.salud)
                    else:
                        jugadores.remove(p)
                        gameover()

        #Colision de balas de Memesis con el jugador
        for b in balas_m:
            b_to_player=pygame.sprite.spritecollide(b,jugadores,False,pygame.sprite.collide_rect_ratio(1.5))
            for j in b_to_player:
                if (b.rect.top < j.rect.bottom) and (b.vely<0):
                    b.rect.top = j.rect.bottom
                elif (b.rect.bottom > j.rect.top) and (b.vely>0):
                    b.rect.bottom = j.rect.top
                elif (b.rect.right > j.rect.left) and (b.velx>0):
                    b.rect.right =  j.rect.left
                elif (b.rect.left < j.rect.right) and (b.velx<0):
                    b.rect.left = j.rect.right
                if j.salud >0:
                    j.salud -= b.damage
                    balas_m.remove(b)
                else:
                    jugadores.remove(j)
                    gameover()

        #Memesis siguiendo al jugador
        estado_boss=0
        for n in bosses:
            if (estado_boss == 0):
                n.move_towards_player(j1)
        #print estado_zombie
        #colision balas con enemigos
        for b in balas:
            b_to_en=pygame.sprite.spritecollide(b,zombies,False,pygame.sprite.collide_rect_ratio(1.5))
            for e in b_to_en:
                if (b.rect.top < e.rect.bottom) and (b.vely<0):
                    b.rect.top = e.rect.bottom
                    e.vely=-40
                elif (b.rect.bottom > e.rect.top) and (b.vely>0):
                    b.rect.bottom = e.rect.top
                    e.vely=40
                elif (b.rect.right > e.rect.left) and (b.velx>0):
                    b.rect.right =  e.rect.left
                    e.velx=40
                elif (b.rect.left < e.rect.right) and (b.velx<0):
                    b.rect.left = e.rect.right
                    e.velx=-40
                if e.salud >0:
                    e.salud -= b.damage
                    #print(e.salud)
                    balas.remove(b)
                else:
                    zombies.remove(e)

        #Colision de balas del jugador con Memesis
        for b in balas:
            b_to_boss=pygame.sprite.spritecollide(b,bosses,False,pygame.sprite.collide_rect_ratio(1.5))
            for n in b_to_boss:
                if (b.rect.top < n.rect.bottom) and (b.vely<0):
                    b.rect.top = n.rect.bottom
                elif (b.rect.bottom > n.rect.top) and (b.vely>0):
                    b.rect.bottom = n.rect.top
                elif (b.rect.right > n.rect.left) and (b.velx>0):
                    b.rect.right =  n.rect.left
                elif (b.rect.left < n.rect.right) and (b.velx<0):
                    b.rect.left = n.rect.right
                if n.salud >0:
                    n.salud -= b.damage
                    print(n.salud)
                    balas.remove(b)
                else:
                    bosses.remove(n)
                    n.sonido_memesis.stop()
                    victory()

        #Colision de balas con el SPAWN
        for b in balas:
            b_to_sp=pygame.sprite.spritecollide(b,spawners,False)
            for s in b_to_sp:
                if (b.rect.top < s.rect.bottom) and (b.vely<0):
                    b.rect.top = s.rect.bottom

                elif (b.rect.bottom > s.rect.top) and (b.vely>0):
                    b.rect.bottom = s.rect.top

                elif (b.rect.right > s.rect.left) and (b.velx>0):
                    b.rect.right = s.rect.left

                elif (b.rect.left < s.rect.right) and (b.velx<0):
                    b.rect.left = s.rect.right

                if s.salud >0:
                    s.salud -= b.damage
                    print(s.salud)
                    balas.remove(b)
                else:
                    if (NIVEL == 1):
                        s.sonido_explosion.play()
                    spawners.remove(s)
        c=0
        if len(spawners)==0:
            #limpiarMundo(jugadores, spawners, zombies, elementos_mapa, fondos, bloques_colision, modificadores)
            if (NIVEL == 1):
                for j in jugadores:
                    jugadores.remove(j)
                    print('Jugador eliminado')
                for z in zombies:
                    zombies.remove(z)
                    print(' Zombies eliminados')
                for e in elementos_mapa:
                    elementos_mapa.remove(e)
                    print('elementos eliminados')
                for f in fondos:
                    fondos.remove(f)
                    print('Eliminar fondo')
                for b in bloques_colision:
                    bloques_colision.remove(b)
                for m in modificadores:
                    modificadores.remove(m)
                NIVEL = 2
                tasa=40
                seg=0
                con=0
                lim=120
                sonido_nivel1.stop()
                interludio()
                sonido_nivel2.play(2)
                pantalla.fill(NEGRO)
                fondo2=pygame.image.load('pisolab.png')
                f=Fondo(fondo2,[0,0])
                fondos.add(f)
                CargarNivel(mp2, mapa2, lab, mod1, mod2, mod3)
                m=recorte(archivo,8,6,48,67)
                j1=Jugador(m,[WIDTH/2,(HEIGHT/2)+50])
                jugadores.add(j1)
                #m2=recorte(archivo_enemigo_1,4,12,48,67)
                m4=recorte(archivo_boss,4,6,84,134)
                b=Boss(m4,[608,608],1.5)
                bosses.add(b)
                b.sonido_memesis.play(2)
            elif(NIVEL == 2) and (c == 0):
                c = c + 1
                print('spawners destruidos')

        #Colision del jugador con modificadores
        j_to_mod=pygame.sprite.spritecollide(j1,modificadores,True)
        for m in j_to_mod:
            if m.tipo == 1:
                j1.salud += m.bon
            if m.tipo == 2:
                j1.salud -= m.bon
            elif m.tipo == 3:
                j1.powerup()
            m.sonido_equipar.play()

        #Colision de Jugador con el mundo
        for j in jugadores:
            ls_col=pygame.sprite.spritecollide(j,bloques_colision,False)
            for l in ls_col:
                if j.rect.bottom > l.rect.top and (j.direccion==0 or j.direccion==4):
                    j.rect.bottom = l.rect.top
                    j.vely=0
                elif j.rect.top < l.rect.bottom and (j.direccion==3 or j.direccion==7):
                    j.rect.top = l.rect.bottom
                    j.vely=0
                elif j.rect.right > l.rect.left and (j.direccion==2 or j.direccion==6):
                    j.rect.right = l.rect.left
                    j.velx=0
                elif j.rect.left < l.rect.right and (j.direccion==1 or j.direccion==5):
                    j.rect.left = l.rect.right
                    j.velx=0

        #Colision Zombies con el mundo
        for z in zombies:
            ls_col=pygame.sprite.spritecollide(z,bloques_colision,False)
            for b in ls_col:
                if z.rect.bottom > b.rect.top and z.direccion == 0:
                    z.rect.bottom = b.rect.top
                    if j1.rect.x > z.rect.x:
                        z.rect.x+=2
                        z.direccion = 2
                    else:
                        z.rect.x-=2
                        z.direccion = 1
                elif z.rect.top < b.rect.bottom and z.direccion == 3:
                    z.rect.top = b.rect.bottom+1
                    if j1.rect.x > z.rect.x:
                        z.rect.x+=2
                        z.direccion = 2
                    else:
                        z.rect.x-=2
                        z.direccion = 1
                elif z.rect.right > b.rect.left and z.direccion == 2:
                    z.rect.right = b.rect.left
                    if j1.rect.y > z.rect.y:
                        z.rect.y+=2
                        z.direccion = 0
                    else:
                        z.rect.y-=2
                        z.direccion = 3
                elif z.rect.left < b.rect.right and z.direccion == 1:
                    z.rect.left = b.rect.right
                    if j1.rect.y > z.rect.y:
                        z.rect.y+=2
                        z.direccion = 0
                    else:
                        z.rect.y-=2
                        z.direccion = 3

        jugadores.update()
        balas.update()
        balas_m.update()
        fondos.update()
        #print estado_zombie
        zombies.update([j1.rect.x, j1.rect.y], estado_zombie)
        bosses.update([j1.rect.x, j1.rect.y], estado_boss)
        elementos_mapa.update()
        spawners.update()
        modificadores.update()
        bloques_colision.update()
        fondos.draw(pantalla)
        elementos_mapa.draw(pantalla)
        modificadores.draw(pantalla)
        jugadores.draw(pantalla)
        spawners.draw(pantalla)
        zombies.draw(pantalla)
        bosses.draw(pantalla)
        balas.draw(pantalla)
        balas_m.draw(pantalla)
        #bloques_colision.draw(pantalla)
        s_salud='Salud: '+ str(j1.salud)
        texto=fuente.render(s_salud, True, BLANCO)
        pantalla.blit(texto,[50,10])
        pygame.display.flip()
        reloj.tick(40)

#FILA 21 COLUMNA 25 MITAD DEL MAPA

