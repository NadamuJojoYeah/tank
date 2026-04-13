import pygame
import math
class Ball:
    def __init__(self, x, y, target_x, target_y, radius=5, speed=8):
        self.x = x
        self.y = y
        self.radius = radius
        self.image=pygame.image.load("image/bullet_image/bullet_1.png").convert_alpha()
        self.angle=0
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
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))  # 获取旋转后图片的矩形，以玩家位置为中心
        screen.blit(rotated_image, rect.topleft)  # 使用矩形左上角坐标绘制，确保旋转后不偏移


    def get_pos(self):
        return self.x, self.y

    def move_rowards_play(self):
        mx,my=pygame.mouse.get_pos()
        dx=my-self.x
        dy=my-self.y
        self.angle=math.degrees(math.atan2(-dy,dx))-90
