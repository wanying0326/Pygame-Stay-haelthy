import pygame
from setting import *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.player_img
        self.rect = self.image.get_rect()
        self.radius = 25
        # pygame.draw.circle(self.image, DODGERBLUE, self.rect.center, self.radius)
        self.rect.centerx = DISPLAY_WIDTH/2
        self.rect.bottom = DISPLAY_HIGHTH - 55
        self.speedx = 4
        

    def update(self):
        #左右移動
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx 
        elif key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx 
        #不超出視窗
        if self.rect.right > DISPLAY_WIDTH :
            self.rect.right = DISPLAY_WIDTH 
        elif self.rect.left < 0:
            self.rect.left = 0

    def hit(self):
        fist = Fist(self.game, self.rect.centerx, self.rect.top)
        self.game.all_sprites.add(fist) #使用main的all_sprite，所以player要引入game
        self.game.all_fists.add(fist)


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.mouth_img
        self.rect = self.image.get_rect()
        # self.radius = 18
        self.rect.x = x
        self.rect.bottom = DISPLAY_HIGHTH - 5

class Trash_food(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = random.choice(self.game.trash_food_img_list)
        self.rect = self.image.get_rect()
        self.radius = 18
        #觸碰半徑可視化
        # pygame.draw.circle(self.image, DODGERBLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(0,DISPLAY_WIDTH-40)
        self.rect.y = random.randrange(-300,0)
        self.speedy = random.randrange(1,3)
        self.speedx = random.randrange(-2,2)

    def update(self):
        #掉下來
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #跑出視窗重置
        if self.rect.right > DISPLAY_WIDTH or self.rect.left < 0:
            self.speedx *= -1

class Fist(pygame.sprite.Sprite):
    def __init__(self, game, player_centerx, player_top):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.fist_img
        self.rect = self.image.get_rect()
        self.radius = 15
        # pygame.draw.circle(self.image, DODGERBLUE, self.rect.center, self.radius)
        self.rect.centerx = player_centerx
        self.rect.bottom = player_top
        self.speedy = -8

    def update(self):
        self.rect.bottom += self.speedy
        #超出視窗刪除
        if self.rect.bottom < 0:
            self.kill()

class Healthy_food(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = random.choice(self.game.healthy_food_img_list)
        self.rect = self.image.get_rect()
        self.radius = 18
        #觸碰半徑可視化
        # pygame.draw.circle(self.image, DODGERBLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(0,DISPLAY_WIDTH-40)
        self.rect.y = random.randrange(-300,0)
        self.speedy = random.randrange(1,3)
        self.speedx = random.randrange(-2,2)

    def update(self):
        #掉下來
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #跑出視窗重置
        if self.rect.right > DISPLAY_WIDTH or self.rect.left < 0:
            self.speedx *= -1