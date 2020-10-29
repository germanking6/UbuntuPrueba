import pygame as pg
import random

class ken(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("ken.png")
        self.pos=self.image.rect.get_rect()
        self.pos.x=random.randrange(900)
        self.pos.y=random.randrange(600)

    def attack(self, player_pos_x, player_pos_y):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pg.math.Vector2(
            player_pos_x - self.rect.x,
            player_pos_y - self.rect.y
        )
        dirvect.normalize()

        # Move along vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)

class student(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("")
        self.pos=self.image.rect.get_rect()