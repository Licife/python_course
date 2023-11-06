import pygame

class Ship:
    """飞船的类"""
    def __init__(self, al_game):
        """初始化飞船"""
        self.screen = al_game.screen
        self.screen_rect = al_game.screen.get_rect()

        self.image = pygame.image.load('Images/ship.bmp')