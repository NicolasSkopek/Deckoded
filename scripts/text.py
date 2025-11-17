import pygame

class Text:
    def __init__(self, font, size, text, color, pos, max_width=750):
        self.window = pygame.display.get_surface()
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.position = pos
        self.max_width = max_width
        self.update_text(text)

        self.text_str = text
        self.text = self.font.render(self.text_str, True, self.color)
        self.text_rect = self.text.get_rect(center=pos)

    def update_text(self, text, color=None):
        if color:
            self.color = color
        self.lines = []

        if self.max_width:
            words = text.split(' ')
            current_line = ''
            for word in words:
                test_line = current_line + (' ' if current_line else '') + word
                if self.font.size(test_line)[0] <= self.max_width:
                    current_line = test_line
                else:
                    self.lines.append(current_line)
                    current_line = word
            if current_line:
                self.lines.append(current_line)
        else:
            self.lines = [text]

        self.rendered_lines = [self.font.render(line, True, self.color) for line in self.lines]

    def draw(self):
        x, y = self.position
        for i, line in enumerate(self.rendered_lines):
            line_rect = line.get_rect(center=(x, y + i * self.font.get_linesize()))
            self.window.blit(line, line_rect)

    def draw_center(self):
        self.draw()
