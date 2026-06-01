import pygame

'''
CLASE BALA
'''

NEGRO=[0,0,0]
VERDE=[0,255,0]
BLANCO=[255,255,255]
AMARILLO=[255,255,0]
ROJO=(255,0,0)
AZUL=(0,0,255)



class Bonus(pygame.sprite.Sprite):
    def __init__(self,imagen,tipo,pos):
        pygame.sprite.Sprite.__init__(self)
        self.tipo=tipo
        self.image=imagen
        self.bon=0
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.sonido_equipar=pygame.mixer.Sound('sonido_equipar.ogg')

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        if self.tipo==2:
            self.bon=10
        elif self.tipo==1:
            self.bon=20

