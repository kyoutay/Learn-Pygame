import os
import sys
import pygame as pg

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

sprite = 0
character = characterSprites[sprite] #characterSprites[3] is sprite4.png, since the first element is at 0, second is at 1, etc.


bg_img = load_img('farmBckgr.png') #1000x1000, the same size as your window
carrot = load_img('carrot.png') #50x50, as long as it's small

characterBox = character.get_rect()
carrotBox = carrot.get_rect()
carrotBox.center = (800,300)

running = True
while running:

    clock.tick(10) #10 frames per second. Change the 10 to a larger number, it'll increase how many times the loop runs per second. Practically, how fast the bunny moves. Recall velocity is how much the bunny moves by

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    pressed = pg.key.get_pressed() #so we don't have to type out pg.key.get_pressed() everytime and can just type pressed
    if pressed[pg.K_RIGHT] or pressed[pg.K_LEFT] or pressed[pg.K_UP] or pressed[pg.K_DOWN]:
        sprite += 1 #switches to the next sprite
        if sprite >= len(characterSprites): #checks if we've reached the end of the list, and then reset to the front
            sprite = 0
        character = characterSprites[sprite]
        if pressed[pg.K_RIGHT]:
            x += velocity
        if pressed [pg.K_LEFT]:
            x -= velocity
            character = pg.transform.flip(character, True, False) #only flip when going to left because the images are already facing right
        if pressed [pg.K_UP]:
            y -= velocity
        if pressed [pg.K_DOWN]:
            y += velocity
        
        
    characterBox.center = (x,y)
    screen.blit(bg_img,(0,0)) 
    screen.blit(carrot, carrotBox) #replaced (800,300) with carrotBox
    screen.blit(character, characterBox) #replaced (x,y) with characterBox

    pg.draw.rect(screen,pg.Color('red'),characterBox,1)

    if characterBox.colliderect(carrotBox):
        pg.quit()

    pg.display.update()
    
pg.quit()
