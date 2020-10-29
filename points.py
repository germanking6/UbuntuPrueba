import pygame as pg
import random

class HomeWork(pg.sprite.Sprite):
    def __init__(self):
        self.points=5
        self.image=pg.image.load("")
        self.pos=self.image.rect.get_rect()
        self.posAssign()
    def posAssign(self):
        self.pos.x=random.randrange(900)
        self.pos.y=random.randrange(600)       

class Proyect(pg.sprite.Sprite):
    def __init__(self):
        self.points=15
        self.image=pg.image.load("")
        self.pos=self.image.rect.get_rect()
        self.posAssign()
    def posAssign(self):
        self.pos.x=random.randrange(900)
        self.pos.y=random.randrange(600)