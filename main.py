import pygame
from character import ball
from character import player
from character import enemy
import time
import os

# 地图路径
map_file = "image/map/img.png"

# 敌人状态
ISDIED= False
def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tank")
    fps = pygame.time.Clock()
    player1 = player.Player(400, 300, "image/tank_image/tank_1.png", 20)
    # 建立敌人数组

    enemy1 = enemy.Enemy("image/tank_image/tank_1.png", 20, 10)
    enemy2=enemy.Enemy("image/tank_image/tank_1.png", 20, 10)
    list_enemy=[enemy1,enemy2]

    map_img=pygame.image.load(map_file).convert()
    map_img=pygame.transform.scale(map_img,(800,600))
    balls = []

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                px, py = player1.get_pos()
                mx, my = pygame.mouse.get_pos()
                angle= player1.get_angle()
                balls.append(ball.Ball(px, py, mx, my,angle))
        # 填充背景颜色
        # screen.fill((0, 128, 0))
        screen.blit(map_img,(0,0))
        # 获取按键元组

        keys = pygame.key.get_pressed()

        enemy1.move_towards_player(player1.x, player1.y)

        # 创建人物
        player1.move(keys, 800, 600)
        player1.draw(screen)

        # 遍历小球
        for b in balls[:]:
            b.move()
            b.draw(screen)
            dx = b.x - enemy1.x
            dy = b.y - enemy1.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < (b.radius + enemy1.size):
                if enemy1.attack(1):
                    ISDIED=True
                    attack_time = time.time()
                    list_enemy.remove(enemy1)
                balls.remove(b)
                continue
            if b.is_out_of_screen(800, 600):
                balls.remove(b)

        if time.time() - attack_time >= 1000 and len(list_enemy) == 1:
            list_enemy.append(enemy1)   #这个地方错了？
        # 创建敌人
        enemy1.draw(screen)

        fps.tick(144)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
#此页面用于测试
