import random

import pygame
import sys

from firework import Firework

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

preto = (0, 0, 0)

pygame.display.set_caption("Linha Branca")

mousePos = (0, 0)
fogos = []

clock = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            print(mousePos)

            posX = random.randint(0, largura)
            fogos.append(Firework((posX, altura), mousePos))

    tela.fill(preto)

    for f in fogos:
        f.update()
        f.draw(tela)

    pygame.display.flip()
    clock.tick(60)
