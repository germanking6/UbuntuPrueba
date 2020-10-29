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
        speed=4
        boss=pg.sprite.Group()
        boss.add(self.Ken)
        # Updates students position.
        while not end:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end = True

            # Update student's position.
            mousePos=pg.mouse.get_pos()
            self.Student.rect.x=mousePos[0]
            self.Student.rect.y=mousePos[1]
            
            # Creates HW when there is non on map.
            if not tareas:
                homework=HomeWork()
                homeworks.add(homework)
                self.sprytes.add(homework)
                tareas=True

            # Updates Professor position to follow student.
            self.Ken.attack(self.Student.rect.x, self.Student.rect.y,speed)
            
            # Student gets HW.
            hit=pg.sprite.spritecollide(self.Student,homeworks,True)
            for homework in hit:
                score += 5
                speed=1.1*speed
                print(score)
                tareas=False
            screen.fill(WHITE)
            hitEnd=pg.sprite.spritecollide(self.Student,boss,True)
            for ken in hitEnd:
                print("se acabo")
                end=True
            # DIsplay sprites.
            self.sprytes.draw(screen)
            pg.display.flip()
            clock.tick(60)
        print("puntaje final: ", score)
    
    def play(self):
        self.initiate()