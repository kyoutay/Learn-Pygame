import os
import sys
import pygame as pg
import random

pg.init()

x = 500
y = 500
velocity = 12

screen = pg.display.set_mode((1000,1000)) #becomes a surface object
pg.display.set_caption('Project2')

clock = pg.time.Clock()

def load_img(name):
    filePath = os.path.join(sys.path[0], name)
    image = pg.image.load(filePath)
    return image

characterSprites = [load_img('sprite1.png'),
                    load_img('sprite2.png'),
                    load_img('sprite3.png'),
                    load_img('sprite4.png'),
                    load_img('sprite5.png'),
                    load_img('sprite6.png')]

filePath = os.path.join(sys.path[0], 'bunnyCrunch.wav')
crunchSound = pg.mixer.Sound(filePath)

sprite = 0
character = characterSprites[sprite]


bg_img = load_img('farmBckgr.png') #1000x1000, the same size as your window
carrot = load_img('carrot.png') #50x50, as long as it's small

characterBox = character.get_rect()
carrotBox = carrot.get_rect()
carrotBox.center = (800,300)

carrotsEaten = 0
font = pg.font.Font(None, 50)
carrotsEatenText = font.render('Carrots Eaten: ' + str(carrotsEaten), True, pg.Color('black')) # this carrot render can be deleted since the one in the loop is constantly being updated anyways

running = True
while running:

    clock.tick(10) #10 frames per second

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT] or pressed[pg.K_LEFT] or pressed[pg.K_UP] or pressed[pg.K_DOWN]:
        sprite += 1
        if sprite >= len(characterSprites):
            sprite = 0
        character = characterSprites[sprite]
        if pressed[pg.K_RIGHT]:
            x += velocity
        if pressed [pg.K_LEFT]:
            x -= velocity
            character = pg.transform.flip(character, True, False)
        if pressed [pg.K_UP]:
            y -= velocity
        if pressed [pg.K_DOWN]:
            y += velocity
        
        
    characterBox.center = (x,y)
    screen.blit(bg_img,(0,0)) 
    screen.blit(carrot, carrotBox) #we only need to change the location of the carrotBox cos the carrot image is blitted to wherever the carrotBox is
    screen.blit(character, characterBox) 

    carrotsEatenText = font.render('Carrots Eaten: ' + str(carrotsEaten), True, pg.Color('black'))
    screen.blit(carrotsEatenText, (50,950)) #score in the bottom left corner

    pg.draw.rect(screen,pg.Color('red'),characterBox,1)

    if characterBox.colliderect(carrotBox):
        carrotsEaten += 1
        crunchSound.play()
        carrotBox.center = (random.randint(0,1000),random.randint(0,1000)) #random.randint(0,1000) returns a random number between 0 and 1000. 0 and 1000 since 1000x1000 is the size of our window and we want the carrot to respawn somewhere in our window
        #not relocating carrot would make the score continuously go up while the bunny is still touching it

    pg.display.update()
    
pg.quit()
