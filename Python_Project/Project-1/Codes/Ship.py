import pygame


class Ship:
    """飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('D:/Study/python_works/Python_Project/Project-1/Images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
