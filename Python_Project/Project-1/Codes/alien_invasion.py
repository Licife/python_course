import sys
import pygame
from Setting import Settings


class AlienInvasion:
    def __init__(self):
        """初始化游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Alien Invasion')

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 键盘与鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            # 抹除旧屏幕 重新绘制新屏幕
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    al = AlienInvasion()
    al.run_game()
