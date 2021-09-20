import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

color = (211,211,211)
rect(screen, color, (0, 0, 400, 400),0)

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 2)

circle(screen, (255, 0, 0), (150, 140), 20)
circle(screen, (0, 0, 0), (150, 140), 20, 2)
circle(screen, (0, 0, 0), (150, 140), 8, 0)

circle(screen, (255, 0, 0), (250, 140), 15)
circle(screen, (0, 0, 0), (250, 140), 15, 2)
circle(screen, (0, 0, 0), (250, 140), 8, 0)

rect(screen, (0, 0, 0), (150, 220, 100, 20))

line(screen, (0, 0, 0), (110, 105), (190, 130), 10)
line(screen, (0, 0, 0), (210, 135), (290, 105), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
