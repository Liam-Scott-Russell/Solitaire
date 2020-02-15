from unittest import TestCase
from MoveChecker import *
from Deque import Deque
from GameState import GameState
from Card import Card


class TestMoveChecker(TestCase):
    def test_check_move_with_condition_1_and_items_in_deque(self):
        game = GameState(2)
        game.columns[0].items = [Card(1), Card(2)]

        self.assertTrue(MoveChecker.check_move(0, 0, game))

    def test_check_move_with_condition_1_and_no_items_in_deque(self):
        game = GameState(2)

        self.assertFalse(MoveChecker.check_move(0, 0, game))

    def test_check_move_with_condition_2_and_valid_items_in_destination(self):
        game = GameState(2)
        game.columns[0].items = [Card(1), Card(2)]
        game.columns[1].items = [Card(4), Card(3)]

        self.assertTrue(MoveChecker.check_move(0, 1, game))

    def test_check_move_with_condition_2_and_invalid_items_in_destination(self):
        game = GameState(2)
        game.columns[0].items = [Card(1), Card(2)]
        game.columns[1].items = [Card(5), Card(4)]

        self.assertFalse(MoveChecker.check_move(0, 1, game))

    def test_check_move_with_condition_2_and_no_items_in_destination(self):
        game = GameState(2)
        game.columns[0].items = [Card(1), Card(2)]

        self.assertTrue(MoveChecker.check_move(0, 1, game))

    def test_check_move_with_condition_2_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)

        self.assertFalse(MoveChecker.check_move(0, 1, game))
