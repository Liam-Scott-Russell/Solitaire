from unittest import TestCase
from MoveHelper import MoveHelper
from DTOs.GameState import GameState
from DTOs.Card import Card
from DTOs.Move import Move


class TestMoveHelperCheckMove(TestCase):
    def test_check_move_with_condition_1_and_items_in_deque(self):
        game = GameState(2)
        game.columns[0].cards.items = [Card(1), Card(2)]
        move = Move(0, 0)

        self.assertTrue(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_1_and_no_items_in_deque(self):
        game = GameState(2)
        move = Move(0, 0)

        self.assertFalse(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_2_and_valid_items_in_destination(self):
        game = GameState(4)
        game.columns[0].cards.items = [Card(1), Card(2)]
        game.columns[1].cards.items = [Card(4), Card(3)]
        move = Move(0, 1)

        self.assertTrue(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_2_and_invalid_items_in_destination(self):
        game = GameState(4)
        game.columns[0].cards.items = [Card(1), Card(2)]
        game.columns[1].cards.items = [Card(5), Card(4)]
        move = Move(0, 1)

        self.assertFalse(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_2_and_no_items_in_destination(self):
        game = GameState(2)
        game.setup_random_deck()
        move = Move(0, 1)

        self.assertTrue(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_2_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)
        move = Move(0, 1)

        self.assertFalse(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_3_and_valid_items_in_destination(self):
        game = GameState(14)  # large so that we generate the correct number of columns
        game.columns[1].cards.items = [Card(1), Card(2)]
        game.columns[2].cards.items = [Card(4), Card(3)]
        game.columns[3].cards.items = [Card(1), Card(2)]

        self.assertTrue(MoveHelper.check_move(game, Move(1, 2)))
        self.assertTrue(MoveHelper.check_move(game, Move(3, 2)))

    def test_check_move_with_condition_3_and_invalid_items_in_destination(self):
        game = GameState(4)
        game.columns[1].cards.items = [Card(1), Card(2)]
        game.columns[2].cards.items = [Card(3), Card(3)]
        move = Move(2, 1)

        self.assertFalse(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_3_and_no_items_in_destination(self):
        game = GameState(2)
        game.columns[1].cards.items = [Card(1), Card(2)]
        move = Move(1, 2)

        self.assertTrue(MoveHelper.check_move(game, move))

    def test_check_move_with_condition_3_and_no_items_in_destination_and_no_items_in_source(self):
        game = GameState(2)
        move = Move(2, 1)

        self.assertFalse(MoveHelper.check_move(game, move))

    def test_check_move_with_empty_column_0(self):
        # TODO: Consider whether this should be implemented
        game = GameState(2)
        game.columns[1].cards.items = [1]
        move = Move(1, 0)

        self.assertRaises(ValueError, MoveHelper.check_move, game, move)


class TestMoveHelperFormatMove(TestCase):
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


class TestMoveHelperDetermineMoveCondition(TestCase):
    def test_determine_move_condition_with_condition_1(self):
        move = Move(0, 0)
        actual_condition = MoveHelper.determine_move_condition(move)
        expected_condition = 1

        self.assertEqual(expected_condition, actual_condition)

    def test_determine_move_condition_with_condition_2(self):
        move = Move(0, 1)
        actual_condition = MoveHelper.determine_move_condition(move)
        expected_condition = 2

        self.assertEqual(expected_condition, actual_condition)

    def test_determine_move_condition_with_condition_3(self):
        move = Move(1, 2)
        actual_condition = MoveHelper.determine_move_condition(move)
        expected_condition = 3

        self.assertEqual(expected_condition, actual_condition)

    def test_determine_move_condition_with_invalid_move(self):
        move = Move(-1, 0)
        self.assertRaises(ValueError, MoveHelper.determine_move_condition, move)


class TestMoveHelperMakeMove(TestCase):
    def test_make_move_with_valid_condition_1(self):
        game = GameState(4)
        game.columns[0].cards.items = [4, 3, 2, 1]
        move = Move(0, 0)
        MoveHelper.make_move(game, move)

        actual_column = game.columns[0].cards.items
        expected_column = [1, 4, 3, 2]

        self.assertListEqual(expected_column, actual_column)

    def test_make_move_with_valid_condition_2_and_no_cards_in_destination(self):
        game = GameState(4)
        game.columns[0].cards.items = [4, 3, 2, 1]
        move = Move(0, 1)
        MoveHelper.make_move(game, move)

        actual_column_0 = game.columns[0].cards.items
        expected_column_0 = [4, 3, 2]

        actual_column_1 = game.columns[1].cards.items
        expected_column_1 = [1]

        self.assertListEqual(expected_column_0, actual_column_0)
        self.assertListEqual(expected_column_1, actual_column_1)

    def test_make_move_with_valid_condition_2_and_cards_in_destination(self):
        game = GameState(4)
        game.columns[0].cards.items = [4, 3, 1]
        game.columns[1].cards.items = [2]
        move = Move(0, 1)
        MoveHelper.make_move(game, move)

        actual_column_0 = game.columns[0].cards.items
        expected_column_0 = [4, 3]

        actual_column_1 = game.columns[1].cards.items
        expected_column_1 = [2, 1]

        self.assertListEqual(expected_column_0, actual_column_0)
        self.assertListEqual(expected_column_1, actual_column_1)

    def test_make_move_with_single_valid_condition_3_and_no_cards_in_destination(self):
        game = GameState(4)
        game.columns[1].cards.items = [4]
        move = Move(1, 2)
        MoveHelper.make_move(game, move)

        actual_column_1 = game.columns[1].cards.items
        expected_column_1 = []

        actual_column_2 = game.columns[2].cards.items
        expected_column_2 = [4]

        self.assertListEqual(expected_column_2, actual_column_2)
        self.assertListEqual(expected_column_1, actual_column_1)

    def test_make_move_with_single_valid_condition_3_and_cards_in_destination(self):
        game = GameState(2)
        game.columns[1].cards.items = [1]
        game.columns[2].cards.items = [2]
        move = Move(1, 2)
        MoveHelper.make_move(game, move)

        actual_column_1 = game.columns[1].cards.items
        expected_column_1 = []

        actual_column_2 = game.columns[2].cards.items
        expected_column_2 = [2, 1]

        self.assertListEqual(expected_column_1, actual_column_1)
        self.assertListEqual(expected_column_2, actual_column_2)

    def test_make_move_with_multiple_valid_condition_3_and_no_cards_in_destination(self):
        game = GameState(3)
        game.columns[1].cards.items = [3, 2, 1]
        game.columns[2].cards.items = []
        move = Move(1, 2)
        MoveHelper.make_move(game, move)

        actual_column_1 = game.columns[1].cards.items
        expected_column_1 = []

        actual_column_2 = game.columns[2].cards.items
        expected_column_2 = [3, 2, 1]

        self.assertListEqual(expected_column_1, actual_column_1)
        self.assertListEqual(expected_column_2, actual_column_2)

    def test_make_move_with_multiple_valid_condition_3_and_cards_in_destination(self):
        game = GameState(4)
        game.columns[1].cards.items = [3, 2, 1]
        game.columns[2].cards.items = [4]
        move = Move(1, 2)
        MoveHelper.make_move(game, move)

        actual_column_1 = game.columns[1].cards.items
        expected_column_1 = []

        actual_column_2 = game.columns[2].cards.items
        expected_column_2 = [4, 3, 2, 1]

        self.assertListEqual(expected_column_1, actual_column_1)
        self.assertListEqual(expected_column_2, actual_column_2)
