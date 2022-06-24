#credits to: https://github.com/PSpeiser/cookieclicker for the cookie logic and shop class

import os
import sys
import pygame as pg
import random #for the random ant spawning we'll add later

class shop: #only ant and shop are classes since we need multiple ants and multiple shop items. Classes serve as cookie cutters or blueprints to make a lot of these same objects
    def __init__(self, rect, text, base_price, base_cps_each):
        self.rect = rect
        self.text = text
        self.level = 0
        self.base_price = base_price
        self.cps_each = base_cps_each

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color('gray'), self.rect ,0) # button background color
        text_surface = font.render('Level: ' + str(self.level) + ' ' + self.text + ' $' + str(int(self.price())), True, pg.Color('black'))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left +10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface,text_rect)
            

    def total_cps(self):
        return self.cps_each * self.level

    def price(self):
        return self.base_price * 1.15**self.level

    def click(self):
        price = self.price()
        global COOKIES
        if COOKIES >= price:
            lvlUpSnd.play()
            self.level += 1
            COOKIES -= price
    
    def collidepoint(self,point):
        return self.rect.collidepoint(point)

    
class Ant(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self) #calling sprite initializer 
        self.image = antImg
        self.originalimage = self.image
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.direction = random.randint(1,4)
        if self.direction == 1: #downwards
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.Xspeed = 0
            self.Yspeed = random.randrange(1, 8)
            self.image = pg.transform.rotate(self.originalimage, 180)
        elif self.direction == 2: #upwards
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(HEIGHT, HEIGHT+60)
            self.Xspeed = 0
            self.Yspeed = -random.randrange(1, 8)
            self.image = self.originalimage
        elif self.direction == 3: #right
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.Xspeed = random.randrange(1, 8)
            self.Yspeed = 0
            self.image = pg.transform.rotate(self.originalimage, -90) #If I want my ant to face right, I can do -90 or 270 degrees
        elif self.direction == 4: #left
            self.rect.x = random.randrange(WIDTH, WIDTH+60)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.Xspeed = -random.randrange(1, 8)
            self.Yspeed = 0
            self.image = pg.transform.rotate(self.originalimage, 90)

    def mouseCollision(self,mouse):
        if self.rect.collidepoint(mouse):
            squishSnd.play()
            self.kill() #part of the sprite class

    def cookieCollision(self):
        global HEALTHPOINTS
        if circleRectCollision(500,500,280,self.rect.left,self.rect.top,self.rect.width,self.rect.height):
            crunchSnd.play()
            self.kill()
            HEALTHPOINTS -= 5

    def update(self):
        self.rect.x += self.Xspeed #keep the ant's rect up with the ant 
        self.rect.y += self.Yspeed

        if self.direction == 1: #if the ant is facing downwards and crosses the border by 10 pixels, then spawn the dude again using self.spawn()
            if self.rect.top > HEIGHT + 10:
                self.spawn()
        elif self.direction == 2: #same but upwards
            if self.rect.bottom < -10:
                self.spawn()
        elif self.direction == 3: # right
            if self.rect.left > WIDTH + 10:
                self.spawn()
        elif self.direction == 4: #left
            if self.rect.right < -10:
                self.spawn()

pg.init()

WIDTH = 1000 #all caps is a global variable
HEIGHT = 1000
COOKIES = 0 
HEALTHPOINTS = 100

screen = pg.display.set_mode((WIDTH,HEIGHT)) #becomes a surface object
pg.display.set_caption('Project3')

def circleRectCollision(cx,cy,cr,rx,ry,rw,rh): #circle's x,y,radius and rectangle's x,y,width,height
    circleDistX = abs(cx-rx)
    circleDistY = abs(cy-ry)

    if circleDistX > (rw/2 + cr) or circleDistY > (rh/2 + cr): return False
    if circleDistX <= rw/2 or circleDistY <= rh/2: return True

    cornerDist_sq = (circleDistX - rw/2)**2 + (circleDistY - rh/2)**2

    return cornerDist_sq <= (cr**2)

def load_img(name):
    filePath = os.path.join(sys.path[0], name)
    image = pg.image.load(filePath)
    return image

def load_sound(name):
    filePath = os.path.join(sys.path[0], name)
    sound = pg.mixer.Sound(filePath)
    return sound



cookieImg = load_img('cookie.png')
antImg = pg.transform.scale(load_img('ant.png'), (40,40)) #the actual image is too large, so we scale it down to 40x40
bckgrImg = load_img('floor.jpg')
shopImg = load_img('shop.png')

squishSnd = load_sound('squish.wav')
tapSnd = load_sound('cookieTap.wav')
shopSnd = load_sound('shop.wav')
lvlUpSnd = load_sound('levelUp.wav')
crunchSnd = load_sound('crunch.wav')
startSnd = load_sound('COOKIE.wav')


running = True
while running:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:

    pg.display.update()

pg.quit()
