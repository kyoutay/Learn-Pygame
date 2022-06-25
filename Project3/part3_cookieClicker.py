import os
import sys
import pygame as pg
import random #for the random ant spawning we'll add later

class shop:
    def __init__(self, rect, text, base_price, base_cps_each):
        self.rect = rect
        self.text = text
        self.level = 0
        self.base_price = base_price
        self.cps_each = base_cps_each

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color('gray'), self.rect) # button background color
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
            self.image = pg.transform.rotate(self.originalimage, -90)
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
            newAnt() #spawn new ant once one dies

    def cookieCollision(self):
        global HEALTHPOINTS
        if circleRectCollision(500,500,280,self.rect.left,self.rect.top,self.rect.width,self.rect.height):
            crunchSnd.play()
            self.kill()
            newAnt()
            HEALTHPOINTS -= 5

    def update(self):
        self.rect.x += self.Xspeed #keep the ant's rect up with the ant 
        self.rect.y += self.Yspeed

        if self.direction == 1:
            if self.rect.top > HEIGHT + 10:
                self.spawn()
        elif self.direction == 2:
            if self.rect.bottom < -10:
                self.spawn()
        elif self.direction == 3:
            if self.rect.left > WIDTH + 10:
                self.spawn()
        elif self.direction == 4:
            if self.rect.right < -10:
                self.spawn()




pg.init()

WIDTH = 1000 #all caps is a global variable
HEIGHT = 1000
COOKIES = 0 
HEALTHPOINTS = 100
CPS = 0.0
FPS = 30
HIDDEN = True #the new variable
CURSORAMT = 1
HIGHSCORE = 0
fpsClock = pg.time.Clock() #create our clock variable
font = pg.font.Font(None, 24) #font variable we'll use for the texts in the game

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

def make_items(text_list, base_price_list, cps_list, rect, spacing):
    button_height = rect.height / len(text_list)
    button_width = rect.width
    buttons = []
    for i in range(len(text_list)):
        text = text_list[i]
        base_price = base_price_list[i]
        base_cps = cps_list[i]
        button_rect = pg.Rect(rect.left, rect.top + i * (button_height + spacing), button_width, button_height)
        button = shop(button_rect, text, base_price, base_cps)
        buttons.append(button)
    return buttons

def click_cookie():
    global COOKIES
    COOKIES += CURSORAMT

def calculate_cps():
    global CPS
    global CURSORAMT
    cps = 0.0
    CURSORAMT = items[0].level ** 1.15 + 1 #if you look at our items list, you'll see the first element is the cursor
    for item in items: 
        cps += item.total_cps()
    CPS = cps

def update_cookies():
    global COOKIES
    global HIGHSCORE
    COOKIES += CPS / FPS
    if COOKIES > HIGHSCORE:
        HIGHSCORE = COOKIES

def hiding(): #we draw the shop items onto the screen here. Only if HIDDEN is false do we do this
    global HIDDEN
    if not HIDDEN:
        for button in items:
            button.draw(screen)

def changeHiding():
    global HIDDEN
    HIDDEN = not HIDDEN

def newAnt():
    a = Ant()
    ants.add(a)

def start_screen():
    screen.blit(bckgrImg,(0,0))
    font = pg.font.Font(None, 64)
    text_surface = font.render('COOKIE',True, pg.Color('white'))
    text_rect = text_surface.get_rect()
    text_rect.center = WIDTH/2, HEIGHT/4
    screen.blit(text_surface,text_rect)

    text2_surface = font.render('Press Any Key to Start', True, pg.Color('white'))
    text2_rect = text2_surface.get_rect()
    text2_rect.center = WIDTH/2, HEIGHT/2
    screen.blit(text2_surface,text2_rect)

    pg.display.update()

    waiting = True
    while waiting:
        fpsClock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                startSnd.play()
                waiting = False


items = make_items(["Cursor", "Grandma", "Farm", "Factory", "Mine", "Shipment", "Alchemy Lab", "Portal",
                    "Time machine", "Antimatter condenser", "Prism"],
                   [15, 100, 500, 3000, 10000, 40000, 200000, 1666666, 123456789, 3999999999, 75000000000],
                   [0, 0.5, 4, 10, 40, 100, 400, 6666, 98765, 999999, 10000000],
                   pg.Rect(700, 25, 230, 400), 5)

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

cookie_rect = cookieImg.get_rect()
cookie_rect.center = (500,500)
shopImg_rect = shopImg.get_rect()
shopImg_rect.topleft = (750,750)


game_over = True
running = True
while running:

    fpsClock.tick(FPS) 
    mouse_pos = pg.mouse.get_pos()
    x,y = mouse_pos #need the x and y separate for our cookie circle clicking

    if game_over:
        start_screen()
        game_over = False
        HEALTHPOINTS = 100
        ants = pg.sprite.Group()#ants sprite group created here in the game_over if statement. ants is essentially a list to control our ant objects of the ant class
        for i in range(8): #spawn 8 ants
            newAnt()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if shopImg_rect.collidepoint(mouse_pos):
                shopSnd.play()
                changeHiding()
            for button in items:
                if not HIDDEN and button.collidepoint(mouse_pos):
                    button.click() #belongs to the shop class. When a shop item is clicked on, that item's level goes up and its cost is subtracted from COOKIES
                    break
            if(pow(x-500,2) + pow(y-500,2)) <= pow(280,2): #clicking the cookie
                tapSnd.play() 
                cookie_rect.move_ip(5,5) #a little move effect when clicked on
                click_cookie()
            for ant in ants:
                ant.mouseCollision(mouse_pos)

        if event.type == pg.MOUSEBUTTONUP:
            if(pow(x-500,2) + pow(y-500,2)) <= pow(280,2):
                cookie_rect.move_ip(-5,-5)

    for ant in ants: # to manipulate objects of a class in our program, we loop through their list(our shop items) or sprite group(our ants)
        ant.cookieCollision()

    if HEALTHPOINTS == 0:
        COOKIES = 0
        CPS = 0
        for button in items:
            button.level = 0
        game_over = True


    screen.blit(bckgrImg,(0,0))
    screen.blit(cookieImg, cookie_rect)
    screen.blit(shopImg, shopImg_rect)
    #pg.draw.circle(screen, pg.Color('red'),(500,500),280,1)
    
    #draw cookies count
    text_surface = font.render(str(int(COOKIES)) + "+" + str(CPS) + "CPS", True, pg.Color('white'))
    text_rect = text_surface.get_rect()
    text_rect.center = (500, 100)
    screen.blit(text_surface, text_rect)

    ants.update()
    ants.draw(screen)
    hiding()
    calculate_cps()
    update_cookies()

    pg.display.update()

pg.quit()
