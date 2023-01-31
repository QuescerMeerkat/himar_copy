import pygame
from pygame.locals import *
from bullet import *

class Player(pygame.sprite.Sprite):
    player = 1
    def __init__(self, size, color, position, health):
        self.player = Player.player
        Player.player += 1
        super().__init__()
        self.image = pygame.Surface(size)
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(center = position)
        self.velocity = -5
        self.health = health
        self.animating = False
        self.dt = 0
        self.limit = 20

    def shoot(self):
        return Bullet(self.rect.center, 10, (250, 20, 40), 1)

    def damage(self, amount):
        self.health -= amount
        self.animating = True
        if self.health <= 0:
            self.kill()

    def move(self, swapchain_extent):
        keys = pygame.key.get_pressed()

        if self.player == 1:
            if keys[K_w] and self.rect.top > 0:
                self.rect.y += self.velocity
            if keys[K_s] and self.rect.bottom < swapchain_extent[1]:
                self.rect.y -= self.velocity

        if self.player == 2:
            if keys[K_UP]:
                self.rect.y += self.velocity
            if keys[K_DOWN]:
                self.rect.y -= self.velocity
        if self.rect.top <= 0:
            self.rect.y -= self.velocity
        if self.rect.bottom >= swapchain_extent[1]:
            self.rect.y += self.velocity

    def play_animation(self):
        if self.dt == self.limit:
            self.dt = 0
            self.animating = False
            self.image.fill(self.color)
            return
        self.image.fill((250, 20, 50))
        self.dt += 1

    def update(self, swapchain_extent):
        self.move(swapchain_extent)
        if self.animating:
            self.play_animation()