from unittest import TestCase
from MoveHelper import MoveHelper
from GameState import GameState
from Card import Card


class TestMoveHelper(TestCase):
    def test_check_move_with_condition_1_and_items_in_deque(self):
        game = GameState(2)
        game.columns[0].items = [Card(1), Card(2)]

        self.assertTrue(MoveHelper.check_move(0, 0, game))

    def test_check_move_with_condition_1_and_no_items_in_deque(self):
        game = GameState(2)

        self.assertFalse(MoveHelper.check_move(0, 0, game))

    def test_check_move_with_condition_2_and_valid_items_in_destination(self):
        game = GameState(4)
        game.columns[0].items = [Card(1), Card(2)]
        game.columns[1].items = [Card(4), Card(3)]

        self.assertTrue(MoveHelper.check_move(0, 1, game))

    def test_check_move_with_condition_2_and_invalid_items_in_destination(self):
        game = GameState(4)
        game.columns[0].items = [Card(1), Card(2)]
        game.columns[1].items = [Card(5), Card(4)]

        self.assertFalse(MoveHelper.check_move(0, 1, game))

    def test_check_move_with_condition_2_and_no_items_in_destination(self):
        game = GameState(2)
        game.setup_random_deck()

        self.assertTrue(MoveHelper.check_move(0, 1, game))

    def test_check_move_with_condition_2_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)

        self.assertFalse(MoveHelper.check_move(0, 1, game))

    def test_check_move_with_condition_3_and_valid_items_in_destination(self):
        game = GameState(14) # large so that we generate the correct number of columns
        game.columns[1].items = [Card(1), Card(2)]
        game.columns[2].items = [Card(4), Card(3)]
        game.columns[3].items = [Card(1), Card(2)]

        self.assertTrue(MoveHelper.check_move(1, 2, game))
        self.assertTrue(MoveHelper.check_move(3, 2, game))

    def test_check_move_with_condition_3_and_invalid_items_in_destination(self):
        game = GameState(4)
        game.columns[1].items = [Card(1), Card(2)]
        game.columns[2].items = [Card(3), Card(3)]

        self.assertFalse(MoveHelper.check_move(2, 1, game))

    def test_check_move_with_condition_3_and_no_items_in_destination(self):
        game = GameState(2)
        game.columns[1].items = [Card(1), Card(2)]

        self.assertTrue(MoveHelper.check_move(1, 2, game))

    def test_check_move_with_condition_3_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)

        self.assertFalse(MoveHelper.check_move(2, 1, game))

    def test_check_move_with_empty_column_0(self):
        # TODO: Consider whether this should be implemented
        game = GameState(2)
        game.columns[1].items = [1]

        self.assertFalse(MoveHelper.check_move(1, 0, game))

    def test_format_move_with_valid_string(self):
        test_move = "0,1"

        actual_move = MoveHelper.format_move(test_move)
        expected_move = (0, 1)

        self.assertEqual(expected_move, actual_move)

    def test_format_move_with_invalid_string(self):
        test_move1 = "I'm and invalid move"
        test_move2 = "a,b"

        with self.assertRaises(ValueError):
            MoveHelper.format_move(test_move1)
            MoveHelper.format_move(test_move2)