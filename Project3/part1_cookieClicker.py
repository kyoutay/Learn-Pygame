import os
import sys
import pygame as pg
from pygame.locals import *
import random

class shop:
    def __init__(self, rect, text, base_price, base_cps_each):
        self.rect = rect
        self.text = text
        self.count = 0
        self.base_price = base_price
        self.cps_each = base_cps_each
        self.hidden = True
    
    def shopIcon(self, surface):
        surface.blit(shopImg,(800,800))

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color('gray'), self.rect,0) # button background color
        text_surface = font.render('Level: ' + str(self.count) + ' ' + self.text + ' $' + str(int(self.price())), False, pg.Color('black'))
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left +10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface,text_rect)

    def total_cps(self):
        return self.cps_each * self.count

    def price(self):
        return self.base_price * 1.15**self.count

    def click(self):
        price = self.price()
        global COOKIES
        if COOKIES >= price:
            self.count += 1
            COOKIES -= price
    
    def collidepoint(self,point):
        return self.rect.collidepoint(point)

class Ants(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        #self.image = antImg



pg.init()

screen = pg.display.set_mode((1000,1000)) #becomes a surface object
pg.display.set_caption('Project3')

COOKIES = 0
CPS = 0.0
FPS = 30
fpsClock = pg.time.Clock()
antSpeed = 10
font = pg.font.Font(None, 24)


def load_img(name):
    filePath = os.path.join(sys.path[0], name)
    image = pg.image.load(filePath)
    return image

def load_sound(name):
    filePath = os.path.join(sys.path[0], name)
    sound = pg.mixer.Sound(filePath)
    return sound

def make_items(text_list, base_price_list, cps_list, rect, spacing):
    button_height = rect.height / len(text_list)
    button_width = rect.width
    buttons = []
    for i in range(len(text_list)):
        text = text_list[i]
        base_price = base_price_list[i]
        base_cps = cps_list[i]
        button_rect = Rect(rect.left, rect.top + i * (button_height + spacing), button_width, button_height)
        button = shop(button_rect, text, base_price, base_cps)
        buttons.append(button)
    return buttons

def click_cookie():
    global COOKIES
    COOKIES += 1

def calculate_cps():
    global CPS
    cps = 0.0
    for item in items:
        cps += item.total_cps()
    CPS = cps

def update_cookies():
    global COOKIES
    COOKIES += CPS / FPS

items = make_items(["Cursor", "Grandma", "Farm", "Factory", "Mine", "Shipment", "Alchemy Lab", "Portal",
                    "Time machine", "Antimatter condenser", "Prism"],
                   [15, 100, 500, 3000, 10000, 40000, 200000, 1666666, 123456789, 3999999999, 75000000000],
                   [0.1, 0.5, 4, 10, 40, 100, 400, 6666, 98765, 999999, 10000000],
                   Rect(400, 25, 230, 400), 5)

cookieImg = load_img('cookie.png')
#antImg = load_img('ant.png')
bckgrImg = load_img('floor.jpg')
shopImg = load_img('shop.png')
#squishSnd = load_sound('bugSquish.mp3')
tapSnd = load_sound('tap.wav')

cookie_rect = Rect(25, 250, cookieImg.get_width(), cookieImg.get_height())





running = True
while running:

    screen.blit(bckgrImg,(0,0))
    screen.blit(cookieImg, cookie_rect)

    #draw cookies count
    text_surface = font.render(str(int(COOKIES)) + "+" + str(CPS) + "CPS", False, pg.Color('white'))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (100, 200)
    screen.blit(text_surface, text_rect)

    for button in items:
        button.draw(screen)

    calculate_cps()
    update_cookies()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_button = event.button
            if mouse_button == 1:
                for button in items:
                    if button.collidepoint(mouse_pos):
                        button.click()
                        break
                if cookie_rect.collidepoint(mouse_pos):
                    click_cookie()


    pg.display.update()
    fpsClock.tick(FPS) 

pg.quit()
