import pygame

pygame.init()

screencaption=pygame.display.set_caption('demo')
screen=pygame.display.set_mode([600, 800])
screen.fill([255, 255, 255])
pygame.draw.rect(screen, [111, 111, 111], [2, 2, 2, 2], 0)
pygame.draw.rect(screen, [111, 111, 111], [2, 5, 2, 2], 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
