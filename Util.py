import pygame
import configparser as ConfigParser
import math
from ClaseJugador import *
from ClaseBala import *
from ClaseEnemigo import *
from ClaseFondo import *
from ClaseBloque import *
from ClaseSpawn import *

WIDTH=600
HEIGHT=600
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
ROJO=(255,0,0)
AZUL=(0,0,255)
origen=[WIDTH/2,HEIGHT/2]

def CargarBloques(mp, mapa, t, elementos_mapa):
    i=0
    c=0
    for filas in mp:
        for e in filas:
            if mapa.get(e,'tipo') == 'vacio':
                c+=1
            else:
                fl=int(mapa.get(e,'fil'))
                cl=int(mapa.get(e,"col"))
                elemento=Bloque(t[fl][cl],[c*32,i*32])
                elementos_mapa.add(elemento)
                c+=1
        c=0
        i+=1

