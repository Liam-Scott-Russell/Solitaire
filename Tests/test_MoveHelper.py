from unittest import TestCase
from MoveHelper import MoveHelper
from DTOs.GameState import GameState
from DTOs.Card import Card
from DTOs.Move import Move


class TestMoveHelper(TestCase):
    def test_check_move_with_condition_1_and_items_in_deque(self):
        game = GameState(2)
        game.columns[0].items = [Card(1), Card(2)]
        move = Move(0, 0)

        self.assertTrue(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_1_and_no_items_in_deque(self):
        game = GameState(2)
        move = Move(0, 0)

        self.assertFalse(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_2_and_valid_items_in_destination(self):
        game = GameState(4)
        game.columns[0].items = [Card(1), Card(2)]
        game.columns[1].items = [Card(4), Card(3)]
        move = Move(0, 1)

        self.assertTrue(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_2_and_invalid_items_in_destination(self):
        game = GameState(4)
        game.columns[0].items = [Card(1), Card(2)]
        game.columns[1].items = [Card(5), Card(4)]
        move = Move(0, 1)

        self.assertFalse(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_2_and_no_items_in_destination(self):
        game = GameState(2)
        game.setup_random_deck()
        move = Move(0, 1)

        self.assertTrue(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_2_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)
        move = Move(0, 1)

        self.assertFalse(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_3_and_valid_items_in_destination(self):
        game = GameState(14) # large so that we generate the correct number of columns
        game.columns[1].items = [Card(1), Card(2)]
        game.columns[2].items = [Card(4), Card(3)]
        game.columns[3].items = [Card(1), Card(2)]

        self.assertTrue(MoveHelper.check_move(Move(1, 2), game))
        self.assertTrue(MoveHelper.check_move(Move(3, 2), game))

    def test_check_move_with_condition_3_and_invalid_items_in_destination(self):
        game = GameState(4)
        game.columns[1].items = [Card(1), Card(2)]
        game.columns[2].items = [Card(3), Card(3)]
        move = Move(2, 1)

        self.assertFalse(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_3_and_no_items_in_destination(self):
        game = GameState(2)
        game.columns[1].items = [Card(1), Card(2)]
        move = Move(1, 2)

        self.assertTrue(MoveHelper.check_move(move, game))

    def test_check_move_with_condition_3_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)
        move = Move(2, 1)

        self.assertFalse(MoveHelper.check_move(move, game))

    def test_check_move_with_empty_column_0(self):
        # TODO: Consider whether this should be implemented
        game = GameState(2)
        game.columns[1].items = [1]
        move = Move(1, 0)

        self.assertFalse(MoveHelper.check_move(move, game))

    def test_format_move_with_valid_string(self):
        test_move = "0,1"

        actual_move = MoveHelper.format_move(test_move)
        expected_move = Move(0, 1)

        self.assertEqual(expected_move.source_column, actual_move.source_column)
        self.assertEqual(expected_move.destination_column, actual_move.destination_column)

    def test_format_move_with_invalid_string(self):
        test_move1 = "I'm and invalid move"
        test_move2 = "a,b"

        self.assertRaises(ValueError, MoveHelper.format_move, test_move1)
        self.assertRaises(ValueError, MoveHelper.format_move, test_move2)

