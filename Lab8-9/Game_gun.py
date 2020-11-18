import pygame
from pygame.draw import *
from random import randint
import math
from numpy import sign

pygame.init()
pygame.font.init()

size = (800, 600)
screen = pygame.display.set_mode((size[0], size[1] + 45))

fon_color = (235, 213, 247)
screen.fill(fon_color)

FPS = 30
clock = pygame.time.Clock()

#colors which we will use for targets
IndianRed = (205, 92, 92)
DarkSalmon = (233, 150, 122)
Crimson = (220, 20, 60)
MediumVioletRed = (199, 21, 133)
DeepPink = (255, 20, 147)
Tomato = (255, 99, 71)
DarkOrange = (255, 140, 0)
Magenta = (255, 0, 255)
MediumOrchid = (186, 85, 211)
BlueViolet = (138, 43, 226)
DarkMagenta = (139, 0, 139)
DarkCyan = (0, 139, 139)
Aqua = (0, 255, 255)
Aquamarine = (127, 255, 212)
DodgerBlue = (30, 144, 255)
MediumSlateBlue = (123, 104, 238)
Navy = (0, 0, 128)
COLORS = [IndianRed, DarkSalmon, Crimson, MediumVioletRed, DeepPink, Tomato, DarkOrange, Magenta,
          MediumOrchid, BlueViolet, DarkMagenta, DarkCyan, Aqua, Aquamarine, DodgerBlue, MediumSlateBlue, Navy]

#colors which we will use for bullets (green tones from light to dark)
Green1 = (127, 255, 0)
Green2 = (0, 255, 0)
Green3 = (34, 139, 34)
Green4 = (0, 100, 0)
 
class Ball():
    """
    This class is responsible for bullets.
    """
    def __init__(self, coordinates, velocity, color, radius = 15):
        """
        Creats a bullet
        
        Parameters
        ----------
        coordinates : [int, int] - the list of coordinates of the centre.
        velocity : [int, int] - the list of components of the bullet velocity.
        color : (0..255, 0..255, 0..255) - the colour of bullet in RGB.
        radius : int - the radius of the bullet (the default is 15)
        """
        self.coordinates = coordinates
        self.radius = radius
        self.velocity = velocity
        self.live = True
        self.color = color
        
    def draw(self):
        """
        Draws the bullet on the screen

        """
        circle(screen, self.color, self.coordinates, self.radius)
        
    def move(self, g = 3):
        """
        Changes the coordinates of the bullet based on gravity.
        Also kills the bullet if the y-component of velocity is small and the bullet fell to the ground.

        Parameters
        ----------
        g : int - acceleration of gravity (the defaut is 3)
        """
        self.velocity[1] += g
        for i in range(2):
            self.coordinates[i] += self.velocity[i]
        self.check_walls()
        if (abs(self.velocity[1]) <= g) and (self.coordinates[1] >= size[1] - self.radius):
            self.live = False
    
    def check_walls(self):
        """
        Checks whether the bullet hit the window border. 
        If yes, changes the velocity component to the opposite one.
        """
        if (self.coordinates[0] <= self.radius): 
            self.velocity[0] = -self.velocity[0]
            self.coordinates[0] = self.radius
        if (self.coordinates[0] >= size[0] - self.radius):
            self.velocity[0] = -self.velocity[0]
            self.coordinates[0] = size[0] - self.radius
        if (self.coordinates[1] <= self.radius):
            self.velocity[1] = -self.velocity[1]
            self.coordinates[1] = self.radius
        if (self.coordinates[1] >= size[1] - self.radius):
            self.velocity[1] = -self.velocity[1]
            self.coordinates[1] = size[1] - self.radius
            
