import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

# RGB colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def main():
    pg.display.set_caption("逃げろ!こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    
    # Create bomb surface
    bomb_surface = pg.Surface((20, 20))
    bomb_surface.set_colorkey(BLACK)
    pg.draw.circle(bomb_surface, RED, (10, 10), 10)

    # Set initial bomb position randomly
    bomb_rect = bomb_surface.get_rect()
    bomb_rect.x = random.randint(0, WIDTH - bomb_rect.width)
    bomb_rect.y = random.randint(0, HEIGHT - bomb_rect.height)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        
        # Blit bomb surface at its current position
        screen.blit(bomb_surface, bomb_rect)

        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
