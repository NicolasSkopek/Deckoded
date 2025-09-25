import pygame

from scripts.obj import Obj, Card
from scripts.scene import Scene
from scripts.settings import WIDTH


class Game(Scene):
    def __init__(self):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj("assets/scenario/bg1.jpg", [0, -300], self.all_sprites)
        self.table = Obj("assets/scenario/table.png", [WIDTH/2 - (640/2), 270], self.all_sprites)

        self.card1 = Card("assets/cards/card1.png", [300, 550], "card1",reveal_offset=(-60, -100), all_sprites=self.all_sprites)
        self.card2 = Card("assets/cards/card2.png", [350, 550], "card2",reveal_offset=(0, -100), all_sprites=self.all_sprites)
        self.card3 = Card("assets/cards/card3.png", [400, 550], "card3",reveal_offset=(60, -100), all_sprites=self.all_sprites)

        self.cards = [self.card1, self.card2, self.card3]

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for card in self.cards:
            card.update(mouse_pos)

    def events(self, event):
        for card in self.cards:
            card.events(event)

    def draw(self):
        self.all_sprites.draw(self.window)