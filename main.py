import pygame
from random import randint
import math


WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60

platform_num = 3
circle_num = 5

circles = pygame.sprite.Group()
platformes = pygame.sprite.Group()

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("background.jpg"), SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(pygame.image.load(filename), size)
        self.rect = self.image.get_rect()
        self.rect.center = coords


    def reset(self):
        window.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, filename, size, coords):
        super().__init__(filename, size, coords)
        self.angle = math.pi / 4
        self.speed = 0
        self.acceleration = 0
        self.attached = False
    def update(self, platforms, circles):
        keys = pygame.key.get_pressed()
        if self.attached:
            self.acceleration = 1
            self.speed += self.acceleration
        else:
            if keys[pygame.K_d]:
                self.rect.x += 5
            elif keys[pygame.K_a]:
                self.rect.x -= 5
            elif keys[pygame.K_w]:
                self.rect.y -= 8
            if not self.collide_platform(platforms):
                self.rect.y += 4
            collided_circles = pygame.sprite.spritecollide(self, circles, False)
            if collided_circles:
                self.attached = True
                point = collided_circles[0].rect.center
                

    def collide_platform(self, platforms):
        collided_platforms = pygame.sprite.spritecollide(self, platforms, False)
        for c in collided_platforms:
            if self.rect.bottom > c.rect.top:
                return True
        return False
        
















item = GameSprite("square.png", (500,400), (0, 600))
stickman = Player("stickman.png", (100, 100), (100,300))

circles.add(
    GameSprite("circle.png", (50, 75), (300, 50)),
    GameSprite("circle.png", (50, 75), (600, 50)),
    GameSprite("circle.png", (50, 75), (900, 50))
)
for i in range(platform_num):
    new_platform = GameSprite("square.png", (50, 75), (randint(WIDTH//2, WIDTH), randint(200, HEIGHT-200)))
    platformes.add(new_platform)

platformes.add(item)
#!platformes.add(GameSprite("square.png", (50,75), (100, 500)))    

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background, (0, 0))
    stickman.update(platformes, circles)
    stickman.reset()
    circles.draw(window)
    platformes.draw(window)
    pygame.display.update()
    clock.tick(FPS)
