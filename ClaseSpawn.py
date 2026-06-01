import pygame
import random

'''
CLASE SPAWN
'''

NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
ROJO=(255,0,0)
AZUL=(0,0,255)
TRANSPARTENT=(0,0,0,0)

class Spawn(pygame.sprite.Sprite):
    def __init__(self,imagen,m,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        #Explosion
        self.direccion=0
        self.col=0
        self.m=m
        self.image2=self.m[self.direccion][self.col]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.salud=100
        self.temp=random.randrange(200)
        self.temp1=random.randrange(500)
        self.limite=[2]
        self.sonido_explosion=pygame.mixer.Sound('explosion.ogg')

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.temp-=1
        self.temp1-=1
        if self.salud ==0:
            self.image = self.m[self.direccion][self.col]
            if self.col <2:
                self.col+=1
            elif self.col==2:
                self.col=0

