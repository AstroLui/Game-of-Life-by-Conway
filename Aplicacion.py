import pygame
import numpy as np
import time
from Widgets.Button import *
from Widgets.Text import *
from Widgets.ButtonImage import *

#Iniciamos Pygame
pygame.init()

#Screen de la Pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

#Name Window
pygame.display.set_caption('Game of Life')

#Font
font = pygame.font.Font('Fonts/Sixtyfour.TTF', 40)
font_other = pygame.font.Font('Fonts/Sixtyfour.TTF', 20)
font_widgets = pygame.font.Font('Fonts/Sixtyfour.TTF', 15)
font_textplano = pygame.font.Font('Fonts/8-BIT WONDER.TTF', 18)

#Funciones

#Widgets
    #Widgets de la Pantalla Principal
Button_Option = Button('Opciones', 250, 50, (260, 400), font_widgets, 6)
TitleCenter = Text('Juego de la Vida', font, '#000000', 75, 150)
SubTitle = Text('de Conway', font_other, '#000000', 90, 190)
StartText = Text('Presione SPACE para comenzar', font_other, '#000000', 110, 340)
    #Widgets de las Opciones
Button_Back = Button('Atras', 100, 50, (20, 20), font_widgets, 6)

#Game Variables
game_option = False
game_start = False
ncX, ncY = 50, 50
dimCW = SCREEN_WIDTH / ncX
dimCH = SCREEN_HEIGHT / ncY

#Game Loop
while running: 
    screen.fill('#DCDDD8')
    if Button_Option.pressed == True:
        Button_Back.draw(screen)
        if Button_Back.pressed == True: 
            Button_Option.pressed = False
            Button_Back.pressed = False
        pass
    elif game_start == True:
        for y in range(4, ncX-10):
            for x in range(2, ncY-2):

                poly = [((x)     * dimCW, y       * dimCH),  
                        ((x + 1) * dimCW, y       * dimCH), 
                        ((x + 1) * dimCW, (y + 1) * dimCH), 
                        ((x)     * dimCW, (y + 1) * dimCH)]
                
                pygame.draw.polygon(screen, "#000000", poly, 1)
        
        pass
    else:
        TitleCenter.Draw(screen)
        SubTitle.Draw(screen)
        StartText.Draw(screen)
        Button_Option.draw(screen)
    
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = True

    pygame.display.update()
    

pygame.quit()