#coding:utf-8
import pygame
import sys
from msilib.schema import Font
from pygame import font

screen_width=600
screen_length=800
distance=100

def linemiddle():
    for x in range(distance, screen_width-distance):
        if x%10<6:
            screen.set_at([screen_length/2, x], [100, 100, 100])
    pygame.display.flip()

def lineleft():
    #0.3:倾斜度 50:距离中线的距离
    pygame.draw.line(screen, [55, 55, 55], [screen_length/2-distance, distance], [screen_length/2-distance-(screen_width-100)*0.2, screen_width-distance])
    pygame.display.flip()

def lineright():
    pointlist=[]
    for y in range(distance, screen_width-distance):
        point=[screen_length/2+distance+(y-distance)*0.2, y]#600
        pointlist.append(point)
    pygame.draw.lines(screen, [55, 55, 55], True, pointlist)
    pygame.display.flip()

def loadcar(x):
    car=pygame.image.load('../images/car.jpg')
    screen.blit(car, [300, x])
    pygame.display.flip()

def loadtext(x, y):
    font=pygame.font.SysFont('雅黑', 19)
    text=font.render('location:'+str(x)+','+str(y), True, (255, 0, 0))
    screen.blit(text, [50, 50])

if __name__=='__main__':
    pygame.init()
    screencaption=pygame.display.set_caption('road')
    screen=pygame.display.set_mode([screen_length, screen_width])


#    linemiddle()
#    lineleft()
#    lineright()
#    loadcar(320)
    while True:
        screen.fill([255, 255, 255])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        for y in range(screen_width-distance-300, distance,-1):
            screen.fill([255, 255, 255])
            pygame.time.delay(200)
            loadcar(y)
            loadtext(300, y)
            linemiddle()
            lineleft()
            lineright()


