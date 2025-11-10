import pygame
import random

from scripts.obj import Obj, Card
from scripts.scene import Scene
from scripts.settings import WIDTH
from scripts.database import Database
from scripts.text import Text

pygame.mixer.init()
pygame.font.init()

class Game(Scene):
    def __init__(self, player_name="Player1"):
        super().__init__()

        self.all_sprites = pygame.sprite.Group()

        self.player = player_name

        self.bg = Obj("assets/scenario/bg1.jpg", [0, -300], self.all_sprites)
        self.table = Obj("assets/scenario/table.png", [WIDTH/2 - (640/2), 270], self.all_sprites)

        self.wood_table = Obj("assets/scenario/woodtable.png", [WIDTH/2-90, -60], self.all_sprites)

        self.card1 = Card("assets/cards/card1.png", [300, 550], "card1", reveal_offset=(-60, -100), all_sprites=self.all_sprites)
        self.card2 = Card("assets/cards/card2.png", [350, 550], "card2", reveal_offset=(0, -100), all_sprites=self.all_sprites)
        self.card3 = Card("assets/cards/card3.png", [400, 550], "card3", reveal_offset=(60, -100), all_sprites=self.all_sprites)

        self.cards = [self.card1, self.card2, self.card3]

        self.score = 0
        self.round = 0

        self.problems = [
            {"text": "O problema da parada: determinar se uma TM para em uma entrada específica", "answer": "card1"},# indecidível
            {"text": "Verificar se uma TM aceita alguma palavra do seu alfabeto", "answer": "card2"},  # semidecidível
            {"text": "Determinar se uma palavra pertence a uma linguagem regular", "answer": "card3"},  # decidível
            {"text": "Verificar se duas TM aceitam a mesma linguagem", "answer": "card1"},  # indecidível
            {"text": "Verificar se uma gramática livre de contexto gera a palavra vazia", "answer": "card3"},# decidível
            {"text": "Verificar se uma TM aceita infinitas palavras", "answer": "card2"},  # semidecidível
            {"text": "Determinar se duas expressões regulares representam a mesma linguagem", "answer": "card3"},# decidível
            {"text": "Determinar se uma TM nunca para em nenhuma entrada", "answer": "card1"},  # indecidível
            {"text": "Verificar se uma linguagem descrita por uma gramática livre de contexto é vazia", "answer": "card3"},  # decidível
            {"text": "Determinar se um autômato finito não-determinístico aceita alguma palavra específica", "answer": "card3"},  # decidível
        ]

        self.current_problem = None

        self.round_text = Text("assets/fonts/ARIAL.ttf", 30, "", (255, 255, 255), [WIDTH//2, 70])
        self.problem_text = Text("assets/fonts/ARIAL.ttf", 24, "", (255, 255, 255), [WIDTH//2, 200])
        self.score_text = Text("assets/fonts/ARIAL.ttf", 30, str(self.score), (0, 0, 255), [50, 50])

        self.next_round()

    def game_over(self):
        if self.round == 11:
            db = Database()
            db.salvar_resultado(self.player, self.score)
            self.active = False

    def next_round(self):
        self.round += 1
        self.current_problem = random.choice(self.problems)
        self.round_text.update_text(f"Round {self.round}")
        self.problem_text.update_text(self.current_problem["text"])

    def check_answer(self, chosen_card):
        if chosen_card.type == self.current_problem["answer"]:
            self.score += 1
        self.score_text.update_text(str(self.score))
        self.next_round()

    def update(self):
        self.game_over()
        mouse_pos = pygame.mouse.get_pos()
        for card in self.cards:
            card.update(mouse_pos)

    def events(self, event):
        for card in self.cards:
            if card.events(event):
                self.check_answer(card)

    def card_clicked(self, card, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if card.rect.collidepoint(event.pos):
                return True
        return False

    def draw(self):
        self.all_sprites.draw(self.window)
        self.round_text.draw_center()
        self.problem_text.draw_center()
        self.score_text.draw_center()
