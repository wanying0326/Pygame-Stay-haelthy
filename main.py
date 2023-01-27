import pygame
from setting import *
from sprite import *
import os

class Game:
    def __init__(self):
    #遊戲初始化
        pygame.init()
        
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HIGHTH))
        pygame.display.set_caption("Stay haelthy")

        self.clock = pygame.time.Clock()
        self.running = True
        self.load_img()

        self.player = Player(self)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.mouth_group = pygame.sprite.Group()
        for i in range(0, 500, 100):
            self.wall = Wall(self, i)
            self.all_sprites.add(self.wall)
            self.mouth_group.add(self.wall)
       
        self.all_trash_foods = pygame.sprite.Group()
        self.all_fists = pygame.sprite.Group()
        self.all_healthy_foods = pygame.sprite.Group()
        
        #掉落物數目迴圈
        for i in range(6):
            trash_food = Trash_food(self)
            self.all_sprites.add(trash_food)
            self.all_trash_foods.add(trash_food)

        for i in range(2):
            healthy_food = Healthy_food(self)
            self.all_sprites.add(healthy_food)
            self.all_healthy_foods.add(healthy_food)
        
        #分數
        self.score = 0      

    def new(self):
        pass
        
    def load_img(self):
        #載入圖片
        self.player_img = pygame.image.load(os.path.join("img", "eye.png")).convert()
        self.player_img = pygame.transform.scale(self.player_img, (60, 60))
        self.player_img.set_colorkey(DODGERBLUE)
       
        self.fist_img = pygame.image.load(os.path.join("img", "fist.png")).convert()
        self.fist_img = pygame.transform.scale(self.fist_img, (30, 40))
        self.fist_img.set_colorkey(BLACK)

        self.mouth_img = pygame.image.load(os.path.join("img", "mouth2.png"))
        self.mouth_img = pygame.transform.scale(self.mouth_img, (90, 50))
        self.mouth_img.set_colorkey(DODGERBLUE)
        
        self.trash_food_img_list = []
        for i in range(1,7):
            self.trash_food_img = pygame.image.load(os.path.join("img", f"trash_food{i}.png")).convert()
            self.trash_food_img = pygame.transform.scale(self.trash_food_img, (40, 40))
            if i == 1 or i == 3 or i == 5:
                self.trash_food_img.set_colorkey(BLACK)
            else:
                self.trash_food_img.set_colorkey(WHITE)
            self.trash_food_img_list.append(self.trash_food_img)

        self.healthy_food_img_list = []
        for i in range(1,8):
            self.healthy_food_img = pygame.image.load(os.path.join("img", f"healthy_food{i}.png")).convert()
            self.healthy_food_img = pygame.transform.scale(self.healthy_food_img, (40, 40))
            if i == 4:
                self.healthy_food_img.set_colorkey(WHITE)
            else:
                self.healthy_food_img.set_colorkey(BLACK)
            self.healthy_food_img_list.append(self.healthy_food_img)

    def events(self):#取得輸入
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.hit()

    def updates(self):#更新指令
        pygame.display.update()
        self.all_sprites.update()

    def draw_text(self):
        pass

    def draw(self):#畫面輸出
        self.screen.fill(AQUAMARINE)
        self.all_sprites.draw(self.screen)

    def collision(self):
        #拳頭與食物碰撞判斷
        hit_list1 = pygame.sprite.groupcollide(self.all_trash_foods, self.all_fists, True, True, pygame.sprite.collide_circle)
        hit_list2 = pygame.sprite.groupcollide(self.all_healthy_foods, self.all_fists, True, True, pygame.sprite.collide_circle)
        for i in hit_list1: #刪除的垃圾食物重新創造
            self.score += 10
            trash_food = Trash_food(self)
            self.all_sprites.add(trash_food)
            self.all_trash_foods.add(trash_food)
        for i in hit_list2: 
            self.score -= 20
            healthy_food = Healthy_food(self)
            self.all_sprites.add(healthy_food)
            self.all_healthy_foods.add(healthy_food)

        #垃圾食物與嘴巴碰撞判斷
        attack_list = pygame.sprite.groupcollide(self.all_trash_foods, self.mouth_group, True, False)
        for i in attack_list: #刪除的垃圾食物重新創造
            trash_food = Trash_food(self)
            self.all_sprites.add(trash_food)
            self.all_trash_foods.add(trash_food)

        #健康食物與嘴巴碰撞判斷
        eat_list = pygame.sprite.groupcollide(self.all_healthy_foods, self.mouth_group, True, False)
        for i in eat_list: 
            healthy_food = Healthy_food(self)
            self.all_sprites.add(healthy_food)
            self.all_healthy_foods.add(healthy_food)

    
    def run(self):
        self.events()
        self.updates()
        self.collision()
        self.draw()
        self.clock.tick(FPS)
   
    def game_intro(self):
        pass

    def gameover(self):
        pass

    def quitgame(self):
        pygame.quit()

    
#遊戲迴圈
game = Game()
while game.running:
    game.run()
game.quitgame() 
    
    