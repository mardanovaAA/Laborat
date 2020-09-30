import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((226,199,199))

def friendly_face(size,x,y:int):
    #main shape of face
    circle(screen,(254,240,143),(x,y),size)
    circle(screen,(120,105,1),(x,y),size,1)
    #the right eye
    circle(screen,(255,255,255),(int(x+0.275*size),int(y-0.275*size)),int(0.15*size))
    circle(screen,(0,0,0),(x+int(0.275*size),y-int(0.275*size)),int(0.15*size),1)
    circle(screen,(0,0,0),(x+int(0.275*size),y-int(0.275*size)),int(0.04*size))    
    #the left eye
    circle(screen,(255,255,255),(int(x-0.275*size),int(y-0.275*size)),int(0.15*size))
    circle(screen,(0,0,0),(x-int(0.275*size),y-int(0.275*size)),int(0.15*size),1)
    circle(screen,(0,0,0),(x-int(0.275*size),y-int(0.275*size)),int(0.04*size)) 
    #the right eyebrow
    polygon(screen,(128,64,64),[(x+int(0.7*size),y-int(0.45*size)),(x+int(0.7*size),y-int(0.35*size)),(x+int(0.1*size),y-int(0.60*size)),(x+int(0.1*size),y-int(0.7*size))])
    #the left eyebrow
    polygon(screen,(128,64,64),[(x-int(0.7*size),y-int(0.45*size)),(x-int(0.7*size),y-int(0.35*size)),(x-int(0.1*size),y-int(0.60*size)),(x-int(0.1*size),y-int(0.7*size))])
    #smile
    arc(screen,(219,0,0),[x-int(0.55*size), y-int(0.1*size),int(1.1*size),int(0.8*size)],math.pi,2*math.pi,math.ceil(0.03*size))

def angry_face(size,x,y:int):
    #main shape of face
    circle(screen,(254,240,143),(x,y),size)
    circle(screen,(120,105,1),(x,y),size,1)
    #the right eye
    circle(screen,(255,255,255),(int(x+0.275*size),int(y-0.275*size)),int(0.15*size))
    circle(screen,(0,0,0),(x+int(0.275*size),y-int(0.275*size)),int(0.15*size),1)
    circle(screen,(0,0,0),(x+int(0.275*size),y-int(0.275*size)),int(0.04*size))    
    #the left eye
    circle(screen,(255,255,255),(int(x-0.275*size),int(y-0.275*size)),int(0.15*size))
    circle(screen,(0,0,0),(x-int(0.275*size),y-int(0.275*size)),int(0.15*size),1)
    circle(screen,(0,0,0),(x-int(0.275*size),y-int(0.275*size)),int(0.04*size)) 
    #the right eyebrow
    polygon(screen,(128,64,64),[(x+int(0.7*size),y-int(0.65*size)),(x+int(0.7*size),y-int(0.55*size)),(x+int(0.1*size),y-int(0.45*size)),(x+int(0.1*size),y-int(0.55*size))])
    #the left eyebrow
    polygon(screen,(128,64,64),[(x-int(0.7*size),y-int(0.65*size)),(x-int(0.7*size),y-int(0.55*size)),(x-int(0.1*size),y-int(0.45*size)),(x-int(0.1*size),y-int(0.55*size))])
    #smile
    arc(screen,(219,0,0),[x-int(0.55*size), y+int(0.1*size),int(1.1*size),int(0.8*size)],0,math.pi,math.ceil(0.03*size))

print('The number of emojis is the square of a natural number. How many emojis do you want?')
number = int(math.sqrt(int(input())))
size = int(0.4*600/number)
mark = True
for LineY in range(1,number):
    Coordin_y = LineY*int(600/number)
    for LineX in range(1,number):
        Coordin_x = LineX*int(600/number)
        if mark:
            friendly_face(size, Coordin_x, Coordin_y)
        else:
            angry_face(size, Coordin_x, Coordin_y)
        mark = not(mark)

           
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()