import pygame
import numpy as np
import time
from Widgets.Button import *
from Widgets.Text import *
from Widgets.ButtonToggle import *

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
Button_Back = Button('Atras', 100, 50, (20, 20), font_widgets, 6,)
Text_ColorCell = Text('Cambiar Color de la Celula', font_textplano, '#000000', 30, 100)
Text_Figura = Text('Cambiar Figura', font_textplano, '#000000', 30, 250)
Button_Classic = ButtonToggle('Clásico', 125, 50, (50, 150), font_widgets, 6, False)
Button_Red = ButtonToggle('Rojo', 125, 50, (190, 150), font_widgets, 6, False)
Button_Azul = ButtonToggle('Azul', 125, 50, (330, 150), font_widgets, 6, False)
Button_Verde = ButtonToggle('Verde', 125, 50, (470, 150), font_widgets, 6, False)
Button_FigClassic = ButtonToggle('Básico', 125, 50, (50, 300), font_widgets, 6, False)
Button_FigParpadeo = ButtonToggle('Parpadeo', 140, 50, (185, 300), font_widgets, 6, False)
Button_Planeador = ButtonToggle('Planeador', 160, 50, (335, 300), font_widgets, 6, False)
Button_Reina = ButtonToggle('Reina', 125, 50, (505, 300), font_widgets, 6, False)
Button_Bellota = ButtonToggle('Bellota', 125, 50, (645, 300), font_widgets, 6, False)
    #Widgets de Inicio del Juego
Button_Exit = Button('Atras', 100, 50, (20, 520), font_widgets, 6,)
Button_Paused = Button('Pausar', 125, 50, (315, 520), font_widgets, 6,)


def texto():
     if game_paused:
        return Button('Continuar', 150, 50, (315, 520), font_widgets, 6,)
     else:
         return Button('Pausar', 125, 50, (315, 520), font_widgets, 6,)

def Colors():
    if game_classic:
        return '#000000'
    elif game_red:
        return "#f20c0c"
    elif game_azul:
        return '#5754A8'
    elif game_verde:
        return '#A5CC1B'
    else:
        return '#000000'

def Figuras():
    if figura_base:
        gameState[21, 21] = 1
        gameState[22, 22] = 1
        gameState[22, 23] = 1
        gameState[21, 23] = 1
        gameState[20, 23] = 1
    if figura_parpadeo:
        gameState[21, 21] = 1
        gameState[22, 21] = 1
        gameState[23, 21] = 1
    if figura_planeador:
        gameState[20, 21] = 1
        gameState[20, 22] = 1
        gameState[21, 22] = 1
        gameState[22, 22] = 1
        gameState[22, 23] = 1
    if figura_reina:
        gameState[2, 1] = 1
        gameState[2, 2] = 1
        gameState[3, 0] = 1
        gameState[3, 1] = 1
        gameState[3, 2] = 1
        gameState[4, 0] = 1
        gameState[4, 2] = 1
        gameState[5, 1] = 1
        gameState[6, 0] = 1
        gameState[6, 2] = 1
        gameState[7, 1] = 1
        gameState[9, 0] = 1
        gameState[9, 3] = 1
        gameState[10, 0] = 1
        gameState[10, 2] = 1
        gameState[10, 3] = 1
        gameState[11, 1] = 1
        gameState[12, 0] = 1
        gameState[12, 2] = 1
        gameState[12, 3] = 1
        gameState[13, 1] = 1
        gameState[14, 0] = 1
        gameState[14, 2] = 1
        gameState[14, 3] = 1
        gameState[15, 1] = 1
        gameState[16, 1] = 1
    if figura_bellota:
        gameState[1, 0] = 1
        gameState[2, 0] = 1
        gameState[3, 1] = 1
        gameState[4, 0] = 1
        gameState[5, 0] = 1
        gameState[6, 1] = 1
    else:
        gameState[21, 21] = 1
        gameState[22, 22] = 1
        gameState[22, 23] = 1
        gameState[21, 23] = 1
        gameState[20, 23] = 1



#Game Variables
game_option = False
game_start = False
game_paused = False
    #Variables de Colores
game_classic = True
Button_Classic.Toggle = True
game_red = False
game_azul = False
game_verde = False
    #Variables de las formas
