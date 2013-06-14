import pygame, os, sys
from pygame.locals import *
import random, math
zoomt=1.0
zoomy=1.0
pulse=20
amp=100
def get_input(events):       #事件捕捉函数
    global zoomt
    global zoomy
    global pulse
    for event in events:
        if event.type==QUIT:
                    sys.exit(0)
        elif event.type==KEYDOWN:
            if event.key==275:
                if zoomt<20:
                    zoomt+=0.1
                else:
                    zoomt=20
            elif event.key==276:
                if zoomt>0.1:
                    zoomt-=0.1
                else:
                    zoomt=0.1
            if event.key==274:
                if zoomy>=0.0024:
                    zoomy/=1.2
                else:
                    zoomy=0.0024
            elif event.key==273:
                if zoomy<=0.8:
                    zoomy*=1.2
                else:
                    zoomy=1.0
            if event.key==44:
                if pulse<200:
                    pulse+=1
                else:
                    pulse=100
            elif event.key==46:
                if pulse>1:
                    pulse-=1
                else:
                    pulse=1
            print(event.key)
def showText(screen, txt, size, pos):    #在界面显示字符
    myfont=pygame.font.SysFont("Vera", size)
    screen.blit(myfont.render(txt, 1, (255, 255, 0)), pos)
def putChart(screen, data, backColor, lineColor, zoom, zoomy, width): #示波器界面生成
    size=(298, 222)
    u_size=screen.get_size()
    face=pygame.Surface(size)
    face=face.convert()
    #face.fill(backColor)
    #rect = [(10,10),(10,250),(330,250),(330,10)]
    #pygame.draw.polygon(face,(255,255,255),rect)
    lenx=len(data)
    leny=100
    first=1
    points=[(0, 0)]
    for i in range(lenx):
    #print lenx - i
        if first==1:
            points[0]=(int(float(i)*zoom*size[0]/float(lenx)), size[1]/2-(data[i]*zoomy))
            first=0
        else:
            points.append((int(float(i)*zoom*size[0]/float(lenx)), size[1]/2-(data[i]*zoomy)))

    pygame.draw.aalines(face, lineColor, 0, points, width)
    screen.blit(face, (30, 29))
pygame.init()
window=pygame.display.set_mode((600, 301))
pygame.display.set_caption("Oscilloscope with sine Data    ----Powered by yuanshl")
face=pygame.image.load(os.path.join("d:\\python", "oscope2.jpg"))
screen=pygame.display.get_surface()
screen.blit(face, (0, 0))
pygame.display.flip()
d=range(100)
clock=pygame.time.Clock()
for i in range(100):    #生成100个点的正弦数据
    d[i]=111.0*math.sin(2*3.141592*i/25)
count=0
while 1:
    count+=1
    if count%pulse==0:
        for i in range(100):
            d[i]=111.0*math.sin(2*3.141592*(i)/25+float(count)/20.0)
    putChart(screen, d, (255, 0, 0), (0, 0, 255), zoomt, zoomy, 1)
    get_input(pygame.event.get())
    fps=clock.get_fps()
    #print "fps = ",fps
    clock.tick()
    s="%0.2f %0.2f %0.2f %d"%(fps, zoomt, zoomy, pulse)
    showText(screen, s, 20, (30, 29))
    pygame.display.update()
    #pygame.time.delay(80)
