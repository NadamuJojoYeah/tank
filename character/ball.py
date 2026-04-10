import pygame
import math
class Ball:
    def __init__(self, x, y, target_x, target_y, radius=5, speed=8):
        self.x = x
        self.y = y
        self.radius = radius
        dx = target_x - x
        dy = target_y - y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            self.speedX = (dx / distance) * speed
            self.speedY = (dy / distance) * speed
        else:
            self.speedX = 0
            self.speedY = 0

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def is_out_of_screen(self, screen_width, screen_height):
        return (self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

