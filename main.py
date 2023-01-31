import pygame, sys
from pygame.locals import *
from player import *

def terminate(msg):
  print(msg)
  pygame.quit()
  sys.exit()

def game_over(player):
  terminate("Player " + str(player) + " won!")

pygame.init()
swapchain_extent = (800, 600)
swapchain = pygame.display.set_mode(swapchain_extent)
pygame.display.set_caption("Himar's game but code is slightly better")

clock = pygame.time.Clock()
fps = 60

player_1 = Player([10, 100], [255, 255, 255], [50, 300], 40)
player_2 = Player([10, 100], [255, 255, 255], [750, 300], 40)
players = [player_1, player_2]

players_group = pygame.sprite.Group()
players_group.add(player_1)
players_group.add(player_2)

player_1_bullets = pygame.sprite.Group()
player_2_bullets = pygame.sprite.Group()

first_frame = True
while True:
  swapchain.fill([0, 0, 0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        terminate("Program terminated with exit code 0.")

  if pygame.key.get_pressed()[K_LSHIFT]:
    player_1_bullets.add(player_1.shoot())
  if pygame.key.get_pressed()[K_RSHIFT]:
    player_2_bullets.add(player_2.shoot())

  player_1_bullets.update(1, players)
  player_2_bullets.update(2, players)
  players_group.update(swapchain_extent)

  if not player_1.alive():
    game_over(2)
  elif not player_2.alive():
    game_over(1)

  player_2_bullets.draw(swapchain)
  player_1_bullets.draw(swapchain)
  players_group.draw(swapchain)

  pygame.display.flip()
  clock.tick(fps)
  first_frame = False