import pygame as pg #so we can use "pg." instead of typing out "pygame." everytime 

pg.init()

background_color = pg.Color('green') #in rgb would be background_color = (234, 212, 252)

screen = pg.display.set_mode((500,500)) #window is 500 by 500
pg.display.set_caption('WindowGoBrr')

screen.fill(background_color)

running = True

while running:
    
# for loop through the event queue  
    for event in pg.event.get():
      
        # Check for QUIT event      
        if event.type == pg.QUIT:
            running = False

    pg.display.flip() #update screen all the time

pg.quit()
