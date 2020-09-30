import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((226,199,199))


circle(screen,(254,240,143),(300,300),200)
circle(screen,(120,105,1),(300,300),200,1)
#the right eye
circle(screen,(255,255,255),(375,250),30)
circle(screen,(0,0,0),(375,250),30,1)
circle(screen,(0,0,0),(375,260),15)    
#the left eye
circle(screen,(255,255,255),(225,250),30)
circle(screen,(0,0,0),(225,250),30,1)
circle(screen,(0,0,0),(225,260),15)     
#friendly smile
polygon(screen,(152,32,53),[(355,350),(355,370),(245,370),(245,350)])
polygon(screen,(0,0,0),[(355,350),(355,370),(245,370),(245,350)],2)
#right eyebrow
polygon(screen,(128,64,64),[(315,215),(315,205),(395,195),(395,205)])
#left eyebrow
polygon(screen,(128,64,64),[(285,215),(285,205),(205,195),(205,205)])
    
    


           
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
