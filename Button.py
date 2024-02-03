import pygame

class Button():
    def __init__(self, text, width, height, pos, font):
        #Core Attribute
        self.pressed = False

        #top rectagular
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = 'white'

        #Text
        self.text_surf = font.render(text, True, '#000000')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
    
    def draw(self, screen): 
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius= 12)
        screen.blit(self.text_surf, self.text_rect)
        self.checked_click()

    def checked_click(self):
        moused_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(moused_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True: 
                    print('Click')
                    self.pressed = False