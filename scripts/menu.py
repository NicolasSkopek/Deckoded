import sys
import pygame

from scripts.scene import Scene
from scripts.obj import Obj

class Menu(Scene):

    def __init__(self):
        super().__init__()


    def next_scene(self):
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

