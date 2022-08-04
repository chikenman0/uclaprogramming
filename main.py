from __future__ import print_function
import pygame
import math

pygame.init()
(width, height) = (1200, 800)
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
charposy1 = arposy - 140
charposx2 = arposx - 110
charposy2 = arposy - 140
charspeed = 10
jumpdelay = 0.3 # seconds
arpos = tuple([arposx, arposy])
charwidth = 120

gamerunning = True
while (gamerunning):
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gunfiring = True
            
        if pressed[pygame.K_a] or pressed[pygame.K_d]:
            char = movingchar
            charwidth = 250
            charposx1 = arposx 
            charposx2 = arposx - 220
        else:
            charwidth = 120
            char = pygame.image.load("sourcefiles/char.png")
            charposx1 = arposx - 10
            charposx2 = arposx - 110

        if pressed[pygame.K_a]:
            arposx -= charspeed
        
        if pressed[pygame.K_d]:
            arposx += charspeed
            
        if event.type == pygame.QUIT:
            gamerunning = False
            pygame.quit()
    
    mousepos = pygame.mouse.get_pos()
    adjacent = mousepos[0] - arposx
    opposite = mousepos[1] - arposy
    gunangle = 0

    if (adjacent == 0):
        gunangle = -math.atan(opposite/-0.000001) * 180/math.pi
    else:
        gunangle = -math.atan(opposite/adjacent) * 180/math.pi
    
    arcopy = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(ar, (170, 60)), -gunangle), 1, 0)
    triglabels = myfont.render(str() + ", " + str(arposx) + ", " + str(gunangle), 1, (0, 255, 255))

    screen.fill(backgroundcolor)
    screen.blit(triglabels, (100, 200))

    if (adjacent <= 0):
        screen.blit(pygame.transform.flip(pygame.transform.scale(char, (charwidth, 200)), 1, 0), (charposx1, charposy1))
        screen.blit(arcopy, (arposx - int(arcopy.get_width() / 2), arposy - int(arcopy.get_height() / 2)))
        
    else:
        screen.blit(pygame.transform.scale(char, (charwidth, 200)), (charposx2, charposy2))
        screen.blit(pygame.transform.rotate(pygame.transform.scale(ar, (170, 60)), gunangle), (arposx - int(arcopy.get_width() / 2), arposy - int(arcopy.get_height() / 2)))

    

    pygame.display.update()
    
