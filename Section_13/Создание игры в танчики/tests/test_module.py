import unittest
import pygame as pg
from player import Tank


class PlayerTest(unittest.TestCase):
    def test_moving(self):
        screen = pg.display.set_mode((500, 500))
        player = Tank()
        fps = pg.time.Clock()
        status = True

        while status:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    status = False
            screen.fill('black')
            fps.tick(60)
            player.update(screen)
            pg.display.update()

        width_result = player.rect.left >= 0 and player.rect.right <= screen.get_width()
        height_result = player.rect.top >= 0 and player.rect.bottom <= screen.get_height()

        return self.assertTrue(width_result and height_result,
                               f'Выход за границу {player.rect.x}, {player.rect.y}')



if __name__ == '__main__':
    unittest.main()