class Target():
    """
    This class is responsible for targets.
    """
    def __init__(self, coordinates = None, radius = None, color = None):
        """
        Creats the target

        Parameters
        ----------
        coordinates : [int, int] - the list of coordinates of the centre.
        radius : int - the radius of the target.
        color : (0..255, 0..255, 0..255) - the colour of the target in RGB.
            DESCRIPTION. If some parametres are None, it will set with random.
        """
        if radius == None:
            radius = randint(20, 50)
        if color == None:
            color = COLORS[randint(0, len(COLORS) - 1)] 
        if coordinates == None:
            self.coordinates = (randint(radius, size[0] - radius), randint(radius, size[1] - radius))    
        self.radius = radius
        self.color = color
    
    def draw(self):
        """
        Draw the target on the screen.
        """
        circle(screen, self.color, self.coordinates, self.radius)
        circle(screen, (0, 0, 0), self.coordinates, self.radius, 1)
        
    def check(self, ball):
        """
        Checks if the target is hit by the bullet.

        Parameters
        ----------
        ball : class Ball() - the bullet which is checked.

        Returns
        -------
        True - if the bullet hit the target.
        False - if not.
        """
        dist = 0
        for i in range(2):
            dist += (self.coordinates[i] - ball.coordinates[i])**2
        return (dist < (self.radius + ball.radius)**2)

