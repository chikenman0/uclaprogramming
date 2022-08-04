from __future__ import print_function
import pygame
import math

pygame.init()
(width, height) = (1000, 800)
backgroundcolor = (255,255,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shooter')

myfont = pygame.font.SysFont("monospace", 15)
ar = pygame.image.load("sourcefiles/M4A1.png")
arposx = 500
arposy = 400
arpos = tuple([arposx, arposy])

gamerunning = True
while (gamerunning):
    mousepos = pygame.mouse.get_pos()
    adjacent = mousepos[0] - arposx
    opposite = mousepos[1] - arposy
    gunangle = 0

    if (adjacent == 0):
        gunangle = -math.atan(opposite/0.000001) * 180/math.pi
    else:
        gunangle = -math.atan(opposite/adjacent) * 180/math.pi
    
    triglabels = myfont.render(str(adjacent) + ", " + str(arposx) + ", " + str(gunangle), 1, (0, 255, 255))

    screen.fill(backgroundcolor)
    screen.blit(triglabels, (100, 200))

    if (adjacent <= 0):
        screen.blit(pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(ar, (50, 30)), -gunangle), 1, 0), arpos)
    else:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(ar, (50, 30)), gunangle), arpos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
            pygame.quit()

    pygame.display.update()
    
