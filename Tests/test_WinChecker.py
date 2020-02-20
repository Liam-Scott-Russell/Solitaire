from unittest import TestCase
from WinChecker import WinChecker
from DTOs.GameState import GameState

class TestWinChecker(TestCase):
    def test_check_if_won_with_cards_in_first_column(self):
        game = GameState(4)
        game.columns[0].items = [0, 1]

        self.assertFalse(WinChecker.check_if_won(game))

    def test_check_if_won_without_cards_in_first_column(self):
        game = GameState(4)
        game.columns[1].items = [3, 2, 1]

        self.assertTrue(WinChecker.check_if_won(game))

    def test_check_if_won_with_card_in_two_columns(self):
        game = GameState(4)
        game.columns[1].items = [3, 2, 1]
        game.columns[2].items = [5, 4]
        self.assertFalse(WinChecker.check_if_won(game))
