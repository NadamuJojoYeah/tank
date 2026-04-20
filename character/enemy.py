import pygame
import time
import random
import math
from character import player

class Enemy:
    def __init__(self, image_file, size, blood):
        self.original_image = pygame.image.load(image_file)
        self.size = size
        self.x = random.randint(self.size, 800 - self.size)
        self.y = random.randint(self.size, 600 - self.size)
        self.original_image = pygame.transform.scale(self.original_image, (size * 2, size * 2))
        self.image = self.original_image.copy()
        self.speed = 1
        self.blood = blood
        self.last_attack_time = 0
        self.attack_interval = 1000
        #self.refresh_time=pygame.time.get_ticks() #最新改动
        self.death_time = None

    def draw(self, screen):
        rotated_rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, rotated_rect.topleft)

    def move_towards_player(self, player_x, player_y):
        dx = player_x - self.x
        dy = player_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if 15<=distance < 350:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

            angle = math.degrees(math.atan2(-dy, dx)) - 90
            self.image = pygame.transform.rotate(self.original_image, angle)

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

    def attacked(self, damage):
        self.blood -= damage
        if self.blood <= 0:
            #self.refresh_time=pygame.time.get_ticks() #改动
            return True
        return False

    def died(self):
        self.death_time = time.time()

    def rebirth(self, blood):
        print(time.time() - self.death_time)
        if self.death_time != None and time.time() - self.death_time >= 2:
            self.death_time = None
            self.blood = blood

