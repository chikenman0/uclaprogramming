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
    
clock = pygame.time.Clock()

counter, text = 10, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: 
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)
