import sys
import pygame

from scripts.button import Button
from scripts.scene import Scene
from scripts.obj import Obj

class Menu(Scene):

    def __init__(self):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/menu/layer_1.png", [0,0], self.all_sprites)
        self.bg_2 = Obj("assets/menu/layer_2.png", [0, 0], self.all_sprites)
        self.bg_2_1 = Obj("assets/menu/layer_2.png", [800, 0], self.all_sprites)
        self.title  = Obj("assets/menu/title.png", [0, 0], self.all_sprites)

        self.btn_play = Button(100, 250, "play", self.next_scene, [255, 0, 0])
        self.btn_quit = Button(100, 300, "quit", self.quit_game, [255, 255, 255])

    def next_scene(self):
        self.active = False

    def events(self, event):
        self.btn_play.events(event)
        self.btn_quit.events(event)

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def move_bg(self):
        self.bg_2.rect.x -= 1
        self.bg_2_1.rect.x -= 1
        if self.bg_2.rect.x <= -800:
            self.bg_2.rect.x = 0
        if self.bg_2_1.rect.x <= 0:
            self.bg_2_1.rect.x = 800

    def update(self):
        self.all_sprites.update()
        self.move_bg()
        self.btn_play.draw()
        self.btn_quit.draw()

    def quit_game(self):
        pygame.quit()
        sys.exit()

