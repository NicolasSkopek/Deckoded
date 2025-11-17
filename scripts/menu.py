import sys
import pygame
from scripts.button import Button
from scripts.scene import Scene
from scripts.obj import Obj
from scripts.cursor import Cursor

class Menu(Scene):
    def __init__(self):
        super().__init__()
        self.all_sprites = pygame.sprite.Group()

        pygame.mixer.stop()
        self.music = pygame.mixer.Sound("assets/sounds/darkfantasy.mp3")
        self.music.set_volume(0.2)
        self.music.play(-1)

        self.bg = Obj("assets/menu/layer_1.png", [0,0], self.all_sprites)
        self.bg_2 = Obj("assets/menu/layer_2.png", [0,0], self.all_sprites)
        self.bg_2_1 = Obj("assets/menu/layer_2.png", [800,0], self.all_sprites)
        self.title = Obj("assets/menu/title.png", [0,0], self.all_sprites)


        self.btn_play = Button(100, 250, "play", self.next_scene, [255,0,0])
        self.btn_quit = Button(100, 320, "quit", self.quit_game, [255,255,255])

        self.cursor = Cursor("assets/cursor/cursor.png")

    def next_scene(self):
        self.active = False

    def events(self, event):
        self.btn_play.events(event)
        self.btn_quit.events(event)

    def update(self):
        self.all_sprites.update()
        self.move_bg()
        self.btn_play.draw()
        self.btn_quit.draw()

    def draw(self):
        self.all_sprites.draw(self.window)
        self.btn_play.draw()
        self.btn_quit.draw()

        self.cursor.draw(self.window)

    def move_bg(self):
        self.bg_2.rect.x -= 1
        self.bg_2_1.rect.x -= 1
        if self.bg_2.rect.x <= -800:
            self.bg_2.rect.x = 0
        if self.bg_2_1.rect.x <= 0:
            self.bg_2_1.rect.x = 800

    def quit_game(self):
        pygame.quit()
        sys.exit()
