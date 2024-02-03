import pygame

class Text():
    def __init__(self, text: str, font: pygame.font.FontType, text_color: str, x: int, y: int):
        self.Text = text
        self.Font = font
        self.Color = text_color
        self.Posx = x
        self.Posy = y

    def Draw(self, screen: pygame.SurfaceType):
        img = self.Font.render(self.Text, True, self.Color)
        screen.blit(img, (self.Posx, self.Posy))
    
