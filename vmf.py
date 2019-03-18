import pygame
import time

pygame.init()
win=pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Fight with Vofimort")

a=50
b=50
width =58
height = 105
speed=5
block=pygame.image.load("blok_1.png")
Hero=pygame.image.load("personag.png")
BLOCK_WIDTH = 59
BLOCK_HEIGHT = 59

level = [
        "-------------------------------------------",
        "-                -                        -",
        "-                -                        -",
        "-                -                        -",
        "-            --  -                        -",
        "-                -          ------        -",
        "-----            -                        -",
        "-                -                        -",
        "-                -  -------               -",
        "-                -                        -",
        "-      ---                               -",
        "-                                        -",
        "-                -                        -",
        "-   -----------  -                   ------",
        "-                -       -------          -",
        "-              ---                        -",
        "-                   --                    -",
        "-                                         -",
        "-                                         -",
        "-                      -------------      -",
        "-                                         -",
        "-  -------------                          -",
        "-                                         -",
        "-------------------------------------------"]

run = True
while run:
        win.fill((255, 255, 255))
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    pf = block
                    # pf.fill(Color(PLATFORM_COLOR))
                    win.blit(pf, (x, y))
                x += BLOCK_WIDTH  # блоки платформы ставятся на ширине блоков
            y += BLOCK_HEIGHT  # то же самое и с высотой
            x = 0
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and a>5:
            a-=speed
        if keys[pygame.K_d] and a<1366-width-5:
            a+=speed
        if keys[pygame.K_w] and b>5:
            b-=speed
        if keys[pygame.K_s] and b<768-height-5:
            b+=speed
        #win.fill((0,0,0))
        #pygame.draw.rect(win,(0,215,0), (a,b,width,height))
        win.blit(Hero, (a, b))
        pygame.display.update()

#pygame.quit()
