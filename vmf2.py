import pygame
import time

pygame.init()
win=pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Fight with Vofimort")

x=50
y=50
width =58
height = 105
speed = 4
lastMove = "right"
block=pygame.image.load("blok_1.png")

BLOCK_WIDTH = 59
BLOCK_HEIGHT = 59
walkRight=[pygame.image.load("personag_p1.png"),pygame.image.load("personag_p2.png")]
walkLeft=[pygame.image.load("personag_l1.png"),pygame.image.load("personag_l2.png")]
walk=[]
left=False
right=False
animCount=0
k=0

clock=pygame.time.Clock()
class snaryad():
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 10 * facing
    def draw(self,win):
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.radius)
def drawwindow():
    global k
    global animCount
    level = [
            "-------------------------------------------",
            "-                -                        -",
            "-                -                        -",
            "-                -                        -",
            "-                -                        -",
            "-                -          ------        -",
            "-------          -                        -",
            "-                -                        -",
            "-                -  -------               -",
            "-                -                        -",
            "-     -----                               -",
            "-                                         -",
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
    win.fill((0, 255, 255))
    a = b = 0  
    for row in level:  
        for col in row: 
            if col == "-":
                pf = block
                win.blit(pf, (a, b))
            a += BLOCK_WIDTH  
        b += BLOCK_HEIGHT  
        a = 0
    if animCount+1>=60:
        animCount=0
    if left:
        win.blit(walkLeft[animCount//30],(x,y))
        animCount +=1
        k=1
    elif right:
        win.blit(walkRight[animCount // 30],(x,y))
        animCount +=1
        k=2
    else:
        if k==0 or k==2:
            win.blit(pygame.image.load("personag_p1.png"), (x, y))
        else:
            win.blit(pygame.image.load("personag_l1.png"), (x, y))
    #win.blit(Hero, (x, y))
    for bullet in bullets:
        bullet.draw(win)


    pygame.display.update()
run = True
bullets=[]
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    for bullet in bullets:
        if bullet.x<1366 and bullet.x>0:
            bullet.x += bullet.vel

        else:
            bullets.pop(bullets.index(bullet))
    pressed= pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    if pressed[0]:
        pygame.time.delay(80)
        if lastMove == "right":
            facing=1
        else:
            facing=-1
        if len(bullets)<10:
            bullets.append(snaryad(round(x+width//2),round(y+height//2),10,(255,0,0),facing))

    if keys[pygame.K_a] and x>5:
        x-=speed
        left=True
        right=False
        lastMove="left"
    elif keys[pygame.K_d] and x<1366-width-5:
        x+=speed
        left=False
        right=True
        lastMove="right"
    else:
        left=False
        right=False
        animCount=0
    if keys[pygame.K_w] and y>5:
        y-=speed
    if keys[pygame.K_s] and y<768-height-5:
        y+=speed

    drawwindow()
