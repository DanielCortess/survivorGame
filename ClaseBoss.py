import pygame
import math
import random

'''
CLASE BOSS
'''

NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
ROJO=(255,0,0)
AZUL=(0,0,255)

class Boss(pygame.sprite.Sprite):
    def __init__(self,m,punto,speed):
        pygame.sprite.Sprite.__init__(self)
        self.direccion=0
        self.col=0
        self.limite=[]
        self.m=m
        self.image=self.m[self.direccion][self.col]
        self.rect=self.image.get_rect()
        self.rect.x=punto[0]
        self.rect.y=punto[1]
        self.radius=600
        self.velx=0
        self.vely=0
        self.reloj=pygame.time.Clock()
        self.sonido_memesis=pygame.mixer.Sound('memesis.ogg')
        #self.distancia_jugador=600
        self.speed=speed
        self.salud = 500
        self.temp=random.randrange(100)


    def update(self, posicion_jugador, estado_boss):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.temp-=1
        self.image=self.m[self.direccion][self.col]

        if (estado_boss == 0):
            col=0
            if (posicion_jugador[0] >= self.rect.x) and (posicion_jugador[1] <= self.rect.y):
                if (abs(posicion_jugador[0] - self.rect.x) > abs(posicion_jugador[1] - self.rect.y)):
                    self.direccion = 2
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0
                else:
                    self.direccion = 3
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0

            if (posicion_jugador[0] >= self.rect.x) and (posicion_jugador[1] >= self.rect.y):
                if (abs(posicion_jugador[0] - self.rect.x) > abs(posicion_jugador[1] - self.rect.y)):
                    self.direccion = 2
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0
                else:
                    self.direccion = 0
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0

            if (posicion_jugador[0] <= self.rect.x) and (posicion_jugador[1] >= self.rect.y):
                if (abs(posicion_jugador[0] - self.rect.x) > abs(posicion_jugador[1] - self.rect.y)):
                    self.direccion = 1
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0
                else:
                    self.direccion = 0
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0

            if (posicion_jugador[0] <= self.rect.x) and (posicion_jugador[1] <= self.rect.y):
                if (abs(posicion_jugador[0] - self.rect.x) > abs(posicion_jugador[1] - self.rect.y)):
                    self.direccion = 1
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0
                else:
                    self.direccion = 3
                    if self.col<5:
                        self.col+=1
                    else:
                        self.col=0


    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        try:
            dx, dy = dx / dist, dy / dist  # Normalize.
        except ZeroDivisionError:
            return False
        # Move along this normalized vector towards the player at current speed.
        self.rect.x = self.rect.x + (dx * self.speed)
        self.rect.y = self.rect.y + (dy * self.speed)

