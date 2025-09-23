import pygame

from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import WIDTH


class Game(Scene):

    def __init__(self):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/bg1.jpg", [0, -300], self.all_sprites)
        self.table = Obj("assets/table.png", [WIDTH/2 - (640/2), 250], self.all_sprites)


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.all_sprites.draw(self.window)