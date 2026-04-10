import pygame
import math
class Player:
    def __init__(self, x, y, image_file, size):
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(image_file).convert_alpha()
        self.size = size
        self.image = pygame.transform.scale(self.original_image, (size * 2, size * 2))
        self.speed = 5
        self.blood=15
        self.angle=0
        self.hp=20

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))     # 获取旋转后图片的矩形，以玩家位置为中心
        screen.blit(rotated_image, rect.topleft)  # 使用矩形左上角坐标绘制，确保旋转后不偏移

    def get_pos(self):
        return self.x, self.y


    def rotate_towards_mouse(self):
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.x
        dy = my - self.y
        self.angle = math.degrees(math.atan2(-dy, dx)) - 90

    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.x = max(self.size, min(screen_width - self.size, self.x))
        self.y = max(self.size, min(screen_height - self.size, self.y))

        self.rotate_towards_mouse()

    def attacked(self,cnt):
        self.blood-=cnt
        if self.blood<=0:
            return True
        return False
