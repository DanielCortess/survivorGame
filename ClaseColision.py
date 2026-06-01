import pygame

WIDTH=600
HEIGHT=600
NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
ROJO=(255,0,0)
AZUL=(0,0,255)

class Pared(pygame.sprite.Sprite):
    def __init__(self, pto,dim):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.dr=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

