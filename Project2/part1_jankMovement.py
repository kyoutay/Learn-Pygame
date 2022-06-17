import os
import sys
import pygame as pg

pg.init()

screen = pg.display.set_mode((1000,1000)) #becomes a surface object. If it was 1280x1280, center would be x=640,y=640
pg.display.set_caption('Project2')

filePath = os.path.join(sys.path[0], 'sprite1.png')
character = pg.image.load(filePath)

x = 500
y = 500
velocity = 12 #change to change how much the bunny moves by each press

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
  
            if event.key == pg.K_UP: #subtracting makes it go up since the top left corner of the window is (0,0) and bottom right corner would be the size of your window, (1000,1000)
                y -= velocity #So increasing y makes it go downwards and decreasing y goes upwards

            if event.key == pg.K_DOWN:
                y += velocity

    screen.fill(pg.Color('white')) #code for white is (255,255,255). you would do screen.fill((255,255,255))
    screen.blit(character, (x, y)) #we fill the background before the blit and inside the game loop since the previous screen isn't erased, we just cover up the previous sprite with a new background 

    pg.display.update()
    
pg.quit()
