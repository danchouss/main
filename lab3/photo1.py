import pygame
from pygame.draw import *
from pygame import Color
import math as m

pygame.init()
FPS = 30
screen = pygame.display.set_mode((800, 1100))

rect(screen, (119, 186, 208), (0, 0, 800, 1100))
rect(screen, (102, 197, 121), (0, 300, 800, 900))
size = width, height = (260, 200)
dog_surface = pygame.Surface(size)
size = width, height = (800, 400)
fence_surface = pygame.Surface(size)


def dog(r):
    t = r

    if 1 > r > 0:
        r = 1
    else:
        r = abs(r)
        r = int(r)

    ellipse(dog_surface, (107, 103, 85), (int(t * 0), int(t * 155), int(t * 50), int(t * 20)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 10), int(t * 62), int(t * 50), int(t * 100)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 90), int(t * 175), int(t * 50), int(t * 20)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 100), int(t * 82), int(t * 50), int(t * 100)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 20), int(t * 35), int(t * 180), int(t * 80)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 140), int(t * 15), int(t * 100), int(t * 70)))
    circle(dog_surface, (107, 103, 85), (int(t * 230), int(t * 80)), int(t * 25))
    circle(dog_surface, (107, 103, 85), (int(t * 150), int(t * 42)), int(t * 25))
    ellipse(dog_surface, (107, 103, 85), (int(t * 240), int(t * 92), int(t * 15), int(t * 60)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 215), int(t * 145), int(t * 35), int(t * 15)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 185), int(t * 65), int(t * 15), int(t * 60)))
    ellipse(dog_surface, (107, 103, 85), (int(t * 160), int(t * 118), int(t * 35), int(t * 15)))
    rect(dog_surface, (107, 103, 85), (int(t * 22), int(t * 0), int(t * 95), int(t * 95)))
    rect(dog_surface, (0, 0, 0), (int(t * 22), int(t * 0), int(t * 95), int(t * 95)), r * 1)
    ellipse(dog_surface, (107, 103, 85), (int(t * 5), int(t * 0), int(t * 30), int(t * 35)))
    ellipse(dog_surface, (0, 0, 0), (int(t * 5), int(t * 0), int(t * 30), int(t * 35)), r * 1)
    ellipse(dog_surface, (107, 103, 85), (int(t * 100), int(t * 0), int(t * 30), int(t * 35)))
    ellipse(dog_surface, (0, 0, 0), (int(t * 100), int(t * 0), int(t * 30), int(t * 35)), r * 1)
    ellipse(dog_surface, (255, 255, 255), (int(t * 35), int(t * 33), int(t * 25), int(t * 10)))
    ellipse(dog_surface, (0, 0, 0), (int(t * 35), int(t * 33), int(t * 25), int(t * 10)), int(t * 2))
    circle(dog_surface, (0, 0, 0), (int(t * 47), int(t * 38)), int(t * 4))
    ellipse(dog_surface, (255, 255, 255), (int(t * 75), int(t * 33), int(t * 25), int(t * 10)))
    ellipse(dog_surface, (0, 0, 0), (int(t * 75), int(t * 33), int(t * 25), int(t * 10)), int(t * 2))
    circle(dog_surface, (0, 0, 0), (int(t * 87), int(t * 38)), int(t * 4))

    arc(dog_surface, (0, 0, 0), (int(t * 40), int(t * 70), int(t * 60), int(t * 30)), 0, m.pi)
    polygon(dog_surface, (255, 255, 255),
            [(int(t * 43), int(t * 77)), (int(t * 46), int(t * 60)), (int(t * 50), int(t * 72))])
    polygon(dog_surface, (0, 0, 0),
            [(int(t * 43), int(t * 77)), (int(t * 46), int(t * 60)), (int(t * 50), int(t * 72))], r * 1)
    polygon(dog_surface, (255, 255, 255),
            [(int(t * 94), int(t * 77)), (int(t * 90), int(t * 60)), (int(t * 87), int(t * 72))])
    polygon(dog_surface, (0, 0, 0),
            [(int(t * 94), int(t * 77)), (int(t * 90), int(t * 60)), (int(t * 87), int(t * 72))], r * 1)


