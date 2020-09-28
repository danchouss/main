import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

rect(screen, (255, 255, 255), (0, 0, 800, 800))
circle(screen, (255, 255, 0), (400, 400), 200)
rect(screen, (0, 0, 0), (300, 500, 200, 40))
circle(screen, (255, 0, 0), (300, 350), 40)
circle(screen, (0, 0, 0), (300, 350), 15)
circle(screen, (255, 0, 0), (500, 350), 35)
circle(screen, (0, 0, 0), (500, 350), 15)
line(screen, (0, 0, 0), (200, 244), (360, 325), 20)
line(screen, (0, 0, 0), (600, 275), (425, 325), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