figura_base = True
Button_FigClassic.Toggle = True
figura_parpadeo = False
figura_planeador = False
figura_reina = False
figura_bellota = False
ncX, ncY = 80, 80
dimCW = SCREEN_WIDTH / ncX
dimCH = SCREEN_HEIGHT / ncY

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
            if Button_Classic.Click():
                game_classic = True
                game_red =  False
                game_azul = False
                game_verde = False
                Button_Red.Toggle = False
                Button_Azul.Toggle = False
                Button_Verde.Toggle = False
            if Button_Red.Click():
                game_red = True
                game_classic = False
                game_azul = False
                game_verde=  False
                Button_Classic.Toggle = False
                Button_Azul.Toggle = False
                Button_Verde.Toggle = False
            if Button_Azul.Click():
                game_red = False
                game_classic = False
                game_azul = True
                game_verde = False
                Button_Classic.Toggle = False
                Button_Verde.Toggle = False
                Button_Red.Toggle = False
            if Button_Verde.Click():
                game_red = False
                game_classic = False
                game_azul = False
                game_verde = True
                Button_Classic.Toggle = False
                Button_Azul.Toggle = False
                Button_Red.Toggle = False

            if Button_FigClassic.Click():
                figura_base = True
                figura_parpadeo = False
                figura_planeador = False
                figura_reina = False
                figura_bellota = False
                Button_FigParpadeo.Toggle = False
                Button_Planeador.Toggle = False
                Button_Reina.Toggle = False
                Button_Bellota.Toggle = False
            if Button_FigParpadeo.Click():
                figura_base = False
                figura_parpadeo = True
                figura_planeador = False
                figura_reina = False
                figura_bellota = False
                Button_FigClassic.Toggle = False
                Button_Planeador.Toggle = False
                Button_Reina.Toggle = False
                Button_Bellota.Toggle = False
            if Button_Planeador.Click():
                figura_base = False
                figura_parpadeo = False
                figura_planeador = True
                figura_reina = False
                figura_bellota = False
                Button_FigParpadeo.Toggle = False
                Button_FigClassic.Toggle = False
                Button_Reina.Toggle = False
                Button_Bellota.Toggle = False
            if Button_Reina.Click():
                figura_base = False
                figura_parpadeo = False
                figura_planeador = False
                figura_reina = True
                figura_bellota = False
                Button_FigParpadeo.Toggle = False
                Button_Planeador.Toggle = False
                Button_FigClassic.Toggle = False
                Button_Bellota.Toggle = False
            if Button_Bellota.Click():
                figura_base = False
                figura_parpadeo = False
                figura_planeador = False
                figura_reina = False
                figura_bellota = True
                Button_FigParpadeo.Toggle = False
                Button_Planeador.Toggle = False
                Button_Reina.Toggle = False
                Button_FigClassic.Toggle = False

    # Main Menu     
    if game_option == False and game_start == False:
        # Estados de la Celulas. Vivos = 1, Muertos = 0
        gameState = np.zeros((ncX, ncY))
        # Iniciamos algunas Celulas para probar su comportamiento
        Figuras()
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
        Text_ColorCell.Draw(screen)
        Text_Figura.Draw(screen)
        Button_Classic.draw(screen)
        Button_Back.draw(screen)
        Button_Red.draw(screen)
        Button_Azul.draw(screen)
        Button_Verde.draw(screen)
        Button_FigClassic.draw(screen)
        Button_FigParpadeo.draw(screen)
        Button_Planeador.draw(screen)
        Button_Reina.draw(screen)
        Button_Bellota.draw(screen)
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
                try: 
                    newGameState[celX, celY] = 1
                except(IndexError):
                    pass
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button_Exit.Click():
                    game_start = False
                    game_paused = False
                    Button_Paused = texto()
                if Button_Paused.Click():
                    if game_paused==False:
                        game_paused = True
                    elif game_paused:
                        game_paused = False
                    Button_Paused = texto()
            
            if event.type == pygame.QUIT:
                running = False
            
        # Bucle para escribir las celdas en pantalla
        for y in range(2, ncX-14):
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
                        if game_classic:
                            pygame.draw.polygon(screen, '#008F39', poly, 0)
                    #Regla 2: Una celda viva con menos de 2 o más de 3 celdas vivas alrededor muere.
                    elif gameState[x, y] == 1 and (n_Neigh < 2 or n_Neigh > 3): 
                        newGameState[x, y] = 0
                        if game_classic:
                            pygame.draw.polygon(screen, '#FF0000', poly, 0)
                # Creamos el poligono para dibujar la celda
                poly = [((x)     * dimCW, y       * dimCH),  
                        ((x + 1) * dimCW, y       * dimCH), 
                        ((x + 1) * dimCW, (y + 1) * dimCH), 
                        ((x)     * dimCW, (y + 1) * dimCH)]
                
                # Dibujamos la celda
                if newGameState[x, y] == 0:
                    Tcolor = Colors() 
                    pygame.draw.polygon(screen, '#606060', poly, 1)
                else:
                    pygame.draw.polygon(screen, Tcolor, poly, 0)
        
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