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

#Widgets
    #Widgets de la Pantalla Principal
Button_Option = Button('Opciones', 250, 50, (260, 400), font_widgets, 6)
TitleCenter = Text('Juego de la Vida', font, '#000000', 75, 150)
SubTitle = Text('de Conway', font_other, '#000000', 90, 190)
StartText = Text('Presione SPACE para comenzar', font_other, '#000000', 110, 340)
    #Widgets de las Opciones
Button_Back = Button('Atras', 100, 50, (20, 20), font_widgets, 6)
    #Widgets de Inicio del Juego
Button_Exit = Button('Atras', 100, 50, (20, 520), font_widgets, 6)
Button_Paused = Button('Pausar', 125, 50, (315, 520), font_widgets, 6)
#Game Variables
game_option = False
game_start = False
game_paused = False
ncX, ncY = 50, 50
dimCW = SCREEN_WIDTH / ncX
dimCH = SCREEN_HEIGHT / ncY
gameState = np.zeros((ncX, ncY))
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#Game Loop
while running: 
    newGameState = np.copy(gameState)
    screen.fill('#DCDDD8')

    if Button_Option.pressed == True:
        Button_Back.draw(screen)
        if Button_Back.pressed == True: 
            Button_Option.pressed = False
            Button_Back.pressed = False
        pass
    elif game_start == True:
        time.sleep(0.045)
        
        Button_Paused.draw(screen)
        Button_Exit.draw(screen)
        if Button_Exit.checked_click() == True:
            game_start = False

        for event in pygame.event.get():
            mouseEvent = pygame.mouse.get_pressed()
            if sum(mouseEvent) > 0: 
                posX, posY = pygame.mouse.get_pos()
                celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH)) 
                newGameState[celX, celY] = 1
          
        for y in range(2, ncX-10):
            for x in range(2, ncY-2):
                if not game_paused: 
                    n_Neigh=gameState[(x - 1) % ncX, (y - 1) % ncY] + \
                            gameState[(x)     % ncX, (y - 1) % ncY] + \
                            gameState[(x + 1) % ncX, (y - 1) % ncY] + \
                            gameState[(x - 1) % ncX, (y)     % ncY] + \
                            gameState[(x + 1) % ncX, (y)     % ncY] + \
                            gameState[(x - 1) % ncX, (y + 1) % ncY] + \
                            gameState[(x)     % ncX, (y + 1) % ncY] + \
                            gameState[(x + 1) % ncX, (y + 1) % ncY] 

                    #Regla 1
                    if gameState[x, y] == 0 and n_Neigh == 3: 
                        newGameState[x, y] = 1
                    #Regla 2
                    elif gameState[x, y] == 1 and (n_Neigh < 2 or n_Neigh > 3): 
                        newGameState[x, y] = 0

                poly = [((x)     * dimCW, y       * dimCH),  
                        ((x + 1) * dimCW, y       * dimCH), 
                        ((x + 1) * dimCW, (y + 1) * dimCH), 
                        ((x)     * dimCW, (y + 1) * dimCH)]
                
                if newGameState[x, y] == 0: 
                    pygame.draw.polygon(screen, '#606060', poly, 1)
                else:
                    pygame.draw.polygon(screen, '#000000', poly, 0)
                
        gameState = np.copy(newGameState)
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
    clock.tick(60)
    
pygame.quit()