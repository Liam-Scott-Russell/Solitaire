from unittest import TestCase
from MoveChecker import *
from Deque import Deque
from GameState import GameState


class TestMoveChecker(TestCase):
    def test_check_move_with_condition_1_and_items_in_deque(self):
        game = GameState(2)
        game.columns[0].items = [1, 2]

        self.assertTrue(MoveChecker.check_move(0, 0, game))

    def test_check_move_with_condition_1_and_no_items_in_deque(self):
        game = GameState(2)

        self.assertFalse(MoveChecker.check_move(0, 0, game))
