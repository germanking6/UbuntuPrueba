import pygame as pg
import random

class ken(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("ken.png")
        self.pos=self.image.rect.get_rect()
        self.pos.x=random.randrange(900)
        self.pos.y=random.randrange(600)     

class student(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("")
        self.pos=self.image.rect.get_rect()