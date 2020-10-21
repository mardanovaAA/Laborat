import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()
pygame.font.init()

FPS = 30
screen = pygame.display.set_mode((900, 600))
screen.fill((226, 199, 199))

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
        x, y - the coordinates of the centre; 
        r - radius; 
        Vx, Vy - the velocities on x coordinate and y coordinate;
        colour - the colour of the ball;
    and put these values into list parameters. 
    '''
    global parameters
    x = randint(100, 800)
    y = randint(100, 500)
    r = randint(15, 100)
    Vx = randint(-5, 5)
    Vy = randint(-5, 5)
    color = COLORS[randint(0, 5)]
    parameters.append([x, y, r, Vx, Vy, color])

def move_balls():
    '''
    This function move every ball from the list parameters by the value Vx and Vy along the x and y coordinate.
    If the ball is near the wall, function will change the velocity to the opposit, so the ball bounces off the wall;
    Also this function outputs the result.
    '''
    screen.fill((226, 199, 199))
    global parameters, result
    for number_ball in range(len(parameters)):
        ball = parameters[number_ball]
        circle(screen, ball[5],(ball[0], ball[1]), ball[2])
        if (ball[0] <= ball[2]) or (ball[0] >= 900-ball[2]):
            parameters[number_ball][3] = -parameters[number_ball][3]
        if (ball[1] <= ball[2]) or (ball[1] >= (600 - ball[2])):
            parameters[number_ball][4] = -parameters[number_ball][4]    
        parameters[number_ball][0] += parameters[number_ball][3]
        parameters[number_ball][1] += parameters[number_ball][4]
    move_bonus()
    f1 = pygame.font.Font(None, 60)
    text = f1.render('Your score: ' + str(result), 1, (255, 0, 0))
    screen.blit(text, (100, 100))  
    pygame.display.update() 

        
def check_ball(position, number_ball):
    '''
    This function checks if the player hits the ball and if yes increases the score.
    position : (int,int) - the coordinates of the player's click
    number_ball : int - the number of ball in list parametres we want to check.
    Returns:
        mark: bool - True if the player hits the ball, False if doesnt
    '''
    global parameters, result
    mark = True    
    if ((position[0] - parameters[number_ball][0])**2 + (position[1] - parameters[number_ball][1])**2) <= parameters[number_ball][2]**2:
         result = result + 1
    else:    
        mark = not mark
    return(mark)

def star(Coordin_x, Coordin_y, size_out, colour):
    """
    This function draw a star
    Coordin_x, Coordin_y: int, int - coordinates of the centre
    size_out: int - the radius of the outer points
    colour (0..255, 0..255, 0..255) - the colour of the star
    """
    Coordinates = [] #the coordinates of the vertexes
    size_in = 0.6*size_out #the radius of the inner points 
    mark = True
    for i in range(15):
        angle = (i/14)*2*math.pi
        if mark:
            Coordinates.append((int(Coordin_x + size_out*math.cos(angle)), int(Coordin_y + size_out*math.sin(angle))))
        else:
            Coordinates.append((int(Coordin_x + size_in*math.cos(angle)), int(Coordin_y + size_in*math.sin(angle))))
        mark = not(mark)
    polygon(screen, colour, Coordinates)


def instruction():
    """
    This function displays the instructions for our game.
    """
    global Name
    screen.fill((226, 199, 199))
    f1 = pygame.font.Font(None, 60)
    f2 = pygame.font.Font(None, 40)
    text = f1.render('It is amazing game "Catch a ball"', 1, (175, 27, 142))
    screen.blit(text, (100, 100))
    text1 = f2.render('If you hit a ball, you will get 1 score point', 1, (128, 64, 0))
    screen.blit(text1, (80, 160))
    text1 = f2.render('If you hit a bonus star, you will get 1 score point', 1, (128, 64, 0))
    screen.blit(text1, (80, 190))
    text1 = f2.render('If you want to start, press esc and enjoy the game!', 1, (175, 27, 142))
    screen.blit(text1, (80, 300))
    flag = True
    pygame.display.update() 
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                flag = False
    
def score():
    """
    This function displays the score in the end of game and redirects to writing score or closes the game.
    """
    global result
    screen.fill((226, 199, 199))
    f1 = pygame.font.Font(None, 60)
    f2 = pygame.font.Font(None, 40)
    text = f1.render('Congratulations! Your score is ' + str(result) + '!', 1, (255, 0, 0))
    screen.blit(text, (100, 100))
    text = f2.render('Do you want to write your result to the score table?', 1, (0, 0, 255))
    screen.blit(text, (90, 280))
    flag = True
    rect(screen, (200, 191, 231), (200, 350, 200, 100))
    rect(screen, (71, 52, 137), (200, 350, 200, 100),2)
    rect(screen, (200, 191, 231), (500, 350, 200, 100))
    rect(screen, (71, 52, 137), (500, 350, 200, 100),2)
    text = f1.render('YES', 1, (255, 0, 0))
    screen.blit(text, (240, 380))
    text = f1.render('NO', 1, (255, 0, 0))
    screen.blit(text, (550, 380))
    pygame.display.update() 
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (200 <= event.pos[0] <= 400) and (350 <= event.pos[1] <= 450):
                    flag = False
                    write_score()
                elif (500 <= event.pos[0] <= 700) and (350 <= event.pos[1] <= 450):
                    flag = False

def write_score():
    """
    This function writes score to the file
    """
    global result
    screen.fill((226, 199, 199))
    f2 = pygame.font.Font(None, 40)
    text = f2.render('Please write your name in the console', 1, (255, 0, 0))
    screen.blit(text, (100, 100))
    pygame.display.update() 
    print("What is your name, dear player?")
    Name = input()
    f = open('6.1.Score.txt', 'a')
    f.write(Name + ' ' + str(result) + '\n')
    f.close()
    flag = True
    while flag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

def creat_bonus():
    """
    This function randomly creates bonuses
    """
    global bonus_parameters
    probability = randint(1, 1000)
    if (probability == 27) or (probability == 63):
        r = randint(10, 50)  
        Vy = randint(1,4)
        bonus_parameters.append([0, 0, r, int(1.5 * Vy), Vy])

def move_bonus():
    """
    This function moves all bonuses on the screen
    """      
    global bonus_parameters
    new_bonus_parameters = []
    for number_bonus in range(len(bonus_parameters)):
        bonus = bonus_parameters[number_bonus]
        star(bonus[0], bonus[1], bonus[2], (148, 0, 89))
        bonus[0] += bonus[3]
        bonus[1] += bonus[4]
        if (bonus[0] < 900) or (bonus[1] < 700):
            new_bonus_parameters.append((bonus_parameters[number_bonus]))
    bonus_parameters = new_bonus_parameters            
            
def check_bonus(position, number_bonus):
    '''
    This function checks if the player hits the bonus and if yes increases the score.
    position : (int,int) - the coordinates of the player's click
    number_ball : int - the number of ball in list parametres we want to check.
    Returns:
        mark: bool - True if the player hits the bonus, False if doesnt
    '''
    global bonus_parameters, result
    mark = True    
    if ((position[0] - bonus_parameters[number_bonus][0])**2 + (position[1] - bonus_parameters[number_bonus][1])**2) <= bonus_parameters[number_bonus][2]**2:
         result = result + 7
    else:    
        mark = not mark
    return(mark)
                
    
pygame.display.update()
clock = pygame.time.Clock()
finished = True

result = 0
parameters = []
bonus_parameters = []
for i in range(17):
    new_ball()
instruction()
move_balls()
pygame.display.update()    
while finished:
    clock.tick(FPS)
    creat_bonus()
    move_balls()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            finished = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            new_parameters = []
            for number_ball in range(len(parameters)):
                if not check_ball(event.pos, number_ball):
                    new_parameters.append(parameters[number_ball])
            number_ball =  len(parameters) - len(new_parameters)       
            parameters = new_parameters
            for i in range(number_ball):
                new_ball()
            new_parameters = []
            for number_bonus in range(len(bonus_parameters)):
                if not check_bonus(event.pos, number_bonus):
                    new_parameters.append(bonus_parameters[number_bonus])    
            bonus_parameters = new_parameters
score()           
            
pygame.quit()