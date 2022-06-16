import os
import sys
import pygame as pg

pg.init()

background_color = pg.Color('green')

screen = pg.display.set_mode((500,500)) #window is 500 by 500
pg.display.set_caption('WindowGoBrr')

screen.fill(background_color)

pg.draw.circle(screen, pg.Color('white'), (250,250), 250)
pg.draw.circle(screen, pg.Color('black'), (150,150), 40)
pg.draw.circle(screen, pg.Color('black'), (350,150), 40)
pg.draw.arc(screen, pg.Color('black'), (150,200,200,200), 3.8, 5.6, 5)

font = pg.font.Font(None, 64)
text = font.render("Have a Good Day!", True, pg.Color('blue'))
textRect = text.get_rect()
textRect.center = (screen.get_width()/2, 40)
screen.blit(text, textRect)

buttonFont = pg.font.Font(None, 80)
buttonText = buttonFont.render('Press Me', True, pg.Color('white'))
buttonRect = buttonText.get_rect()
buttonRect.center = (screen.get_width()/2, 300)
pg.draw.rect(screen,pg.Color('gray'),buttonRect)

filePath = os.path.join(sys.path[0], 'punch.wav')
sound = pg.mixer.Sound(filePath)

running = True
while running: #things are inside the game loop if we need to constantly check it, update it, refresh it, etc. Otherwise, if we need to do it only once it goes outside the loop(above it)
    mouse = pg.mouse.get_pos()

# for loop through the event queue. the event queue loop  
    for event in pg.event.get():
      
        # Check for QUIT event      
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN: #don't need to release mouse for click to register
            if buttonRect.collidepoint(mouse):
                sound.play()

    if buttonRect.collidepoint(mouse):
        pg.draw.rect(screen,pg.Color('black'), buttonRect)
    else:
        pg.draw.rect(screen,pg.Color('gray'), buttonRect)

    screen.blit(buttonText, buttonRect) #we blit the text on after since the if we do it before, the rectangle goes on top of the text and the text is hidden.
    pg.display.update()

pg.quit()
