###########################################
#тестирование и логирование игры в танчики#
###########################################

import pygame as pg
from player import Tank


screen = pg.display.set_mode((600, 600))
player = Tank()

fps = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    fps.tick(60)
    player.update(screen)
    pg.display.update()