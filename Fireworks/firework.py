import pygame
from random import randint, uniform

from bolinhas import Bolinha


class Firework:

    def __init__(self, pos_inicial, pos_final):
        self.pos_inicial = pygame.Vector2(pos_inicial)
        self.pos_final =pygame.Vector2(pos_final)
        self.pos_atual = pygame.Vector2(pos_inicial)
        self.cor = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.explodiu = False
        self.bolinhas = []

    def update(self):
        direcao = (self.pos_final - self.pos_inicial).normalize() * 500

        if self.pos_atual.y > self.pos_final.y:
            self.pos_atual += direcao * (1 / 60)

        elif not self.explodiu and self.pos_atual.y <= self.pos_final.y:
            self.explodiu = True
            self.explodir()
        else:
            for bol in self.bolinhas:
                bol.vel += bol.vel.normalize() * -1.7 * (1/60) # conta mover
                bol.vel.y += 10 * (1/60) # add gravidade
                bol.pos += bol.vel * 5 * (1/60) # mover de verdade

    def draw(self, tela):
        if not self.explodiu:
            pygame.draw.line(tela, self.cor, self.pos_inicial, self.pos_atual, 5)
        else:
            for bol in self.bolinhas:
                pygame.draw.circle(tela, bol.cor, bol.pos, bol.tam, 0)


    def explodir(self):
        quantidade = randint(1000, 2000)

        for bol in range(quantidade):

            dir_vel = pygame.Vector2(uniform(-10, 10), uniform(-10, 10))

            while dir_vel.length() > 10:
                dir_vel = pygame.Vector2(uniform(-10, 10), uniform(-10, 10))

            tam = uniform(1.5, 1.9)
            nova_bolinha = Bolinha(self.pos_atual.copy(), dir_vel, tam, self.cor)

            self.bolinhas.append(nova_bolinha)