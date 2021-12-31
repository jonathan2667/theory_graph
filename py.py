import pygame
from random import randrange
import random

screen = pygame.display.set_mode((2500, 800))

RED = (255, 0, 0)
GREEN = (0, 255, 0)

running = 1

x1 = 0
x2 = 400
val = 10

cnt = 0

while running:
     event = pygame.event.poll()
     if event.type == pygame.QUIT:
         running = 0

     if cnt < 300:
        cnt = cnt + 1
        for i in range(1):
             r = randrange(3)
             if r == 0:
                pygame.draw.line(screen, RED, (x1, x2), (x1 + val, x2 + val))
                x1 = x1 + val
                x2 = x2 + val
             elif r == 1:
                pygame.draw.line(screen, RED, (x1, x2), (x1 + val, x2 - val))
                x1 = x1 + val
                x2 = x2 - val
             else:
                 pygame.draw.line(screen, RED, (x1, x2), (x1 + val, x2))
                 x1 = x1 + val

     else:
        cnt = 0
        x1 = 0
        x2 = 400
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        RED = (r, g, b)

     pygame.display.update()
