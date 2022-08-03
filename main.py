from __future__ import print_function
import pygame
import math

pygame.init()
(width, height) = (1000, 800)
backgroundcolor = (255,255,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shooter')

myfont = pygame.font.SysFont("monospace", 15)
assaultrifle = pygame.transform.scale(pygame.image.load("sourcefiles/M4A1.png"), (50, 30))
assaultrifleposx = 500
assaultrifleposy = 400
assaultriflepos = tuple([assaultrifleposx, assaultrifleposy])

gamerunning = True
while (gamerunning):
    mousepos = pygame.mouse.get_pos()
    adjacent = abs(mousepos[0] - assaultrifleposx)
    opposite = abs(mousepos[1] - assaultrifleposy)
    
    triglabels = myfont.render(str(mousepos[0]) + ", " + str(assaultrifleposx) + ", " + str(math.atan(opposite/adjacent) * 180/math.pi), 1, (0, 255, 255))

    screen.fill(backgroundcolor)
    screen.blit(triglabels, (100, 200))
    screen.blit(assaultrifle, assaultriflepos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
            pygame.quit()

    pygame.display.update()
    
