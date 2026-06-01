import pygame
from ClaseBala import*

'''
CLASE JUGADOR
'''


class Jugador(pygame.sprite.Sprite):
    def __init__(self,m,pto):
        pygame.sprite.Sprite.__init__(self)
        self.direccion=0
        self.col=0
        self.limite=[]
        self.m=m
        #print 'Llegue hasta aqui'
        self.image=self.m[self.direccion][self.col]
        #print 'Llegue hasta aqui'
        #print self.direccion
        #print self.col
        self.rect=self.image.get_rect()
        self.radius=int((self.rect.width * .30)/ 2)
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.velx=0
        self.vely=0
        self.salud=100
        self.power=1
        self.arma=0


    def update(self):
        #if (arma == 0):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.image=self.m[self.direccion][self.col]
        if self.vely!=0 and (self.direccion==0 or self.direccion==4):
            if self.col<5:
                self.col+=1
            else:
                self.col=0

        elif self.velx!=0 and (self.direccion==1 or self.direccion==5):
            if self.col<5:
                self.col+=1
            else:
                self.col=0

        elif self.velx!=0 and (self.direccion==2 or self.direccion==6):
            if self.col<5:
                self.col+=1
            else:
                self.col=0
        elif self.vely!=0 and (self.direccion==3 or self.direccion==7):
            if self.col<5:
                self.col+=1
            else:
                self.col=0

        else:
            self.col=0


    def powerup(self):
        self.power+=1

