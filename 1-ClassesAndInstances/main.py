import os
import time
import pygame
from pygame.locals import *

### Setup Pygame:
pygame.init()

keys_pressed = []

screen_width = 1300
screen_height = 900

screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()
fps = 30

bg_color = [102, 214, 255]
running = True

playerSprite = pygame.image.load("img/plane.png")
playerRect = playerSprite.get_rect()
playerSpeed = 10



### Class Plane:
class Plane:
    _health = 150
    _speed = 250
    _damage = 10

    def Message(this):
        print("Key registrating...")


#    def Attack(this):

    def __init__(self, HP):

        self._health = HP



while running:

  
    Spitfire = Plane(200)

    Spitfire.__init__(200)

    keys_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


## Keys Pressed----------------------
    if keys_pressed[K_UP] or keys_pressed == ord("w"):
        playerRect.y -= playerSpeed
        Spitfire.Message()
    elif keys_pressed[K_DOWN] or keys_pressed == ord("s"):
        playerRect.y += playerSpeed
        Spitfire.Message()

    if keys_pressed[K_LEFT] or keys_pressed == ord("a"):
        playerRect.x -= playerSpeed
        Spitfire.Message()
    elif keys_pressed[K_RIGHT] or keys_pressed == ord("d"):
        playerRect.x += playerSpeed
        Spitfire.Message()
## ----------------------------------

    screen.fill(bg_color)
    screen.blit(playerSprite, playerRect)

    pygame.display.flip()

    clock.tick(fps)