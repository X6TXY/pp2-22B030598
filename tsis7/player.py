import time
import pygame as pg
pg.init()

despacitoPath = "/Users/bahauddin/Coding/pp2-22B030598/tsis7/Despacito.mp3"
mozzartPath = "/Users/bahauddin/Coding/pp2-22B030598/tsis7/m1.mp3"
boomPath = "/Users/bahauddin/Coding/pp2-22B030598/tsis7/mot.mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("ЭМ ПЕ ТРИ ПЛЕЙЕР")
clock = pg.time.Clock()
mozzart = pg.mixer.music.load(mozzartPath)
boom = pg.mixer.music.load(boomPath)
despacito = pg.mixer.music.load(despacitoPath)
musicList = [despacitoPath, mozzartPath, boomPath]
pg.mixer.music.play(-1)
monkey = pg.image.load("/Users/bahauddin/Coding/pp2-22B030598/tsis7/monkey.jpeg")

sc.blit(monkey, (0, 0))
flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)
