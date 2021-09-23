import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

#background - sky and grass
rect(screen, (152, 251, 152), (0, 300, 800, 300),0)
rect(screen, (176, 224, 230), (0, 0, 800, 300),0)


def men(x,y):
    #man: body
    ellipse(screen, (147, 112, 219), (x-10,y+40,100,200))
    #man: head
    ellipse(screen, (255, 228, 196), (x,y,80,70))
    #man: arms
    line(screen, (0,0,0), (x+5,y+75),(x-60,y+180))
    line(screen, (0,0,0), (x+75,y+75),(x+130,y+180))
    #man:legs
    line(screen, (0,0,0), (x+75,y+210),(x+90,y+360))
    line(screen, (0,0,0), (x+5,y+210),(x-50,y+360))
    line(screen, (0,0,0), (x-80,y+365),(x-50,y+360))
    line(screen, (0,0,0), (x+90,y+360),(x+125,y+360))


def woman(x,y):
    #woman:body
    polygon(screen, (255, 105, 180), [(x+40,y+30),(x-20,y+240),(x+100,y+240)])
    #woman:head
    ellipse(screen, (255, 228, 196), (x,y,80,70))
    #woman:arms
    line(screen, (0,0,0), (x+30,y+80),(x-30,y+180))
    line(screen, (0,0,0), (x+50,y+80),(x+110,y+140))
    line(screen, (0,0,0), (x+130,y+60),(x+110,y+140))
    #man:legs
    line(screen, (0,0,0), (x+10,y+240),(x-5,y+360))
    line(screen, (0,0,0), (x+65,y+240),(x+100,y+360))
    line(screen, (0,0,0), (x-30,y+365),(x-5,y+360))
    line(screen, (0,0,0), (x+100,y+360),(x+125,y+365))

def heart(x,y):
    #heart
    polygon(screen, (255,0,0), [(x,y), (x+33,y-32),(x-20,y-40)])
    circle(screen, (255,0,0), (x-5,y-40),15)
    circle(screen, (255,0,0), (x+20,y-37),15)
    #line
    line(screen, (0,0,0), (x,y),(x-20,y+70))

def icecream(x,y,s):
    #cone
    polygon(screen, (218, 165, 32), [(x,y), (x+s*40,y-np.abs(s)*20),(x+s*20,y-np.abs(s)*40)])
    #red ball
    ellipse(screen,(220, 20, 60),(x+s*30,y-np.abs(s)*35,s*18,np.abs(s)*16))
    #brown ball
    ellipse(screen,(129, 49, 9),(x+s*14,y-np.abs(s)*45,s*22,np.abs(s)*20))
    #white ball
    ellipse(screen,(255, 248, 220),(x+s*29,y-np.abs(s)*52,s*23,np.abs(s)*20))
    


men(260,160)
woman(420,160)
heart(560,175)
icecream(204,345,-2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
