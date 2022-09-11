import pygame as pg
import time

pg.init()
window = pg.display.set_mode((300, 300))
clock = pg.time.Clock()


def hi():
    pass


if __name__ == "__main__":
    while True:
        clock.tick(60)
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            keyspressed = [keys[pg.K_w], keys[pg.K_a], keys[pg.K_s], keys[pg.K_d], keys[pg.K_SPACE]]
            # keyspressed=[keys[pg]]
            print(keyspressed)
