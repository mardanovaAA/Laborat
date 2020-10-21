import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((428, 629))

#Colours that we will use
white = (255, 255, 255)
black = (0, 0, 0)
gray = (42, 42, 42)
marroon = (43, 17, 0)
brown = (40, 34, 11)
light_gray = (82, 70, 63)
moon_glow = (235, 245, 255)
yellow = (212, 170, 0)
fon = (102, 102, 102)
roof = (30, 30, 30)


screen.fill(fon) #fill in the background

circle(screen, moon_glow, [385, 55], 37) #Draw the moon 
rect(screen, black, [0, 263, 428, 365]) #Drow the ground


def house(x, y):
    '''
    This function draws a house.
    x, y: int,int - the coordinates of the lower left corner;
    '''
    # the walls
    rect(screen, brown, [x, y - 162, 114, 163])
    # the windows (lower)
    rect(screen, marroon, [x + 13, y - 42, 22, 27])
    rect(screen, marroon, [x + 47, y - 42, 22, 27])
    rect(screen, yellow, [x + 81, y - 42, 22, 27])
    # the high windows (upper)
    rect(screen, light_gray, [x + 21, y - 160, 13, 61])
    rect(screen, light_gray, [x + 48, y - 160, 13, 61])
    rect(screen, light_gray, [x + 75, y - 160, 13, 61])
    # the fence
    rect(screen, gray, [x-10, y - 99, 136, 17])
    rect(screen, gray, [x - 5, y - 121, 124, 6])
    rect(screen, gray, [x + 11, y - 115, 7, 16])
    rect(screen, gray, [x + 38, y - 115, 7, 16])
    rect(screen, gray, [x + 65, y - 115, 7, 16])
    rect(screen, gray, [x + 92, y - 115, 7, 16])
    # the roof
    polygon(screen, roof, [[x - 10, y - 163], [x + 6, y - 175], [x + 105, y - 175], [x + 124, y - 163]])
    # pipes
    rect(screen, gray, [x + 23, y - 203, 8, 15])
    rect(screen, gray, [x + 67, y - 190, 4, 15])
    rect(screen, gray, [x + 96, y - 190, 4, 15])
    rect(screen, gray, [x + 16, y - 190, 4, 15])


def cloud(r, g, b, p, x, y, length_x, high_y):
    '''
    This function draws clouds;
    r, g, b: 0..255, 0..255, 0..255 - the colour of cloud in RGB;
    x, y: int,int - the coordinates of the upper left corner;
    length_x: int - the length on x coordinate of cloud.
    high_y: int - the high on y coordinate of cloud.
    p: int - transparency;
    '''
    ellipse(surface, (r, g, b, p), (x, y, length_x, high_y))




