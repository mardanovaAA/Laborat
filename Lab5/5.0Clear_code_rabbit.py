import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((226,199,199))


def draw_body(Coordin_x,Coordin_y,height,fat, colour_body,colour_belly):
    """
    this function draws the body of rabbit
    Parameters:
    Coordin_x, Coordin_y: int, int
        the coordinates of the bottom centre. 
    height : int
        The length of body from bottom to top.
    fat_body : int
        The thickness of body.
    colour_body: (0..255,0..255,0..255) of the name of colour
        the colour of body.
    colour_belly: (0..255,0..255,0..255) of the name of colour
        the colour of belly.
    """
    ellipse(screen, colour_body,(Coordin_x-fat//2, Coordin_y- height, fat, height))
    ellipse(screen, colour_belly,(Coordin_x-fat//4, Coordin_y - 2*height//3, fat//2, height//2))


def draw_head(Coordin_x, Coordin_y, size, colour_head ):
    """
    This function draws head
    Parameter:
    Coordin_x, Coordin_y: int, int
        the coordinates of the bottom centre.
    size : int
        the radius of head.
    colour_head :(0..255,0..255,0..255) of the name of colour
        the colour of head.
    """
    circle(screen, colour_head,(Coordin_x,Coordin_y),size)
    
def draw_ear(Coordin_x, Coordin_y, length,thickness,colour_ear,colour_inner):
    """
    This function draws ear
    Parameters:
    Coordin_x, Coordin_y: int, int: 
        The coordinates of the ear's bottom
    length : int
        the length of ear.
    thickness : int
        the thickness of ear.
    colour_ear :(0..255,0..255,0..255) of the name of colour
        the colour of ear.
    colour_inner :(0..255,0..255,0..255) of the name of colour
        the colour of the inner ear.    
    """    
    ellipse(screen,colour_ear,(Coordin_x-thickness//2,Coordin_y-length,thickness,length))
    ellipse(screen,colour_inner,(Coordin_x-thickness//4,Coordin_y-2*length//3,thickness//2,length//2))

def draw_leg(Coordin_x,Coordin_y,height,thickness,colour_leg):
    """
    This function draws leg
    Parameters:
    Coordin_x, Coordin_y: int, int: 
        The coordinates of the centre left side
    height : int
        the length from bottom to top.
    thickness : int
        the length from left to right.
    colour_leg : (0..255,0..255,0..255) of the name of colour
        the colour of leg.
    """    
    ellipse(screen,colour_leg,(Coordin_x,Coordin_y-height//2,thickness,height))
        
    
def rabbit(Coordin_x, Coordin_y, height, length_ears, colour_0,colour_1):
    """
    This function draws a pretty rabbit
    Parameters:
    Coordin_x, Coordin_y: int, int: 
        The coordinates of the bottom centre
    height : int: 
        the height of rabbit - from hind legs to the top of head WITHOUT ears.
    length_ears : int: 
        the length of rabbit's ears;
    colour_0 : (0..255,0..255,0..255) or the colour name: 
        the colour of our rabbit;
    colour_1 : (0..255,0..255,0..255) or the colour name: 
        the colour of rabbit's belly and ears;    
    """
    draw_body(Coordin_x,Coordin_y,int(0.7*height),int(0.5*height),colour_0,colour_1)
    draw_head(Coordin_x, int(Coordin_y-0.8*height), int(0.2*height), colour_0)
    draw_ear(Coordin_x + int(0.1*height),Coordin_y-int(0.85*height),length_ears,int(0.35*length_ears),colour_0,colour_1)
    draw_ear(Coordin_x - int(0.1*height),Coordin_y-int(0.85*height),length_ears,int(0.35*length_ears),colour_0,colour_1)
    draw_leg(Coordin_x + int(0.1*height),Coordin_y-int(0.02*height),int(0.1*height),int(0.25*height),colour_0)
    draw_leg(Coordin_x - int(0.35*height),Coordin_y-int(0.02*height),int(0.1*height),int(0.25*height),colour_0)
    

rabbit(300,500,300,110,(133,211,250),(254,241,129))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()