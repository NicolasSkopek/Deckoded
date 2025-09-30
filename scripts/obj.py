import pygame

class Obj(pygame.sprite.Sprite):

    def __init__(self, img, pos, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.frame = 0
        self.tick = 0

    def animation(self, speed, frames, path, file_type):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame += 1
            if self.frame > frames - 1:
                self.frame = 0
            self.image = pygame.image.load(path + str(self.frame) + "." + file_type)

class Card(Obj):
    def __init__(self, image, pos, type, reveal_offset=(0, -100), all_sprites=None):
        super().__init__(image, pos, all_sprites)

        self.type = type
        self.hovered = False
        self.speed = 6.5

        self.hover_sound = pygame.mixer.Sound("assets/sounds/hoversound.mp3")

        self.original_pos = pygame.Vector2(pos)
        self.reveal_pos = pygame.Vector2(pos[0] + reveal_offset[0],
                                         pos[1] + reveal_offset[1])

        self.images = {
            "normal": pygame.image.load(f"assets/cards/{type}.png"),
            "hover": pygame.image.load(f"assets/cards/{type}s.png")
        }
        self.image = self.images["normal"]

    def events(self, event):
        clicked = False

        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                if not self.hovered:
                    self.hovered = True
                    self.hover_sound.play()
                    self.image = self.images["hover"]
            else:
                if self.hovered:
                    self.hovered = False
                    self.image = self.images["normal"]

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                clicked = True

        return clicked

    def update(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        if 600 > mouse_x > 200 and mouse_y > 450:
            target = self.reveal_pos
        else:
            target = self.original_pos

        current = pygame.Vector2(self.rect.topleft)
        direction = (target - current)

        if direction.length() > self.speed:
            direction = direction.normalize() * self.speed

        self.rect.topleft = current + direction
