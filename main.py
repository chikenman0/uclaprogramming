from __future__ import print_function
import pygame
import math
from random import *

pygame.init()
(width, height) = (1400, 800)
backgroundcolor = (255,255,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shooter')

myfont = pygame.font.SysFont("monospace", 15)
ar = pygame.image.load("sourcefiles/M4A1.png")
char = pygame.image.load("sourcefiles/char.png")
movingchar = pygame.image.load("sourcefiles/movingchar.png")

arposx = 500
arposy = 400

charposx1 = arposx - 10
charposx2 = arposx - 110
charspeed = 10
charmoving = False
charwidth = 120

spread = random() * 20
muzzlevelocity = 200
arpos = tuple([arposx, arposy])

gamerunning = True
while (gamerunning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
            pygame.quit()
            
    if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]:
        charwidth = 250
        charposx1 = arposx 
        charposx2 = arposx - 220
        charmoving = True
    else:
        charwidth = 120
        charposx1 = arposx - 10
        charposx2 = arposx - 110
        charmoving = False

    if pygame.key.get_pressed()[pygame.K_a]:
        arposx -= charspeed

    if pygame.key.get_pressed()[pygame.K_d]:
        arposx += charspeed
    
    mousepos = pygame.mouse.get_pos()
    currenttime = pygame.time.get_ticks()
    shootingdelay = 500
    adjacent = mousepos[0] - arposx
    opposite = mousepos[1] - arposy
    gunangle = 0

    if (adjacent == 0):
        gunangle = -math.atan(opposite/-0.000001) * 180/math.pi
    else:
        gunangle = -math.atan(opposite/adjacent) * 180/math.pi
    
    arcopy = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(ar, (170, 60)), -gunangle), 1, 0)
    triglabels = myfont.render(str(currenttime + shootingdelay) + ", " + str(currenttime) + ", " + str(gunangle), 1, (0, 255, 255))
    muzzlepos = tuple([arposx - 85, arposy - 10])
    targetpos = tuple([mousepos[0], mousepos[1] + spread])

    screen.fill(backgroundcolor)
    screen.blit(triglabels, (100, 200))

    if (pygame.event.get().type == pygame.MOUSEBUTTONDOWN):
        next_shootable = currenttime + shootingdelay
        if (currenttime <= next_shootable):
            pygame.draw.line(screen, "black", muzzlepos, targetpos, 2)
            shootingdelay -= 100

    if (adjacent <= 0):
        if (charmoving == False):
            screen.blit(pygame.transform.flip(pygame.transform.scale(char, (charwidth, 200)), 1, 0), (charposx1, (arposy - 140)))
        else:
            screen.blit(pygame.transform.flip(pygame.transform.scale(movingchar, (charwidth, 200)), 1, 0), (charposx1, (arposy - 140)))

        screen.blit(arcopy, (arposx - int(arcopy.get_width() / 2), arposy - int(arcopy.get_height() / 2)))
        
    else:
        if (charmoving == False):
            screen.blit(pygame.transform.scale(char, (charwidth, 200)), (charposx2, (arposy - 140)))
        else:
            screen.blit(pygame.transform.scale(movingchar, (charwidth, 200)), (charposx2, (arposy - 140)))

        screen.blit(pygame.transform.rotate(pygame.transform.scale(ar, (170, 60)), gunangle), (arposx - int(arcopy.get_width() / 2), arposy - int(arcopy.get_height() / 2)))

    pygame.display.update()
    
