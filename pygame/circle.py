#coding:utf-8
'''
Created on 2012-6-12

@author: kejiangtao
'''
import pygame, sys
import time
import random
from pygame.color import THECOLORS

pygame.init()
screencaption=pygame.display.set_caption('hello world')#定义窗口的标题为'hello world'
screen=pygame.display.set_mode([640, 480])#定义窗口大小为640*480
screen.fill([0, 0, 0])#用白色填充窗口
pygame.draw.rect(screen, THECOLORS['grey'], [0, 0, 60, 60])
#pygame.draw.circle(screen,THECOLORS["red"],[100,100],30,0)
rect=[(10, 10), (10, 250), (330, 250), (330, 10), (100, 100)]
pygame.draw.polygon(screen, THECOLORS['blue'], rect)

for i in range(10):
    zhijing=random.randint(0, 100)
    width=random.randint(0, 255)
    height=random.randint(0, 100)
    top=random.randint(0, 400)
    left=random.randint(0, 500)

    pygame.draw.circle(screen, [0, 255, 0], [top, left], zhijing, 2)
    pygame.draw.rect(screen, [255, 0, 0], [left, top, width, height], 3)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
