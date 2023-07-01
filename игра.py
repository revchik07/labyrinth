import pygame as pg
import random
pg.init()
tiles = 25
window = pg.display.set_mode((tiles * 19, tiles * 17))
pg.display.set_caption("Лабиринт")
list_wall = ["1111111111111111111",
             "1000000000100000001",
             "1011101110101110101",
             "1000101010100010101",
             "1111101010111110101",
             "1000001010000000101",
             "1011111011111111101",
             "1010000000001000101",
             "1011101111101110101",
             "1000100000100010001",
             "1110111110101111101",
             "1000100000100000001",
             "1011101111111111111",
             "1010101000001000100",
             "0010101011101010100",
             "0010000010000010001",
             "1111111111111111111"]

class GameSprite:
    def __init__ (self, image, x,y, width, height,speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Hero(GameSprite):
    def control (self, walls):
        keys = pg.key.get_pressed()
        if keys [pg.K_a]:
            self.rect.x -= self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x += self.speed
        if keys [pg.K_d]:
            self.rect.x += self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.x -= self.speed
        if keys [pg.K_w]:
            self.rect.y -= self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.y += self.speed
        if keys [pg.K_s]:
            self.rect.y += self.speed
            for i in walls:
                if pg.sprite.collide_rect(self,i):
                    self.rect.y -= self.speed
class Enemy(GameSprite):
    def __init__(self, image, x, y, width, height, speed, direction):
        super().__init__(image, x, y, width, height, speed)
        self.direction = direction 
    def move(self):
        global walls 
        if self.direction == 0:
            self.rect.x += self.speed
            for i in walls:
                if pg.sprite.collide_rect(self, i):
                    self.rect.x -= self.speed
                    self.direction = 1
        if self.direction == 1:
            self.rect.x -= self.speed
            for i in walls:
                if pg.sprite.collide_rect(self, i):
                    self.rect.x += self.speed
                    self.direction = 0
enemy_1 = Enemy("image/враг.PNG", 1 * tiles, 1 * tiles, tiles, tiles,tiles//9, 1)
enemy_2 = Enemy("image/wa.png", 11 * tiles, 1 * tiles, tiles, tiles,tiles//9, 1)
enemy_3 = Enemy("image/враг.PNG", 3 * tiles, 7 * tiles, tiles, tiles,tiles//9, 1)                     
enemies = [enemy_1, enemy_2, enemy_3]
walls = []
floors = []
for i in range (len(list_wall)):
    for g in range (len(list_wall[i])):
        if list_wall [i][g] == "1":
            walls.append (GameSprite("image/wall.png",g* tiles, i* tiles, tiles, tiles,0))
        else:
            floors.append (GameSprite("image/Снимок.PNG",g* tiles, i* tiles, tiles, tiles,0))
player = Hero ("image/танк.png", 0, 15* tiles, tiles//1.2, tiles//1.2, tiles//5 )
finish_1 = GameSprite("image/fin.png", 18 * tiles, 14 * tiles, tiles, tiles, 0)
finish_2 = GameSprite("image/fin.png", 18 * tiles, 13 * tiles, tiles, tiles, 0)
music = pg.mixer.Sound("image/happyrock.mp3")
music.play(-1)
music.set_volume(0.1)

game = True
game_over = "image/l.png"
while game:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    for i in walls:
        i.reset()
    for i in floors:
        i.reset()
    player.reset()
    player.control(walls)
    for i in enemies:
        if pg.sprite.collide_rect(i, player):
            game = False 
        i.reset()
        i.move()
    finish_1.reset()
    finish_2.reset()
    if pg.sprite.collide_rect(finish_1, player):
        game_over = "image/загружено.png"
        game = False
    if pg.sprite.collide_rect(finish_2, player):
        game_over = "image/загружено.png"
        game = False
    pg.display.flip()
back = GameSprite(game_over, 0, 0,tiles * 19, tiles * 17,0)
while True:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    back.reset()
    pg.display.flip()