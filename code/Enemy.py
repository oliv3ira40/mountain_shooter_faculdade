#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, window):
        super().__init__(name, position)
        self.window = window
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.direction = 1  # 1 para baixo, -1 para cima

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3':
            if self.direction == 1:
                self.rect.centery += ENTITY_SPEED[self.name] * 2  # Desce com o dobro da velocidade
            else:
                self.rect.centery -= ENTITY_SPEED[self.name]  # Sobe com a velocidade normal

            if self.rect.top <= 0:
                self.rect.top = 0
                self.direction = 1  # Muda a direção para baixo
            elif self.rect.bottom >= self.window.get_height():
                self.rect.bottom = self.window.get_height()
                self.direction = -1  # Muda a direção para cima

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
