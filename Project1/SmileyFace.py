
import pygame as pg

pg.init()

background_color = pg.Color('green')

screen = pg.display.set_mode((500,500)) #window is 500 by 500
pg.display.set_caption('WindowGoBrr')

screen.fill(background_color)

#draw face
pg.draw.circle(screen, pg.Color('white'), (250,250), 250) #face
pg.draw.circle(screen, pg.Color('black'), (150,150), 40) #left eye. y-coordinate is 150
pg.draw.circle(screen, pg.Color('black'), (350,150), 40) #right eye. y-coordinate is 150
pg.draw.arc(screen, pg.Color('black'), (150,200,200,200), 3.8, 5.6, 5) #smile

#add text
font = pg.font.Font(None, 64)
text = font.render("Have a Good Day!", True, pg.Color('blue')) #anti-aliasing is a boolean 
textRect = text.get_rect()
textRect.center = (screen.get_width()/2, 40)
screen.blit(text, textRect) #screen is a surface object


running = True
while running:
    
# for loop through the event queue  
    for event in pg.event.get():
      
        # Check for QUIT event      
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()
