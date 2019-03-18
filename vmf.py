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
        x = y = 0  
        for row in level:  
            for col in row:  
                if col == "-":
                    
                    pf = block
                    
                    win.blit(pf, (x, y))
                x += BLOCK_WIDTH 
            y += BLOCK_HEIGHT 
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
        win.blit(Hero, (a, b))
        pygame.display.update()

#pygame.quit()