def fence(r):
    t = r

    rect(fence_surface, (195, 172, 77), (int(t * 0), int(t * 0), int(t * 800), int(t * 400)))
    line(fence_surface, (0, 0, 0), (int(t * 0), int(t * 0)), (int(t * 0), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 53), int(t * 0)), (int(t * 53), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 106), int(t * 0)), (int(t * 106), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 159), int(t * 0)), (int(t * 159), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 212), int(t * 0)), (int(t * 212), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 265), int(t * 0)), (int(t * 265), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 318), int(t * 0)), (int(t * 318), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 371), int(t * 0)), (int(t * 371), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 424), int(t * 0)), (int(t * 424), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 477), int(t * 0)), (int(t * 477), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 530), int(t * 0)), (int(t * 530), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 583), int(t * 0)), (int(t * 583), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 636), int(t * 0)), (int(t * 636), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 689), int(t * 0)), (int(t * 689), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 742), int(t * 0)), (int(t * 742), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 800), int(t * 0)), (int(t * 800), int(t * 400)), 1)
    line(fence_surface, (0, 0, 0), (int(t * 0), int(t * 400)), (int(t * 800), int(t * 400)), 1)


def doghouse():
    polygon(screen, (195, 172, 77), [(477, 650), (477, 775), (620, 850), (670, 750), (670, 640), (620, 675)])
    line(screen, (0, 0, 0), (477, 650), (477, 775), 1)
    line(screen, (0, 0, 0), (620, 850), (670, 750), 1)
    line(screen, (0, 0, 0), (670, 640), (620, 675), 1)
    line(screen, (0, 0, 0), (477, 650), (620, 675), 1)
    line(screen, (0, 0, 0), (620, 675), (670, 640), 1)
    line(screen, (0, 0, 0), (670, 640), (670, 750), 1)
    line(screen, (0, 0, 0), (670, 750), (620, 850), 1)
    line(screen, (0, 0, 0), (620, 850), (477, 775), 1)
    line(screen, (0, 0, 0), (620, 675), (620, 850), 1)

    ellipse(screen, (0, 0, 0), (510, 700, 60, 70))

    polygon(screen, (205, 172, 57), [(477, 650), (620, 675), (670, 640), (577, 550), (540, 570)])
    line(screen, (0, 0, 0), (477, 650), (620, 675), 1)
    line(screen, (0, 0, 0), (670, 640), (620, 675), 1)
    line(screen, (0, 0, 0), (670, 640), (620, 675), 1)
    line(screen, (0, 0, 0), (670, 640), (577, 550), 1)
    line(screen, (0, 0, 0), (540, 570), (577, 550), 1)
    line(screen, (0, 0, 0), (540, 570), (477, 650), 1)
    line(screen, (0, 0, 0), (620, 675), (540, 570), 1)

    ellipse(screen, (0, 0, 0), (500, 760, 30, 15), 1)
    ellipse(screen, (107, 103, 85), (490, 760, 20, 30))
    ellipse(screen, (0, 0, 0), (480, 780, 30, 15), 1)
    ellipse(screen, (0, 0, 0), (470, 780, 20, 30), 1)
    ellipse(screen, (0, 0, 0), (455, 800, 30, 15), 1)
    ellipse(screen, (0, 0, 0), (430, 805, 40, 15), 1)
    ellipse(screen, (0, 0, 0), (415, 810, 30, 15), 1)
    ellipse(screen, (0, 0, 0), (390, 815, 40, 10), 1)
    ellipse(screen, (0, 0, 0), (380, 815, 20, 20), 1)
    ellipse(screen, (0, 0, 0), (365, 825, 30, 15), 1)
    ellipse(screen, (0, 0, 0), (355, 825, 20, 20), 1)
    ellipse(screen, (107, 103, 85), (490, 760, 20, 30))
    ellipse(screen, (0, 0, 0), (490, 760, 20, 30), 1)


fence(1)
screen.blit(fence_surface, (200, 50))
empty = Color(0, 0, 0, 0)
fence_surface.fill(empty)

"""Чтобы не добавлять новый объект к поверхности, на которой уже существуют объекты (самодельный метод clear)"""

fence(0.8)
screen.blit(fence_surface, (-200, 200))
fence_surface.fill(empty)

fence(0.6)
screen.blit(fence_surface, (400, 400))
fence_surface.fill(empty)

fence(0.6)
screen.blit(fence_surface, (-120, 430))
fence_surface.fill(empty)

"""Новая поверхность которая является отражением поверхности dog_surface"""

dog(0.95)
reversed_dog = pygame.transform.flip(dog_surface, True, False)
dog_surface.fill(empty)
screen.blit(reversed_dog, (40, 790))
reversed_dog.fill(empty)

dog(1)
screen.blit(dog_surface, (40, 600))
dog_surface.fill(empty)

dog(0.8)
reversed_dog = pygame.transform.flip(dog_surface, True, False)
screen.blit(reversed_dog, (540, 580))
reversed_dog.fill(empty)
dog_surface.fill(empty)

doghouse()

"""Переделываю размер поверхности, чтобы в нее влезла голова собаки"""

size = width, height = (600, 600)
dog_surface = pygame.Surface(size)
dog(2.7)
screen.blit(dog_surface, (470, 740))
dog_surface.fill(empty)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

