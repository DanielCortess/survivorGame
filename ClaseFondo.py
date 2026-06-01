import pygame

'''
CLASE Fondo
'''

class Fondo(pygame.sprite.Sprite):
    def __init__(self,img, pto):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=pto[0]
        self.rect.y=pto[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

