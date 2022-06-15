import pygame as pg

pg.init()

background_color = pg.Color('green')

screen = pg.display.set_mode((500,500)) #window is 500 by 500
pg.display.set_caption('WindowGoBrr')

screen.fill(background_color)


pg.display.flip()


running = True

while running:
    
# for loop through the event queue  
    for event in pg.event.get():
      
        # Check for QUIT event      
        if event.type == pg.QUIT:
            running = False

    pg.display.flip()

pg.quit()
