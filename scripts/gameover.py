import pygame
from scripts.button import Button
from scripts.scene import Scene
from scripts.database import Database
from scripts.text import Text
from scripts.cursor import Cursor
from scripts.settings import *

class GameOver(Scene):
    def __init__(self):
        super().__init__()
        self.db = Database()

        self.text = Text("assets/fonts/ARIAL.ttf", 40, "RESULTADO", (255,0,0), [WIDTH//2, 200])
        self.btn_return = Button(100,100,"return", self.next_scene, [255,255,255])

        resultados = self.db.listar_resultados(10)
        self.score_texts = []
        for i, (jogador, pontos, data) in enumerate(resultados):
            txt = Text("assets/fonts/ARIAL.ttf", 25, f"{i+1}. {jogador} — {pontos} pontos",
                       (255,255,255), [WIDTH//2, 300+i*30])
            self.score_texts.append(txt)

        self.cursor = Cursor("assets/cursor/cursor.png")


    def events(self, event):
        self.btn_return.events(event)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.btn_return.render.text_rect.collidepoint(mouse_pos):
            self.cursor.set_image("assets/cursor/cursor2.png")
        else:
            self.cursor.reset_image()

    def draw(self):
        self.text.draw_center()
        self.btn_return.draw()
        for txt in self.score_texts:
            txt.draw_center()
        self.cursor.draw(self.window)

    def next_scene(self):
        self.active = False
