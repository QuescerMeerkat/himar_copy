import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite, pygame.sprite.Group):
    def __init__(self, position, radius, color, damage):
        super().__init__()
        self.image = pygame.Surface((radius, radius))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = position)
        self.radius = radius
        self.color = color
        self.velocity = 7
        self.damage = damage

    def move(self, player_number):
        if player_number == 1: self.rect.x += self.velocity
        elif player_number == 2: self.rect.x -= self.velocity

    def update(self, player_number, players):
        self.move(player_number)
        if self.rect.colliderect(players[player_number % 2].rect):
            self.kill()
            players[player_number % 2].damage(self.damage)