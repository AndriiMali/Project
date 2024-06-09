import pygame
from random import randint

WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

platform_num = 3
circle_num = 5

circles = []
platformes = []

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("background.jpg"), SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords


    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys [pygame.K_w]:
            self.rect.y -= 5












circle = GameSprite("circle.png", (50, 50), (400, 150))
platform = GameSprite("square.png", (200, 35), (600, 300))
item = GameSprite("square.png", (500,400), (0, 600))
stickman = GameSprite("stickman.png", (100, 100), (100, 400))

for i in range(circle_num):
    new_circle = GameSprite("circle.png", (50, 75), (randint(100, 1200), randint(50, 50)))
    circles.append(new_circle)

for i in range(platform_num):
    new_platform = GameSprite("square.png", (50, 75), (randint(600, 1200), randint(200, 900)))
    platformes.append(new_platform)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background, (0, 0))
    stickman.reset()
    item.reset()
    platform.reset()
    for c in circles:
        c.reset()
    for t in platformes:
        t.reset()
    pygame.display.update()
    clock.tick(FPS)
