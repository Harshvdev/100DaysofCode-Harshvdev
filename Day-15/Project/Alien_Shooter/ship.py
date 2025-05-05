import pygame as pg

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        original_image = pg.image.load('images/plane.png')
        self.image = pg.transform.scale(original_image, (100, 75))  # (width, height) in pixels

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
