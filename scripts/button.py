import pygame

from scripts.text import Text


class Button:

    def __init__(self, color, x, y, rect_width, rect_height, call_back):
        self.window = pygame.display.get_surface()
        self.color = color
        self.rect = pygame.Rect(x, y, rect_width, rect_height)

        self.call_back = call_back

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.color ## aqui você pode alterar a cor quando o mouse estiver em cima do botão
            else:
                self.color = self.color ## aqui ele retorna à cor original

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == 1 and self.rect.collidepoint(event.pos):
                self.call_back()

class ButtonWithText(Button):
    def __init__(self, color, x, y, rect_width, rect_height, call_back, font, text_size, text, text_color, text_position, new_text_color):
        super().__init__(color, x, y, rect_width, rect_height, call_back)

        self.text = text
        self.text_color = text_color
        self.text_position = text_position
        self.new_text_color = new_text_color

        self.render = Text(font, text_size, self.text, self.text_color, self.text_position)

    def draw(self):
        super().draw()
        self.render.draw()

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.color ## aqui você pode alterar a cor quando o mouse estiver em cima do botão
                self.render.update_text(self.text, self.new_text_color)
            else:
                self.color = self.color ## aqui ele retorna à cor original
                self.render.update_text(self.text, self.text_color)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == 1 and self.rect.collidepoint(event.pos):
                self.call_back()
