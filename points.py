import pygame as pg
import random

class HomeWork(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points=5
        self.image=pg.image.load("hongo.png")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(900)
        self.rect.y=random.randrange(600)       

class Proyect(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.points=15
        self.image=pg.image.load("")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(900)
        self.rect.y=random.randrange(600)