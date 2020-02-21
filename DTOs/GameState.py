from .Column import Column
from .Card import Card
import random


class GameState:
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.number_of_cols = (self.number_of_cards // 8) + 3
        self.current_turn_number = 0
        self.max_turn_number = 2 * self.number_of_cards
        self.columns = [Column() for i in range(self.number_of_cols)]

    def setup_random_deck(self):
        deck = [Card(i) for i in range(self.number_of_cards)]
        random.shuffle(deck)
        self.columns[0].cards.items = deck
