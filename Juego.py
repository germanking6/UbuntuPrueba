import pygame as pg
from Personajes import ken, student
from points import HomeWork, Proyect

class Juego(pg.sprite.Sprite):
    def __init__(self):
        
        sprytes = pg.sprite.Group()
        Ken = ken()
        sprytes.add(Ken)
        Student = student()
        sprytes.add(Student)
