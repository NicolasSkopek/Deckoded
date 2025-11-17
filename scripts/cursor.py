import pygame

class Cursor:
    def __init__(self, image_path, size=(46, 46), hotspot=None):
        self.size = size
        self.default_image_path = image_path
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.default_image = self.image.copy()

        if hotspot is None:
            self.hotspot = (size[0] // 2, size[1] // 2)
        else:
            self.hotspot = hotspot

        pygame.mouse.set_visible(False)

    def set_image(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

    def reset_image(self):
        self.image = self.default_image.copy()

    def draw(self, surface):
        mx, my = pygame.mouse.get_pos()
        surface.blit(self.image, (mx - self.hotspot[0], my - self.hotspot[1]))
