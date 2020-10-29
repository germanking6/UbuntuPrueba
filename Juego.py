import pygame as pg
from Personajes import ken, student
from points import HomeWork, Proyect

class Juego(pg.sprite.Sprite):
    def __init__(self):
        self.sprytes = pg.sprite.Group()
        self.Ken = ken()
        self.Student = student()

    def initiate(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        tareas = False
        score = 0
        pg.init()
        screen = pg.display.set_mode([950, 950])
        clock = pg.time.Clock()
        end=False
        pg.mouse.set_visible(0)
        homeworks=pg.sprite.Group()
        self.sprytes.add(self.Student)
        self.sprytes.add(self.Ken)

        while not end:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

            mousePos=pg.mouse.get_pos()
            self.Student.rect.x=mousePos[0]
            self.Student.rect.y=mousePos[1]
            
            if not tareas:
                homework=HomeWork()
                homeworks.add(homework)
                self.sprytes.add(homework)
                tareas=True
            
            hit=pg.sprite.spritecollide(self.Student,homeworks,True)
            for homework in hit:
                score += 5
                print(score)
                tareas=False
            screen.fill(WHITE)

            self.sprytes.draw(screen)
            pg.display.flip()
            clock.tick(60)
    
    def play(self):
        self.initiate()