def ghost(x, y, r, colour_R, colour_G, colour_B, p,Pos):
    '''
    this function draws ghost.
    x, y: int, int - the coordinates of the face centre of the ghost; 
    r: int - the radius of face of the ghost.
    colour_R, colour_G, colour_B: 0..255,0..255,0..255 - the colour of ghost in RGB;
    p: int - transparency;
    Pos: bool - True if ghost turns left, False if ghost turns right;
    '''
    circle(surface, (colour_R, colour_G, colour_B, p), (x, y), r)
    rect(surface, (colour_R, colour_G, colour_B, p), (x - r, y, 2*r, 1.3*r))
    polygon(surface, (colour_R, colour_G, colour_B, p), [(x - r, y + 1.3*r), (x - r, y + 1.6*r), 
                                                         (x - r + 0.33*r, y + 1.4*r), (x - r + 2*0.33*r, y + 1.6*r), 
                                                         (x - r + 3*0.33*r, y + 1.4*r), (x - r + 4*0.33*r, y + 1.6*r), 
                                                         (x - r + 5*0.33*r, y + 1.4*r), (x + r, y + 1.6*r), 
                                                         (x + r, y + 1.3*r)])
    if Pos:
        circle(surface, (225, 225, 225, 225), [x - int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
        circle(surface, (0, 0, 0, 225), [x - int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))
        circle(surface, (225, 225, 225, 225), [x + int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
        circle(surface, (0, 0, 0, 225), [x + int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))
    else:
        circle(surface, (225, 225, 225, 225), [x - int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
        circle(surface, (0, 0, 0, 225), [x - int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))
        circle(surface, (225, 225, 225, 225), [x + int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
        circle(surface, (0, 0, 0, 225), [x + int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))



surface = pygame.Surface([428, 629], pygame.SRCALPHA, 32)
surface = surface.convert_alpha()

cloud(77, 77, 77, 255, 19, 59, 227, 53)
cloud(51, 51, 51, 255, 187, 41, 213, 53)
cloud(77, 77, 77, 255, 254, 93, 193, 47)
cloud(0, 0, 0, 50, 187, 127, 240, 40)
cloud(52, 52, 52, 100, 76, 240, 293, 40)
cloud(52, 52, 52, 100, 188, 292, 293, 40)
cloud(52, 52, 52, 100, 0, 333, 200, 53)

house(147, 396)
house(10, 459)
house(311, 313)

ghost(339, 466, 33, 255, 0, 0,  255, True)
ghost(89, 497, 20, 255, 100, 180,  120, False)
ghost(71, 527, 20, 0, 0, 255,  100, False)
ghost(346, 362, 27, 255, 100, 10, 150, True)

screen.blit(surface, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

def ghostl(x, y, r, i, j, k, p):
    pygame.draw.circle(surface, (i, j, k, p), (x, y), r)
    pygame.draw.rect(surface, (i, j, k, p), (x-r, y, 2*r, 1.3*r))
    pygame.draw.polygon(surface, (i, j, k, p), [(x-r, y+1.3*r), (x-r, y+1.6*r), (x-r+0.33*r, y+1.4*r),
                                                      (x-r+2*0.33*r, y+1.6*r), (x-r+3*0.33*r, y+1.4*r),
                                                      (x-r+4*0.33*r, y+1.6*r), (x-r+5*0.33*r, y+1.4*r),
                                                      (x+r, y+1.6*r), (x+r, y+1.3*r)])
    pygame.draw.circle(screen, (225, 225, 225), [x-int(0.5*r), y-int(0.5*r)], int(0.3*r))
    pygame.draw.circle(screen, (0, 0, 0), [x - int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))
    pygame.draw.circle(screen, (225, 225, 225), [x + int(0.25*r), y - int(0.25 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x + int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))


def ghostr(x, y, r, i, j, k, p):
    pygame.draw.circle(surface, (i, j, k, p), (x, y), r)
    pygame.draw.rect(surface, (i, j, k, p), (x - r, y, 2 * r, 1.3 * r))
    pygame.draw.polygon(surface, (i, j, k, p),
                            [(x - r, y + 1.3 * r), (x - r, y + 1.6 * r), (x - r + 0.33 * r, y + 1.4 * r),
                             (x - r + 2 * 0.33 * r, y + 1.6 * r), (x - r + 3 * 0.33 * r, y + 1.4 * r),
                             (x - r + 4 * 0.33 * r, y + 1.6 * r), (x - r + 5 * 0.33 * r, y + 1.4 * r),
                             (x + r, y + 1.6 * r), (x + r, y + 1.3 * r)])
    pygame.draw.circle(screen, (225, 225, 225), [x - int(0.25 * r), y - int(0.25 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x - int(0.25 * r), y - int(0.25 * r)], int(0.1 * r))
    pygame.draw.circle(screen, (225, 225, 225), [x + int(0.5 * r), y - int(0.5 * r)], int(0.3 * r))
    pygame.draw.circle(screen, (0, 0, 0), [x + int(0.5 * r), y - int(0.5 * r)], int(0.1 * r))

# рисуем наконец
house(220, 594, 0, 0)
house(15, 688, 0, 0)
house(467, 469, 0, 0)
ghostl(508, 699, 50, 255, 0, 0, 250)
ghostr(134, 746, 30, 255, 100, 180, 120)
ghostr(107, 791, 30, 0, 0, 255, 100)
ghostl(519, 543, 40, 255, 100, 10, 150)
screen.blit(surface, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()