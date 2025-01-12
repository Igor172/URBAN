import pygame as pg
import logging


logger1 = logging.getLogger('MovingLogger')
logging.basicConfig(
    level=logging.INFO,
#    handlers=[logging.FileHandler('movelogger.log', mode='w', encoding='utf-8')]
)


class Tank(pg.sprite.Sprite): #Создает образы и позволяет работать с ними
    def __init__(self):
        super().__init__()
#        self.image = pg.Surface((50, 50)) #Создаем изображение поверхности(местности)
#        self.image.fill('green')          #Раскрашиваем изображение
        self.image = pg.transform.scale(pg.image.load('../images/tank.png'),(116, 60))#Вместо двух верхних строк кода
        self.normal_image = self.image
        self.big_image = pg.transform.scale(pg.image.load('../images/tank.png'),(232, 120))
        self.little_image = pg.transform.scale(pg.image.load('../images/tank.png'), (58, 60))
        self.rect = self.image.get_rect()


    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s]:
            self.rect.y += 1
        if keys[pg.K_w]:
            self.rect.y -= 1
        if keys[pg.K_a]:
            self.rect.x -= 1
        if keys[pg.K_d]:
            self.rect.x += 1

        if self.rect.centerx < 150:
            self.image = self.little_image
        elif 150 < self.rect.centerx < 300:
            self.image = self.normal_image
        elif self.rect.centerx > 300:
            self.image = self.big_image



    def moving_logger(self):
        keys = pg.key.get_pressed()
        if any([keys[pg.K_s], keys[pg.K_w], keys[pg.K_a], keys[pg.K_d]]):
            logger1.info(f'Произошло движение: {self.rect.x}, {self.rect.y}')


    def update(self, screen):
        self.move()
        self.moving_logger()
        pg.draw.rect(screen, 'red', self.rect, 1)
        screen.blit(self.image, self.rect)#self.image - то что хотим отобразить(картинка), self.rect - то где хотим отобразить
                                          #сама поверхность координатами не обладает - только набором пикселей