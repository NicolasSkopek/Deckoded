import pygame
from scripts.text import Text
from scripts.settings import SECONDARY_COLOR

class Button:
    def __init__(self, x, y, text, call_back, color, cursor=None):
        self.window = pygame.display.get_surface()
        self.text = text
        self.call_back = call_back
        self.color = color
        self.cursor = cursor

        self.hovered = False
        self.hover_sound = pygame.mixer.Sound("assets/sounds/hoversound.mp3")

        self.render = Text("assets/fonts/VINERITC.ttf", 40, self.text, self.color, (x, y))

    def draw(self):
        self.render.draw_center()

    def events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        hovering = self.render.text_rect.collidepoint(mouse_pos)

        if event.type == pygame.MOUSEMOTION:
            if hovering:
                if not self.hovered:
                    self.hover_sound.play()
                    self.hovered = True
                    if self.cursor:
                        self.cursor.set_image("assets/cursor/cursor2.png")
                self.render.update_text(self.text, SECONDARY_COLOR)
            else:
                if self.hovered:
                    self.hovered = False
                    self.render.update_text(self.text, self.color)
                    if self.cursor:
                        self.cursor.reset_image()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and hovering:
                self.call_back()
