import pygame
import random

'''
CLASE BlOQUE
'''

class Bloque(pygame.sprite.Sprite):
    def __init__(self, imagen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.radius=int((self.rect.width * .60 )/ 2)
        self.temp=random.randrange(200)
        self.temp1=random.randrange(500)
        self.salud=100
        #self.sonido_explosion=pygame.mixer.Sound('sonido_explosion.ogg')


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

