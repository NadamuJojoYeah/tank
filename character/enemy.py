import pygame
import time
import random
from character import player
class Enemy:
    # 此行size指的是半径
    def __init__(self, image_file, size,blood):
        self.original_image = pygame.image.load(image_file)
        self.size = size
        self.x=random.randint(self.size,800-self.size)
        self.y=random.randint(self.size,600-self.size)
        self.image = pygame.transform.scale(self.original_image, (size*2,size*2))
        self.speed = random.randint(1,5)
        self.blood=blood
        self.last_attack_time = 0
        self.attack_interval = 1000  # 攻击间隔（毫秒）

    def draw(self,screen):  #hu绘制
        screen.blit(self.image,(self.x-self.size,self.y-self.size))

    def move_towards_player(self, player_x, player_y):
        dx = player_x - self.x
        dy = player_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    def attack(self, player, damage=1):
        current_time = pygame.time.get_ticks()

        dx = player.x - self.x
        dy = player.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < self.size + player.size and current_time - self.last_attack_time > self.attack_interval:
            self.last_attack_time = current_time
            player.attacked(damage)
            return True
        return False

    def attack(self, damage):
        self.blood -= damage
        if self.blood <= 0:
            return True
        return False



