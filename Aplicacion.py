import pygame
import numpy as np
import time
from Widgets.Button import *
from Widgets.Text import *
from Widgets.ButtonImage import *

#Iniciacion de Pygame
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
font_copy = pygame.font.Font('Fonts/Pixelinter.ttf', 14)

#Widgets
    #Widgets de la Pantalla Principal
Button_Option = Button('Opciones', 250, 50, (260, 400), font_widgets, 6)
TitleCenter = Text('Juego de la Vida', font, '#000000', 75, 150)
SubTitle = Text('de Conway', font_other, '#000000', 90, 190)
StartText = Text('Presione SPACE para comenzar', font_other, '#000000', 110, 340)
CopyText = Text('Copyrights (C) 2024, Astrofamily. All Rights Reserveds', font_copy, '#000000', 415, 550)
CopyText_By = Text('By AstroLui and Moi', font_copy, '#000000', 650, 570)
    #Widgets de las Opciones
Button_Back = Button('Atras', 100, 50, (20, 20), font_widgets, 6)
    #Widgets de Inicio del Juego
Button_Exit = Button('Atras', 100, 50, (20, 520), font_widgets, 6)
Button_Paused = Button('Pausar', 125, 50, (315, 520), font_widgets, 6)
Button_Classic = Button('Clásico', 125, 50, (315, 520), font_widgets, 6)
#Game Variables
game_option = False
game_start = False
game_paused = False
game_classic = False
ncX, ncY = 50, 50
dimCW = SCREEN_WIDTH / ncX
dimCH = SCREEN_HEIGHT / ncY

def texto():
     if game_paused:
        return Button('Continuar', 150, 50, (315, 520), font_widgets, 6)
     else:
         return Button('Pausar', 125, 50, (315, 520), font_widgets, 6)
#Game Loop
while running: 
    # Color de Background
    screen.fill('#DCDDD8')
    # Event Handler
    # Bucle que escucha el evento de QUIT 
    # de la ventana y del SPACE para iniciar el juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Button_Option.Click():
                game_option = True
            if Button_Back.Click():
                game_option = False
    # Main Menu     
    if game_option == False and game_start == False:
        # Estados de la Celulas. Vivos = 1, Muertos = 0
        gameState = np.zeros((ncX, ncY))
        # Iniciamos algunas Celulas para probar su comportamiento
        gameState[21, 21] = 1
        gameState[22, 22] = 1
        gameState[22, 23] = 1
        gameState[21, 23] = 1
        gameState[20, 23] = 1
        # Copiamos gameState, esta lista es donde haremos
        # los cambios
        newGameState = np.copy(gameState)
        # Dibujamos los Widgets en pantalla
        TitleCenter.Draw(screen)
        SubTitle.Draw(screen)
        StartText.Draw(screen)
        Button_Option.draw(screen)
        CopyText.Draw(screen)
        CopyText_By.Draw(screen)
        pass

    # Menu Opciones
    if game_option == True:
        # Dibujamos el Boton de Atras en 
        # el menu de opciones
        Button_Classic.draw(screen)
        Button_Back.draw(screen)

        if Button_Classic.pressed:
            game_classic = True
        # Codicion para regresar al Main Menu
        pass

    # Juego
    if game_start == True:
        # Le damos un Delay
        time.sleep(0.045)
        # Dibujamos los botones para Pausar 
        # y salir
        Button_Paused.draw(screen)
        Button_Exit.draw(screen)
        # Condicion para salir al Main Menu
        # Bucle que escucha los eventos de click del 
        # mouse en la Pantalla
        for event in pygame.event.get():
            # Tupla para saber si presiona la pantalla
            mouseEvent = pygame.mouse.get_pressed()
            if sum(mouseEvent) > 0: 
                # Posicion de donde se dio click en la 
                # pantalla
                posX, posY = pygame.mouse.get_pos()
                # Determinamos la celdas
                celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH)) 
                # Cambiamos el estado de la cedula
                newGameState[celX, celY] = 1
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_Exit.Click():
                    game_start = False
                if Button_Paused.Click():
                    if game_paused==False:
                        game_paused = True
                    elif game_paused:
                        game_paused = False
                    Button_Paused = texto()
            
            if event.type == pygame.QUIT:
                running = False
            
        # Bucle para escribir las celdas en pantalla
        for y in range(2, ncX-10):
            for x in range(2, ncY-2):
                if not game_paused:
                    # Determinamos los vecinos cercanos de cada celda 
                    n_Neigh=gameState[(x - 1) % ncX, (y - 1) % ncY] + \
                            gameState[(x)     % ncX, (y - 1) % ncY] + \
                            gameState[(x + 1) % ncX, (y - 1) % ncY] + \
                            gameState[(x - 1) % ncX, (y)     % ncY] + \
                            gameState[(x + 1) % ncX, (y)     % ncY] + \
                            gameState[(x - 1) % ncX, (y + 1) % ncY] + \
                            gameState[(x)     % ncX, (y + 1) % ncY] + \
                            gameState[(x + 1) % ncX, (y + 1) % ncY] 

                    #Regla 1: Una celda muerta con exactamente 3 vecinas vivas, "revive"
                    if gameState[x, y] == 0 and n_Neigh == 3: 
                        newGameState[x, y] = 1
                    #Regla 2: Una celda viva con menos de 2 o más de 3 celdas vivas alrededor muere.
                    elif gameState[x, y] == 1 and (n_Neigh < 2 or n_Neigh > 3): 
                        newGameState[x, y] = 0
                # Creamos el poligono para dibujar la celda
                poly = [((x)     * dimCW, y       * dimCH),  
                        ((x + 1) * dimCW, y       * dimCH), 
                        ((x + 1) * dimCW, (y + 1) * dimCH), 
                        ((x)     * dimCW, (y + 1) * dimCH)]
                
                # Dibujamos la celda
                if newGameState[x, y] == 0: 
                    pygame.draw.polygon(screen, '#606060', poly, 1)
                else:
                    pygame.draw.polygon(screen, '#000000', poly, 0)
        
        # Al final de bucle actualizaremos el estado de todas 
        # las celdas al mismo tiempo
        gameState = np.copy(newGameState)
        pass


    #Actualizacion de Display
    pygame.display.update()
    
    #Limitacion de Fps
    clock.tick(60)

# Finalizamos el Pygame
pygame.quit()