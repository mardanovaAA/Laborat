import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 600))
screen.fill((62,247,251))
rect(screen,(77,235,16),(0,300,900,300))

def tree(bottom_x,bottom_y,height:int):
    #bottom_x, bottom_y - coordinates of the centre of tree's bottom
    #height - height of the tree
    #tree trunk
    rect(screen,(128,80,53),(bottom_x-int(0.1*height),bottom_y-height//2,int(0.2*height),height//2))
    rect(screen,(66,33,0),(bottom_x-int(0.1*height),bottom_y-height//2,int(0.2*height),height//2))
    #tree leaves:
    #1
    circle(screen, (35,120,35), (bottom_x, bottom_y-int(0.525*height)),height//5)     
    circle(screen, (0,89,0), (bottom_x, bottom_y-int(0.525*height)),height//5,1)  
    #2
    circle(screen, (26,149,41), (bottom_x, bottom_y-int(5*height/6)), height//6)     
    circle(screen, (0,89,0), (bottom_x, bottom_y-int(5*height/6)), height//6,1) 
    #3
    circle(screen, (26,149,41), (bottom_x, bottom_y-int(0.6*height)), height//6)     
    circle(screen, (0,89,0), (bottom_x, bottom_y-int(0.6*height)), height//6,1) 
    #4
    circle(screen, (26,149,41), (bottom_x-int(0.2*height), bottom_y-int(0.75*height)), height//6)     
    circle(screen, (0,89,0), (bottom_x-int(0.2*height), bottom_y-int(0.75*height)), height//6,1)
    #5
    circle(screen, (26,149,41), (bottom_x+int(0.2*height), bottom_y-int(0.75*height)), height//6)     
    circle(screen, (0,89,0), (bottom_x+int(0.2*height), bottom_y-int(0.75*height)), height//6,1)
    #6
    circle(screen, (35,120,35), (bottom_x+int(0.15*height), bottom_y-int(0.5*height)), height//6)     
    circle(screen, (0,89,0), (bottom_x+int(0.15*height), bottom_y-int(0.5*height)), height//6,1)
    #7
    circle(screen, (35,120,35), (bottom_x-int(0.15*height), bottom_y-int(0.5*height)), height//6)     
    circle(screen, (0,89,0), (bottom_x-int(0.15*height), bottom_y-int(0.5*height)), height//6,1)
 
def house(Coordin_x,Coordin_y,height,colour_wall,colour_roof,colour_window):
    #Coordin_x,Coordin_y - coordinates of the lower-left corner
    #height - height of the house
    #walls
    rect(screen,colour_wall,(Coordin_x,Coordin_y-height//2,height,height//2))
    rect(screen,(0,0,0),(Coordin_x,Coordin_y-height//2,height,height//2),1)
    #roof
    polygon(screen,colour_roof,[(Coordin_x-height//8,Coordin_y-height//2),(Coordin_x+height//4,Coordin_y-height),(Coordin_x+6*height//8,Coordin_y-height),(Coordin_x+9*height//8,Coordin_y-height//2)])
    polygon(screen,(0,0,0),[(Coordin_x-height//8,Coordin_y-height//2),(Coordin_x+height//4,Coordin_y-height),(Coordin_x+6*height//8,Coordin_y-height),(Coordin_x+9*height//8,Coordin_y-height//2)],1)
    #window1
    rect(screen,colour_window,(Coordin_x+height//8,Coordin_y-3*height//8,height//4,height//4))
    rect(screen,(0,0,0),(Coordin_x+height//8,Coordin_y-3*height//8,height//4,height//4),1)
    line(screen,(0,0,0),(Coordin_x+height//8,Coordin_y-height//4),(Coordin_x+3*height//8,Coordin_y-height//4),2)
    line(screen,(0,0,0),(Coordin_x+height//4,Coordin_y-3*height//8),(Coordin_x+height//4,Coordin_y-height//8),2)
    #window2
    rect(screen,colour_window,(Coordin_x+5*height//8,Coordin_y-3*height//8,height//4,height//4))
    rect(screen,(0,0,0),(Coordin_x+5*height//8,Coordin_y-3*height//8,height//4,height//4),1)
    line(screen,(0,0,0),(Coordin_x+5*height//8,Coordin_y-height//4),(Coordin_x+7*height//8,Coordin_y-height//4),2)
    line(screen,(0,0,0),(Coordin_x+6*height//8,Coordin_y-3*height//8),(Coordin_x+6*height//8,Coordin_y-height//8),2)

def cloud(Coordin_x,Coordin_y,length):
    #Coordin_x,Coordin_y - coordinates of the lower-left corner
    #lehgth - length of the cloud
    for i in range(1,5):
        circle(screen,(193,252,253),(Coordin_x+i*length//4,Coordin_y-length//4),length//4)
        circle(screen,(6,181,185),(Coordin_x+i*length//4,Coordin_y-length//4),length//4,1)
    for i in range(1,3):
        circle(screen,(193,252,253),(Coordin_x+i*3*length//8,Coordin_y-5*length//8),length//4)
        circle(screen,(6,181,185),(Coordin_x+i*3*length//8,Coordin_y-5*length//8),length//4,1)

def sun(Coordin_x,Coordin_y,size_out,colour):
    #Coordin_x, Coordin_y - coordinates of the centre
    #size_out - the radius of the outer points   
    Coordinates = [] #the coordinates of the vertexes
    size_in = 0.6*size_out #the radius of the inner points 
    mark = True
    for i in range(15):
        angle = (i/14)*2*math.pi
        if mark:
            Coordinates.append((int(Coordin_x+size_out*math.cos(angle)),int(Coordin_y+size_out*math.sin(angle))))
        else:
            Coordinates.append((int(Coordin_x+size_in*math.cos(angle)),int(Coordin_y+size_in*math.sin(angle))))
        mark = not(mark)
    polygon(screen,colour,Coordinates)
    polygon(screen,(0,0,0),Coordinates,1)
    
#pink stars
sun(120,227,15,(240,184,53))
sun(698,75,13,(240,184,53))
sun(877,272,13,(240,184,53))
sun(408, 279,10,(240,184,53))
#violet stars
sun(626,191,17,(183,114,190))
sun(336,37,13,(183,114,190))
sun(794,19,10,(183,114,190))
#green stars
sun(433,147,13,(147,216,141))
sun(15,250,8,(147,216,141))
sun(833,128,10,(147,216,141))
sun(524,40,15,(147,216,141))
#big yellow sun
sun(77,62,35,(255,242,0))
#clouds
cloud(130,190,180)
cloud(365,91,100)
cloud(756,120,110)
house(40,540,250,(185,122,87),(192,35,7),(255,187,221))
tree(350,540,270)
tree(520,350,235)
house(585,360,180,(201,29,188),(38,30,189),(245,233,80))
tree(820,360,200)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()