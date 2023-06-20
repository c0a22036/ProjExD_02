import random
import pygame as pg

import sys

# 練習４
delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT: (+1, 0),
    }

# 練習５
def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool,bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数1：画面SuefaceのRect
    引数2：こうかとん、または、爆弾SurfaceのRect
    戻り値：横方向、縦方向のはみ出し判定結果（画面内：True/画面外：False）
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect() # 練習４
    kk_rct.center = 900, 400 # 練習４

    bb_img = pg.Surface((20,20)) # 練習１
    pg.draw.circle(bb_img,(255,0,0),(10,10),10) # 練習１
    bb_img.set_colorkey((0,0,0)) # 練習１
    x, y = random.randint(0,1600), random.randint(0,900) # 練習2
    vx, vy = +1, +1 # 練習３
    avx, avy = +1, +1  #追加機能2

    bb_rct = bb_img.get_rect() # 練習３
    bb_rct.center = x, y # 練習３
    
    accs = [ a for a in range(1, 11)] #加速度のリスト

    tmr = 0
    overtime = -1
    gameover = False

    kokaton = {
        (0, -1): pg.transform.rotate(pg.transform.flip(kk_img, False, False), -90),#上
        (+1, -1): pg.transform.rotate(pg.transform.flip(kk_img, False, False), -135),#
        (+1, 0): pg.transform.rotate(pg.transform.flip(kk_img, False, True), -180),#右
        (+1, +1): pg.transform.rotate(pg.transform.flip(kk_img, False, False), -225),#
        (0, +1): pg.transform.rotate(pg.transform.flip(kk_img, False, False), -270),#下
        (-1, +1): pg.transform.rotate(pg.transform.flip(kk_img, False, False), -315),#
        (-1, 0): pg.transform.rotate(pg.transform.flip(kk_img, False, False), 0),#
        (-1, -1): pg.transform.rotate(pg.transform.flip(kk_img, False, False), -40),#
        }

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        avx, avy = vx*accs[min(tmr//1000, 9)], vy*accs[min(tmr//1000, 9)]  #追加機能2

        # 練習４
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
                kk_img = kokaton[mv]
        if check_bound(screen.get_rect(),kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)  #練習４
        bb_rct.move_ip(avx,avy) # 練習３&追加機能2
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko: # 横方法にはみ出ていたら
            vx *= -1
        if not tate: # 縦方向にはみ出ていたら
            vy *= -1
        screen.blit(bb_img, bb_rct) # 練習３
        
        if kk_rct.colliderect(bb_rct): #練習６
            kk_img = pg.image.load("ex02/fig/8.png")  #追加機能３
            kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)  #追加機能３
            gameover = True  #追加機能３
            overtime = tmr  #追加機能３

        if gameover == True:  #追加機能３
            if  tmr - overtime > 200:  #追加機能３ 
                return  #追加機能３

        pg.display.update()
        clock.tick(1000)

def start():#スタート時にkkを跳ねさせる

    pg.display.set_caption("逃げろ！こうかとん")
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1600, 900))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/9.png")
    kk_img = pg.transform.rotozoom(kk_img, -10, 3.0)
    kk10_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img,kk10_img]
    tmr = 0

    while True:
        tmr += 1
        if tmr%100 <= 50:
            a = 1
        else:
            a = 0
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_imgs[a], [700 ,300])
        if tmr == 500:
            return 0
        
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__": 
    pg.init()
    start()
    main()
    pg.quit()
    sys.exit()