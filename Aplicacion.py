import pygame
from Button import *

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

#Funciones
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

#Widgets
Button_Option = Button('Opciones', 250, 50, (260, 400), font_widgets)

#Game Variables
game_option = False
game_start = False

#Game Loop
while running: 
    screen.fill('#DCDDD8')
    if Button_Option.pressed == True:
        pass
    elif game_start == True:
        pass
    else:
        draw_text("Juego de la Vida",font, '#000000', 75, 150)
        draw_text("de Conway", font_other, '#000000', 90, 190)
        draw_text('Presione SPACE para comenzar', font_other, '#000000', 110, 340)
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