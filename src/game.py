import pygame as pg
import constants as const
import random
from tile import Tile

class Game(object):
    def __init__(self):
        
        self.root = pg.display.set_mode(const.WIND_SIZE)
        self.clock = pg.time.Clock()

        self.score = 0
        self.game_over = False
        self.tile_list = pg.sprite.Group()

        self.root.fill(const.WHITE)

        self.create_tiles()
        self.set_tiles_position()
        self.tile_list.draw(self.root)

        
        
    def set_tiles_position(self):
        positions = [
            (x + 1, y + 1)
            for x in range(4)
            for y in range(4)
        ]

        for tile in self.tile_list:
            cordenates = random.choice(positions)
            tile.rect.x = cordenates[0]
            tile.rect.y = cordenates[1]
            positions.remove(cordenates)




    def run_logic(self, a):
        a + 1
        
        
        
    def create_tiles(self):
        for i in range(15):
            self.tile_list.add(Tile(str(i + 1)))

        self.tile_list.add(Tile("null"))



# tile.rect.x = x - const.SCREEN_WIDTH
# tile.rect.y = y - const.SCREEN_HEIGHT