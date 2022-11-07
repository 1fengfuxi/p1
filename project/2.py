import pygame
import random
import math
pygame.init()
running=True
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption(" plane game")
icon=pygame.image.load("space.jpg")
pygame.display.set_icon(icon)
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(1)
bg=pygame.image.load("space.jpg")
player=pygame.image.load("test.png ")
playerx=400
playery=500
player_step=0
player_stepy=0

number_of_enemies= 6

class clsss_Eneymy():
    def __init__(self):
        self.eneymy_image= pygame.image.load("eneymy image.png")
        self.x= random.randint(100,800)
        self.y= random.randint(50,300)
        self.eneymy_step= random.uniform(0.01 ,0.2)
    def reset(self):
        self.x=random.randint(100,800)
        self.y=random.randint(50,300)

enemies=[]
for i in range(number_of_enemies):
    enemies.append(clsss_Eneymy())


def show_eneymy():
    for e in enemies:
        screen.blit(e.eneymy_image, (e.x, e.y))
        e.x += e.eneymy_step
        if e.x > 710 or e.x < 0:
            e.eneymy_step *=-1
            e.y += 20



class Bullet () :
    def __init__(self):
        self.image = pygame.image.load("bullets .png")
        self.x = playerx
        self.y = playery-10
        self.step = 0.2

    def hit(self):
         for e in enemies:
             if distance(self.x , self.y, e.x, e.y)<30:
                bullets.remove(self)
                e.reset()




bullets=[]


def show_bullets():
    for b in bullets:
        screen.blit(b.image, (b.ages, b.y))
        b.hit()
        b.y-= b.step
        if b.y <0 :
            bullets.remove(b)

def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a*a+ b*b)


def setborder_and_dispaly():# add player step to cordniate
    global playerx
    global playery
    screen.blit(bg, (0, 0))
    screen.blit(player, (playerx, playery))
    playerx += player_step
    playery += player_stepy
    if playerx > 761:
        playerx = 761
    elif playerx < 0:
        playerx = 0
    elif playery> 525:
        playery=525
    elif playery<0:
        playery=0

def show_eneymy():
    for e in enemies:
        screen.blit(e.eneymy_image, (e.x, e.y))
        e.x += e.eneymy_step
        if e.x > 710 or e.x < 0:
            e.eneymy_step *=-1
            e.y += 20

def process_event():
    global player_stepy
    global player_step
    global running
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                player_step=0.1
            elif event.key==pygame.K_LEFT:
                player_step=-0.1
            elif event.key==pygame.K_DOWN:
                player_stepy=0.1
            elif event.key==pygame.K_UP:
                player_stepy=-0.1
            elif event.key== pygame.K_SPACE:
                bullets.append(Bullet())

        if event.type==pygame.KEYUP:
            player_step=0
            player_stepy=0

while running:
    process_event()
    setborder_and_dispaly()
    show_eneymy()
    show_bullets()
    pygame.display.update()




