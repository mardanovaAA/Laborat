import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

FPS = 30
screen = pygame.display.set_mode((900, 700))
screen.fill((226,199,199))

#Colours that we will use
RED = (255, 57, 57)
BLUE = (0, 128, 255)
YELLOW = (255, 255, 120)
GREEN = (128, 255, 0)
MAGENTA = (255, 136, 255)
CYAN = (139, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''
    This function create new ball with the random parameters: 
        x,y - the coordinates of the centre; 
        r - radius; 
        Vx,Vy - the velocities on x coordinate and y coordinate;
        colour - the colour of the ball;
    and put these values into list parameters. 
    '''
    global parameters
    x = randint(100, 800)
    y = randint(100, 600)
    r = randint(10, 100)
    Vx = randint(-5,5)
    Vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    parameters.append([x,y,r,Vx,Vy,color])

def move_balls():
    '''
    This function move every ball from the list parameters by the value Vx and Vy along the x and y coordinate.
    If the ball is near the wall, function will change the velocity to the opposit, so the ball bounces off the wall;
    Also this function outputs the result.
    '''
    global parameters,result
    screen.fill((226,199,199))
    for number_ball in range(len(parameters)):
        ball = parameters[number_ball]
        circle(screen, ball[5],(ball[0],ball[1]),ball[2])
        if ball[0]<=ball[2] or ball[0]>=900-ball[2]:
            parameters[number_ball][3]= -parameters[number_ball][3]
        if ball[1]<=ball[2] or ball[1]>=700-ball[2]:
            parameters[number_ball][4]= -parameters[number_ball][4]    
        parameters[number_ball][0]+=parameters[number_ball][3]
        parameters[number_ball][1]+=parameters[number_ball][4]
    f1 = pygame.font.Font(None, 60)
    text = f1.render('Your score: '+str(result), 1, (255, 0, 0))
    screen.blit(text, (100, 100))    
    pygame.display.update() 

        
def check(position, number_ball):
    '''
    This function checks if the player hits the ball and if yes increases the score.
    position : (int,int) - the coordinates of the player's click
    number_ball : int - the number of ball in list parametres we want to check.
    Returns:
        mark: bool - True if the player hits the ball, False if doesnt
    '''
    global parameters, result
    mark = True    
    if (position[0]-parameters[number_ball][0])**2 + (position[1]-parameters[number_ball][1])**2 <= parameters[number_ball][2]**2:
         result = result + 1
    else:    
        mark = not mark
    return(mark)

          
    
pygame.display.update()
clock = pygame.time.Clock()
finished = True

result = 0
parameters=[]
print('How many balls do you want?')
N = int(input()) # the number of balls
for i in range(N):
    new_ball()
move_balls()
pygame.display.update()    
while finished:
    clock.tick(FPS)
    move_balls()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = False 
            for number_ball in range(len(parameters)):
                if check(event.pos,number_ball):
                    del(parameters[number_ball])
                    new_ball()
                    flag = True #the flag is True if the player hits at least one ball
            if flag:
                print('Click! Hooray, you are good!')
                print('Your score: ', result) 
            else:
                print('Click! You have missed!')
                print('Your score: ', result)         
            
            

pygame.quit()