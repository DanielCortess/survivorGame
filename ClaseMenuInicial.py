import pygame


BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)


class MenuInicial(object):
    def __init__(self):
        self.opciones = []
        self.nop = 1
        self.seleccion = 0
        self.fuente = pygame.font.Font(None, 40)

    def abajo(self):
        if not self.opciones:
            return
        self.nop += 1
        if self.nop > len(self.opciones):
            self.nop = 1

    def arriba(self):
        if not self.opciones:
            return
        self.nop -= 1
        if self.nop < 1:
            self.nop = len(self.opciones)

    def draw(self, pantalla):
        y = 360
        for i, opcion in enumerate(self.opciones, start=1):
            color = AMARILLO if i == self.nop else BLANCO
            texto = self.fuente.render(opcion, True, color)
            rect = texto.get_rect(center=(300, y))
            pantalla.blit(texto, rect)
            y += 40

