from __future__ import print_function
import pygame

pygame.init()
(width, height) = (1000, 800)
backgroundcolor = (255,255,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shooter')


myfont = pygame.font.SysFont("monospace", 15)

assaultrifle = pygame.transform.scale(pygame.image.load("sourcefiles/M4A1.png"), (50, 30))



gamerunning = True
while (gamerunning):
    mousepos = pygame.mouse.get_pos()
    label = myfont.render(str(mousepos[0]) + ", " + str(mousepos[1]), 1, (0, 255, 255))

    screen.fill(backgroundcolor)
    screen.blit(label, (100, 100))
    screen.blit(assaultrifle, (500, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
            pygame.quit()

    pygame.display.update()
    
pygame.display.Clock
