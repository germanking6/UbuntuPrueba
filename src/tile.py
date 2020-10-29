import pygame as pg
import constant as const

class Tile(pg.sprite.Sprite):
    def __init__(self, index):
        super().__init__()
        self.value = index
        self.image = pg.image.load(
            const.IMG_ADDRESS +
            str(index) +
            ".png"
        )
        self.rect = self.image.get_rect()

        self.image.set_colorkey(const.BLACK)
        