class Gun():
    """
    This class is responsible for gun
    """
    def __init__(self):
        """
        Creats the gun.
        
        Parameters
        ----------
        coordinates: [int, int] - the list of coordinates of the left bottom corner.
        power_min: int - the minimal power of the gun.
        power_max: int - the maximum power of the gun.
        power: int - the current power of the gun.
        live: bool - True if the gun is active
        color: (0..255, 0..255, 0..255) - the colour of the gun in RGB.
        angle: int - angle of gun inclination.
        points: list of [int,int] - the list of coordinates of the 4 vertices.

        """
        self.coordinates = [20, size[1] // 2]
        self.power_min = 10
        self.power_max = 50
        self.power = 10
        self.live = False
        self.color = (160, 82, 45)
        self.angle = 0
        self.points = []
        
    def power_up(self):
        """
        Increases the current power of gun, if the gun is active.
        """
        if self.live and (self.power < self.power_max):
            self.power += 0.5
    
    def targetting(self, event = 0):
        """
        Sets angle of gun inclination based on mouse position. 
        Creat points - the list of coordinates of the 4 vertices.
        Parameters
        ----------
        event : [int,int] - the coordinates of the mouse position (the default is 0)
        """
        if event:
            if event[0] != self.coordinates[0]:
                self.angle = math.atan((self.coordinates[1] - event[1]) / (event[0] - self.coordinates[0]))
            else:
                self.angle = (math.pi / 2) * sign(self.coordinates[1] - event[1])
        else:
            self.angle = 0
        self.points = []
        self.points.append((self.coordinates[0], self.coordinates[1]))
        self.points.append((self.coordinates[0] + int(max(self.power, 10) * math.cos(self.angle)), 
                            self.coordinates[1] - int(max(self.power, 10) * math.sin(self.angle))))
        self.points.append((self.coordinates[0] + int(max(self.power, 10) * math.cos(self.angle)) - int(20 * math.sin(self.angle)), 
                            self.coordinates[1] - int(max(self.power, 10) * math.sin(self.angle)) - int(20 * math.cos(self.angle))))
        self.points.append((self.coordinates[0] - int(20 * math.sin(self.angle)), 
                            self.coordinates[1] - int(20 * math.cos(self.angle)))) 
    
    def draw(self): 
        """
        Draws the gun on the screen.
        """
        if self.points == []:
            self.targetting()
        polygon(screen, self.color, self.points)
        polygon(screen, (0, 0, 0), self.points, 1)
    
    def shoot(self):
        """
        Makes a gun shot. Make the gun isn't active, reduce the current power to the min_power. 

        Returns
        -------
        new_ball : class Ball() - created bullet.

        """
        self.live = False
        velocity = [int( self.power * math.cos(self.angle)), -int(1 * self.power * math.sin(self.angle))]
        if (10 <= self.power <= 20):
            color = Green1
        elif (20 < self.power <= 30):
            color = Green2
        elif (30 < self.power <= 40):
            color = Green3
        elif (40 < self.power <= 50):
            color = Green4
        coordinates = list(self.coordinates)    
        new_ball = Ball(coordinates, velocity, color)
        self.power = self.power_min
        return new_ball

    
class game_body():
    """
    This class is responsible for all main function about the process of the game
    """
    def __init__(self, number_targets = 3):
        """
        Creats the gun, set targets. 

        Parameters
        ----------
        number_targets : int - the number of targets on the screen (the default is 3).
        targets: list of the class Target() - the list of all targets which are on the screen.
        balls: list of the class Ball() - the list of all bullets which are on the screen.
        flag_finish: bool - True if the user wants to exit.
        score: int - the number of hitted targets during the game.
        num_shoot: int - the number of shots during the game.
        """
        self.number_targets = number_targets
        self.gun = Gun()
        self.targets = []
        self.balls = []
        self.flag_finish = False
        for i in range(number_targets):
            self.targets.append(Target())
        self.score = 0
        self.num_shoot = 0
    
    def whats_up(self, events):
        """
        Checks events.
        If the user click the mouse, activates the gun.
        If the user release the mouse, shoots the gun.
        Moves the gun based on user pressing buttons.
        If the user wants to exit, changes flag_finish.
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.flag_finish = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.gun.coordinates[1] -= 15
                    self.gun.coordinates[1] %= size[1]
                elif event.key == pygame.K_DOWN:
                    self.gun.coordinates[1] += 15
                    self.gun.coordinates[1] %= size[1]
                elif event.key == pygame.K_RIGHT:
                    self.gun.coordinates[0] += 15
                    self.gun.coordinates[0] %= size[0]
                elif event.key == pygame.K_LEFT:
                    self.gun.coordinates[0] -= 15
                    self.gun.coordinates[0] %= size[0]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.live = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:    
                    self.gun.live = False
                    self.balls.append(self.gun.shoot())
                    self.num_shoot += 1
    
    def write_score(self):
        """
        Writes score and num_shoot on the screen.
        """
        f1 = pygame.font.Font(None, 40)
        text = f1.render('You have done ' + str(self.num_shoot) + ' shots. Your score: ' + str(self.score), 1, (139, 0, 0))
        screen.blit(text, (50, 605))
        
    def check_balls(self):
        """
        Checks all balls on the screen whether they are dead. If yes, delete them.
        """
        balls_for_delete = []
        for i, ball in enumerate(self.balls):
            if not ball.live:
                balls_for_delete.append(i)
        for i in reversed(balls_for_delete):
            self.balls.pop(i)

    def check_target(self):
        """
        Checks all targets on the screen whether they are hitted. If yes, delete them. 
        """
        targets_for_delete = []
        for ball in self.balls:
            for i, target in enumerate(self.targets):
                if target.check(ball):
                    targets_for_delete.append(i)
                    self.score += 1
        targets_for_delete.sort()
        new = len(targets_for_delete)
        for i in reversed(targets_for_delete):
            self.targets.pop(i)
        for i in range(new):
            self.targets.append(Target())
            
    def draw_balls_targets(self):
        """
        Draws all balls and targets on the screen
        """
        for ball in self.balls:
            ball.draw()
        for target in self.targets:
            target.draw()
            
    def move_balls(self): 
        """
        Moves all bullets on the screen.
        """
        for ball in self.balls:
            ball.move()
            
    def process(self, events):
        """
        The main part of the programm. Do everything about the process of the game.

        Parameters
        ----------
        events : pygame.event.get().

        Returns
        -------
        flag_finish

        """
        screen.fill(fon_color)
        self.draw_balls_targets()
        self.gun.draw()
        self.move_balls()
        self.check_balls()
        self.check_target()
        self.whats_up(events)
        self.gun.power_up()
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos()
            self.gun.targetting(mouse_pos)
        self.write_score()    
        pygame.display.update()
        return self.flag_finish

body = game_body()
flag_finish = False

while not flag_finish:
    clock.tick(FPS)
    flag_finish = body.process(pygame.event.get())                    
                    
                    
                    
pygame.quit() 