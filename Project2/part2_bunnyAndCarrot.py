import os
import sys
import pygame as pg

pg.init()

x = 500
y = 500
velocity = 12

screen = pg.display.set_mode((1000,1000)) #becomes a surface object
pg.display.set_caption('Project2')

def load_img(name):
    filePath = os.path.join(sys.path[0], name)
    image = pg.image.load(filePath)
    return image

character = load_img('sprite1.png')
bg_img = load_img('farmBckgr.png') #1000x1000, the same size as your window
carrot = load_img('carrot.png') #50x50, as long as it's small

characterBox = character.get_rect() #get_rect() creates a rectangle of the image's size
carrotBox = carrot.get_rect() 
carrotBox.center = (800,300)

running = True
while running:
  
    for event in pg.event.get():
  
        if event.type == pg.QUIT:
            running = False
  
        if event.type == pg.KEYDOWN:
  
            if event.key == pg.K_LEFT: #the K_LEFT and such are pygame constants, in the documentation
                x -= velocity
  
            if event.key == pg.K_RIGHT:
                x += velocity
  
            if event.key == pg.K_UP:
                y -= velocity

            if event.key == pg.K_DOWN:
                y += velocity
            
    characterBox.center = (x,y) #using characterBox.move_ip(x,y) instead would make the bunny instantly disappear from the screen because it's moving so fast, since (x,y) is being added to the current location in a loop rather than changing the location to (x,y)
    screen.blit(bg_img,(0,0)) 
    screen.blit(carrot, carrotBox) #If the carrot is blitted before the bg_img, then we wouldn't see the image since it would be under bg_img
    screen.blit(character, characterBox) #changing the box's location alone doesn't change the image's location, we have to blit the image to where the box is

    pg.draw.rect(screen,pg.Color('red'),characterBox,1)

    if characterBox.colliderect(carrotBox):
        pg.quit()

    pg.display.update()
    
pg.quit()
