import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pygame as pg
from settings import Settings
from ship import Ship
pg.init()

class AlienInvasion:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pg.display.flip()
            self.clock.tick(60)

if __name__=='__main__':
    ai = AlienInvasion()
    ai.run_game()

###I'm dropping this project as learning Pygame won't help me in future###

