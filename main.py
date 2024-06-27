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
        self.damping = 0.999
    def update(self, platforms, circles):
        prev_x, prev_y = self.rect.x, self.rect.y
        keys = pygame.key.get_pressed()
        if self.attached:
            self.acceleration = -0.50 / 50 * math.sin(self.angle)
            self.speed += self.acceleration
            self.speed *= self.damping
            self.angle += self.speed
            self.rect.centerx = self.point[0] + 50 * math.sin(self.angle)
            self.rect.y = self.point[1] + 50 * math.cos(self.angle)
            if keys[pygame.K_SPACE]:
                self.attached = False



        else:
            if keys[pygame.K_w]:
                self.rect.y -= 4
            elif not self.collide_platform_top(platforms):
                self.rect.y += 4
                if keys[pygame.K_d]:
                    self.rect.x += 5
                elif keys[pygame.K_a]:
                    self.rect.x -= 5
            
            collided_platforms = pygame.sprite.spritecollide(self, platforms, False)
            if collided_platforms:
                self.rect.x = prev_x
                self.rect.y = prev_y

            collided_circles = pygame.sprite.spritecollide(self, circles, False)
            if collided_circles:
                self.attached = True
                self.point = collided_circles[0].rect.center
                

    def collide_platform_top(self, platforms):
        collided_platforms = pygame.sprite.spritecollide(self, platforms, False)
        for c in collided_platforms:
            if self.rect.bottom > c.rect.top and self.rect.bottom <= c.rect.bottom:
                return True
        return False
        
















item = GameSprite("square.png", (500,400), (0, 300))
stickman = Player("stickman.png", (75, 100), (100,50))

circles.add(
    GameSprite("circle.png", (50, 50), (300, 50)),
    GameSprite("circle.png", (50, 50), (450, 150)),
    GameSprite("circle.png", (50, 50), (600, 200)),
    GameSprite("circle.png", (50, 50), (750, 300)),
    GameSprite("circle.png", (50, 50), (900, 400)),
    GameSprite("circle.png", (50, 50), (700, 450))
)
#for i in range(platform_num):
    #new_platform = GameSprite("square.png", (50, 75), (randint(WIDTH//2, WIDTH), randint(300, HEIGHT-200)))
    #platformes.add(new_platform)

platformes.add(item)
platformes.add(GameSprite("square.png", (50,75), (775, 600)),
                GameSprite("square.png", (600,25), (350, 400)))  
finish = GameSprite("finish.jpg", (100, 230), (550, 530)) 
#GameSprite("square.png", (50,75), (300, 300)), GameSprite("square.png", (50,75), (600, 300)),
pause = False

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if not pause:
        window.blit(background, (0, 0))
        stickman.update(platformes, circles)
        stickman.reset()
        circles.draw(window)
        platformes.draw(window)
        finish.reset()
        if pygame.sprite.collide_rect(stickman, finish):
            pygame.font.init()
            font = pygame.font.Font(None, 30)
            text = font.render("YOU WIN!", True, (0, 255, 0))
            window.blit(text, (WIDTH/2, HEIGHT/2))
            pause = True
    pygame.display.update()
    clock.tick(FPS)
