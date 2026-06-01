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

class Bala(pygame.sprite.Sprite):

    def __init__(self,punto,md,dano,cl=BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(md)
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=punto[0]
        self.rect.y=punto[1]
        self.velx=0
        self.vely=0
        self.disparo=pygame.mixer.Sound('disparo.ogg')
        self.disparo2=pygame.mixer.Sound('disparos_2.ogg')
        self.disparo3=pygame.mixer.Sound('shotgun.ogg')
        self.disparo.set_volume(0.3)
        self.disparo2.set_volume(0.3)
        self.disparo3.set_volume(0.3)
        self.damage=dano

    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

