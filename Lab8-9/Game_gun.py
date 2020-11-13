import pygame
from pygame.draw import *
from random import randint
import math

pygame.init()
pygame.font.init()

FPS = 30
size = (800, 600)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

#Colours that we will use
RED = (255, 57, 57)
BLUE = (0, 128, 255)
YELLOW = (255, 255, 120)
GREEN = (128, 255, 0)
MAGENTA = (255, 136, 255)
CYAN = (139, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball():
    def __init__(self, coordinates, velocity, radius = 15, color = None):
        if color == None:
            color = COLORS[randint(0, len(COLORS)-1)]
        self.alive = True
        self.color = color
        self.coordinates = coordinates
        self.velocity = velocity
        self.radius = radius

    def move(self, g = 3):
        self.velocity[1] += g
        for i in range(2):
            self.coordinates[i] += self.velocity[i]
        self.check_walls()
        if (self.velocity[0]**2 + self.velocity[1]**2 < 6**2) and (self.coordinates[1] > size[1] - 2*self.radius):
               self.alive = False

    def check_walls(self):
        if (self.coordinates[0] <= self.radius) or (self.coordinates[0] >= size[0] - self.radius):
            self.velocity[0] = -self.velocity[0]
        if (self.coordinates[1] <= self.radius) or (self.coordinates[0] >= size[1] - 2*self.radius):
            self.velocity[1] = -self.velocity[1]
            self.alive = False
    
    def draw(self, screen):
        circle(screen, self.color, self.coordinates, self.radius)


class Gun():
    def __init__(self, coord = [20, size[1] // 2], power_min = 10, power_max = 50):
        self.coord = coord
        self.angle = 0
        self.power_min = power_min
        self.power_max = power_max
        self.power = power_min
        self.activation = False
        self.points = []
    
    def start_work(self):
        self.activation = 1
    
    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.angle = math.atan((350 - event[1]) / (event[0] - 20))
        else:
            self.angle = 0
        if self.activation:
            self.points = []
            self.points.append((self.coord[0], self.coord[1]))
            self.points.append((self.coord[0] + int(max(self.power, 20) * math.cos(self.angle)), 
                           self.coord[1] - int(max(self.power, 20) * math.sin(self.angle))))
            self.points.append((self.coord[0] + int(max(self.power, 20) * math.cos(self.angle)) - int(20 * math.sin(self.angle)), 
                           self.coord[1] - int(max(self.power, 20) * math.sin(self.angle)) - int(20 * math.cos(self.angle))))
            self.points.append((self.coord[0] - int(20 * math.sin(self.angle)), 
                           self.coord[1] - int(20 * math.cos(self.angle))))    
         
    def draw(self):
        if self.points != []:
            polygon(screen, (255, 255, 120), self.points)
            polygon(screen, (0, 0, 0), self.points, 1)
        else:
            self.targetting()
            polygon(screen, (255, 255, 120), self.points)
            polygon(screen, (0, 0, 0), self.points, 1)

        
    def power_up(self):
        if self.activation and (self.power < self.power_max):
                self.power += 1
    
    def gun_shoot(self):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        velocity = [int(self.power * math.cos(self.angle)), -int(0.4*self.power * math.sin(self.angle))]
        new_ball = Ball(list(self.coord), velocity)
        self.activation = 0
        self.power = 10
        return new_ball
    


class target():
    def __init__(self, coordinates = None, color = (255, 57, 57), radius = 20):
        """ Инициализация новой цели. """
        if coordinates == None:
            self.coordinates = (randint(radius, size[0] - radius), randint(radius, size[1] - radius))
        self.radius = randint(5, 50)
        self.color = color
        self.points = 0
        
    def draw(self, screen):
        circle(screen, self.color, self.coordinates, self.radius)
    
    def check_hit(self, ball):
        dist = sum([(self.coordinates[i] - ball.coordinates[i])**2 for i in range(2)])**0.5
        min_dist = self.radius + ball.radius
        return (dist <= min_dist)
        

class Manager():
    def __init__(self, n_targets = 3):
        self.gun = Gun()
        self.targets = []
        self.n_targets = n_targets
        self.balls = []   
        self.missions()    
        
    def move(self):
        
        for i in self.balls:
            i.move(g = 1)
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move(g = 1)
            if not ball.alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)

        
    def process(self, events, screen):
        done = self.whats_up(events)
        self.gun.activation = True
        self.draw()
        self.move()
        self.collide()
        self.check_alive()
        self.gun.activation = True
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.missions()        
        if pygame.mouse.get_focused():
            self.gun.activation = True
            mouse_pos = pygame.mouse.get_pos()
            self.gun.targetting(mouse_pos)
        return done
        
    def draw(self):
        screen.fill((255,255,255))
        self.gun.draw()
        for i in self.balls:
            i.draw(screen)
        for target in self.targets:
            target.draw(screen)

        
    def whats_up(self, events):
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.gun.activation = True
                    self.gun.coord[1] -= 20
                elif event.key == pygame.K_DOWN:
                    self.gun.activation = True
                    self.gun.coord[1] += 20
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.power_up()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.gun_shoot())             
        if pygame.mouse.get_focused():
            mouse_pos = pygame.mouse.get_pos()
            self.gun.targetting(mouse_pos)
        return done
    
    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
   
    def missions(self):
        for i in range(self.n_targets):
            self.targets.append(target(radius=randint(1, 30)))
    
    def collide(self):
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_hit(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
        targets_c.sort()
        for j in reversed(targets_c):
            self.targets.pop(j)


mgr = Manager(3)

done = False

while not done:
    clock.tick(FPS)
    done = mgr.process(pygame.event.get(), 3)
    pygame.display.update()
    
    
pygame.quit()