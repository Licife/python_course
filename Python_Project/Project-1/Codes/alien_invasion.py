import sys
import pygame
from Setting import Settings
from Ship import Ship


class AlienInvasion:
    def __init__(self):
        """初始化游戏资源"""
        pygame.init()

        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Alien Invasion')

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        # 键盘与鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # 每次循环重新绘制
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 抹除旧屏幕 重新绘制新屏幕
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
