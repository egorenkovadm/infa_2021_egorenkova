from random import randrange as rnd, choice
import pygame
from pygame.draw import *
import numpy as np
import math

pygame.init()

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
LAVENDER = (230, 230, 250)
PLUM = (221, 160, 221)
ORANGE = (255, 165, 0)
SEA = (32, 178, 170)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, CYAN, PLUM, SEA]
TARGET_COLORS = [RED, ORANGE, MAGENTA]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 3
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= self.ay
        self.x += self.vx
        self.y -= self.vy

        if self.x >= WIDTH:
            self.vx *= -1
        if self.y >= HEIGHT:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        distance = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5

        if distance <= (self.r + obj.r):
            return True
        else:
            return False


class Cube:
    def __init__(self, screen: pygame.Surface, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 3
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= self.ay
        self.x += self.vx
        self.y -= self.vy

        if self.x >= WIDTH:
            self.vx *= -1
        if self.y >= HEIGHT:
            self.vy *= -1

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x, self.y, self.r, self.r),

        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        distance = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5

        if distance <= (self.r + obj.r):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.x = 20
        self.y = 450
        self.vx = rnd(1, 10)
        self.vy = rnd(1, 10)
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.color_body = BLACK

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        if self.f2_power <= 50:
            new_ball = Cube(self.screen, self.x, self.y)
        else:
            new_ball = Ball(self.screen, self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def move(self, event):

        if event.key == pygame.K_DOWN:
            self.y += self.vy
        if event.key == pygame.K_UP:
            self.y -= self.vy
        if event.key == pygame.K_RIGHT:
            self.x += self.vx
        if event.key == pygame.K_LEFT:
            self.x -= self.vx

        if (self.x >= (WIDTH - 50)) or (self.x <= 10):
            self.vx *= -1
        if (self.y >= (HEIGHT - 50)) or (self.y <= 10):
            self.vy *= -1

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] == self.x:
                self.an = math.atan((event.pos[1] - self.y) / 0.1)
            else:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        rect(screen, self.color_body, (self.x - 30, self.y - 30, 60, 60,))
        line(self.screen, self.color, (self.x, self.y), (self.x + max(self.f2_power, 20) * math.cos(self.an),
                                                         self.y + max(self.f2_power, 20) * math.sin(self.an)), 5)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.vx = rnd(1, 10)
        self.vy = rnd(1, 10)
        self.r = rnd(5, 50)
        self.color = choice(TARGET_COLORS)
        self.screen = screen

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(5, 50)
        self.vx = rnd(1, 10)
        self.vy = rnd(1, 10)
        color = self.color = choice(TARGET_COLORS)
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y -= self.vy

        if (self.x >= WIDTH) or (self.x <= 170):
            self.vx *= -1
        if (self.y >= HEIGHT) or (self.y <= 0):
            self.vy *= -1


class TargetFast:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.vx = rnd(10, 25)
        self.r = rnd(20, 100)
        self.color = choice(TARGET_COLORS)
        self.screen = screen

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(5, 50)
        self.vx = rnd(1, 10)
        color = self.color = choice(TARGET_COLORS)
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        rect(self.screen, self.color, (self.x, self.y, self.r, self.r))

    def move(self):
        self.x += self.vx

        if (self.x >= (WIDTH - self.r)) or (self.x <= 170):
            self.vx *= -1

class Bomb:
    def __init__(self):
        self.x = rnd(300, 600)
        self.y = rnd(200, 400)
        self.r = 30
        self.number = 0

    def draw(self):
        circle(screen, BLACK, (self.x, self.y), self.r)

    def bang(self):
        """ Bomb explosion: creates new targets """
        self.number = rnd(1, 5)
        for i in range(self.number):
            k = rnd(1, 10)
            if k < 7 :
                Target.new_target()
                targets.append(Target())
            else:
                TargetFast.new_target()
                targets.append(TargetFast())




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
targets = [TargetFast(), Target()]
score = 0

screen.fill(WHITE)
clock = pygame.time.Clock()
gun = Gun(screen)
finished = False
while not finished:
    font = pygame.font.Font('freesansbold.ttf', 12)
    text1 = font.render('Уничтожено целей: ' + str(score), True, BLACK, (255, 255, 255))
    text1Rect = text1.get_rect()
    text1Rect.center = (70, 20)
    screen.blit(text1, text1Rect)
    pygame.display.update()

    # screen.fill(WHITE)
    rect(screen, WHITE, (0, 50, 800, 600))
    rect(screen, WHITE, (150, 0, 800, 600))
    gun.draw()
    for a in targets:
        a.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            gun.move(event)
    for a in targets:
        a.move()
    for b in balls:
        b.move()
        for a in targets:
            if b.hittest(a) and a.live:
                a.live = 0
                a.hit()
                a.new_target()

                # font = pygame.font.Font('freesansbold.ttf', 32)
                # text = font.render('Вы уничтожили цель за ' + str(bullet) + ' выстрелов', True, BLACK, (255,255,255))
                # textRect = text.get_rect()
                # textRect.center = (400, 300)
                # screen.blit(text, textRect)
                # pygame.display.update()

                # pygame.time.wait(200)
                score += 1
                bullet = 0

    gun.power_up()

pygame.quit()
