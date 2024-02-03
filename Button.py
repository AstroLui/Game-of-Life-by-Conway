import pygame

class Button():
    def __init__(self, text, width, height, pos, font, elevation):
        #Core Attribute
        self.pressed = False
        self.evelation = elevation
        self.dinamyc_elevation = elevation
        self.original_pos = pos[1]

        #top rectagular
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#FFFFFF'

        #bottom rectangular
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = '#606060'

        #Text
        self.text_surf = font.render(text, True, '#000000')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
    
    def draw(self, screen): 
        #Elevacion
        self.top_rect.y = self.original_pos - self.dinamyc_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dinamyc_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius= 12 )
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius= 12 )
        screen.blit(self.text_surf, self.text_rect)
        self.checked_click()

    def checked_click(self):
        moused_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(moused_pos):
            self.top_color = '#C6C6C6'
            if pygame.mouse.get_pressed()[0]:
                self.dinamyc_elevation = 0
                self.pressed = True
            else:
                self.dinamyc_elevation = self.evelation
                if self.pressed == True: 
                    print('Click')
                    self.pressed = False
        else:
            self.dinamyc_elevation = self.evelation
            self.top_color = 'white'