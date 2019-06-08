import pygame
import random
from time import sleep
pygame.init()
screenWidth = 700
screenHeight = 500
clock = pygame.time.Clock()
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Flappy clone')


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

    def draw(self, win):
        keys = pygame.key.get_pressed()
        if self.y < screenHeight - 50:
            self.y += self.vel
        if keys[pygame.K_SPACE] and self.y > 0:
            self.y -= self.vel * 2
        pygame.draw.rect(win, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))


class blocks(object):
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.width = 70
        self.height = height
        self.vel = 8

    def draw(self, win):
        self.x -= self.vel
        pygame.draw.rect(win, (0, 150, 0),
                         (self.x, self.y, self.width, self.height))


def redraw():
    aaa = 0

    win.fill((0, 0, 0))
    man.draw(win)

    for block in blocksArr:
        block.draw(win)
    for block in blocksArr:
        if block.x <= man.x + man.width:
            if block.y == 0:
                if block.height >= man.y:
                    aaa += 1
                    print('Top', str(aaa))
                    text = font.render(
                        'How fucking hard it is to press one button?', 1, (255, 255, 255))
                    win.blit(text, (0, screenHeight/2))
                    sleep(1)
            if block.y != 0:
                if block.height <= man.y:
                    aaa += 1
                    print('Bottom', str(aaa))
                    text = font.render(
                        'How fucking hard it is to press one button?', 1, (255, 255, 255))
                    win.blit(text, (0, screenHeight/2))
                    sleep(1)
    pygame.display.update()


# main loop
man = player(40, screenHeight / 2, 50, 50)
blocksArr = []
font = pygame.font.SysFont('comicsans', 30, True)
sometimer = random.choice([20, 30, 40, 50, 60])
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for block in blocksArr:
        if block.x <= 0:
            blocksArr.pop(blocksArr.index(block))
    sometimer -= 1
    if sometimer == 0:
        sometimer = random.choice([70, 90, 100])
        blockheights = [300, 250, 200]
        finalheight = random.choice(blockheights)
        blocky = [0, screenHeight - finalheight]
        finaly = random.choice(blocky)
        if len(blocksArr) < 5:
            blocksArr.append(blocks(800, finaly, finalheight))

    redraw()
pygame.quit()
# block.x <= man.x + man.width
#man.height <= block.height
