from unittest import TestCase
from ScreenHelper import ScreenHelper
from DTOs.Screen import Screen
from DTOs.Card import Card
from DTOs.Column import Column
from DTOs.GameState import GameState


class TestScreenHelperDrawLine(TestCase):
    def test_draw_line_horizontally_with_valid_coordinates(self):
        """
        A test that a horizontal line can be drawn
        """
        screen = Screen(3, 3)

        ScreenHelper.draw_line(screen, 0, 0, 0, 1, "#")

        expected_screen = Screen(3, 3)
        expected_screen.set_point(0, 0, "#")
        expected_screen.set_point(0, 1, "#")

        self.assertListEqual(screen.get_matrix(), expected_screen.get_matrix())

    def test_draw_line_horizontally_with_invalid_coordinates(self):
        """
        A test that a horizontal line won't be drawn for invalid coordinates
        """
        screen = Screen(2, 2)

        self.assertRaises(IndexError, ScreenHelper.draw_line, screen, 0, 0, 3, 0, "#")

        self.assertListEqual(screen.get_matrix(), Screen(2, 2).get_matrix())

    def test_draw_line_vertically_with_valid_coordinates(self):
        """
        A test that a vertical line can be drawn
        """
        screen = Screen(4, 4)

        ScreenHelper.draw_line(screen, 1, 0, 2, 0, "#")

        expected_screen = Screen(4, 4)
        expected_screen.set_point(1, 0, "#")
        expected_screen.set_point(2, 0, "#")

        self.assertListEqual(screen.get_matrix(), expected_screen.get_matrix())

    def test_draw_line_vertical_with_invalid_coordinates(self):
        """
        A test that a vertical line won't be drawn for invalid coordinates
        """
        screen = Screen(2, 2)

        self.assertRaises(IndexError, ScreenHelper.draw_line, screen, 0, 0, 0, 3, "#")

        self.assertListEqual(screen.get_matrix(), Screen(2, 2).get_matrix())

    def test_draw_line_diagonally_with_valid_coordinates(self):
        """
        A test that a diagonal line can be drawn
        """
        screen = Screen(4, 4)

        ScreenHelper.draw_line(screen, 1, 1, 2, 2, "#")

        expected_screen = Screen(4, 4)
        expected_screen.set_point(1, 1, "#")
        expected_screen.set_point(2, 2, "#")

        self.assertListEqual(screen.get_matrix(), expected_screen.get_matrix())

    def test_draw_line_diagonally_with_invalid_coordinates(self):
        """
        A test that a diagonal line won't be drawn for invalid coordinates
        """
        screen = Screen(2, 2)

        self.assertRaises(IndexError, ScreenHelper.draw_line, screen, 0, 0, 0, 3, "#")

        self.assertListEqual(screen.get_matrix(), Screen(2, 2).get_matrix())


class TestScreenHelperDrawCard(TestCase):
    def test_draw_card_with_valid_coordinates(self):
        screen = Screen(6, 5)
        card = Card(2)

        ScreenHelper.draw_card(screen, 0, 0, card)

        expected_matrix = [list(" ____ "),
                           list("|   2|"),
                           list("|    |"),
                           list("|    |"),
                           list("|____|")]

        self.assertListEqual(expected_matrix, screen.get_matrix())

    def test_draw_card_with_valid_coordinates_and_no_number(self):
        screen = Screen(6, 5)
        card = Card(2)

        ScreenHelper.draw_card(screen, 0, 0, card, show_number=False)

        expected_matrix = [list(" ____ "),
                           list("|   *|"),
                           list("|    |"),
                           list("|    |"),
                           list("|____|")]

        self.assertListEqual(expected_matrix, screen.get_matrix())

    def test_draw_card_with_invalid_coordinates(self):
        """
        A test that trying to draw a card on an invalid screen won't change the state of the screen
        """
        screen = Screen(4, 4)
        card = Card(3)

        self.assertRaises(IndexError, ScreenHelper.draw_card, screen, 0, 0, card)

        self.assertListEqual(Screen(4, 4).get_matrix(), screen.get_matrix())


class TestScreenHelperCardWillFitOnScreen(TestCase):
    def test_card_will_fit_on_screen_with_valid_coordinates(self):
        screen = Screen(6, 5)
        card = Card(3)

        self.assertTrue(ScreenHelper.card_will_fit_on_screen(screen, 0, 0, card))

    def test_card_will_fit_on_screen_with_invalid_x_coordinates(self):
        screen = Screen(5, 5)
        card = Card(3)

        self.assertFalse(ScreenHelper.card_will_fit_on_screen(screen, 1, 0, card))

    def test_card_will_fit_on_screen_with_invalid_y_coordinates(self):
        screen = Screen(5, 5)
        card = Card(3)

        self.assertFalse(ScreenHelper.card_will_fit_on_screen(screen, 0, 1, card))


class TestScreenHelperDrawColumn(TestCase):
    # TODO: Add tests for invalid x and y coordinates
    def test_draw_column_with_empty_column(self):
        screen = Screen(10, 10)
        column = Column()
        column.cards.items = []
        ScreenHelper.draw_column(screen, 0, 0, column)

        expected_screen = Screen(10, 10)

        self.assertListEqual(expected_screen.get_matrix(), screen.get_matrix())

    def test_draw_column_with_one_card_and_valid_coordinate(self):
        screen = Screen(10, 10)
        column = Column()
        column.cards.items = [Card(5)]
        ScreenHelper.draw_column(screen, 0, 0, column)

        expected_screen = Screen(10, 10)
        ScreenHelper.draw_card(expected_screen, 0, 0, Card(5))

        self.assertListEqual(expected_screen.get_matrix(), screen.get_matrix())

    def test_draw_column_with_multiple_cards_and_valid_coordinates(self):
        screen = Screen(10, 10)
        column = Column()
        column.cards.items = [Card(5), Card(4)]
        ScreenHelper.draw_column(screen, 1, 0, column)

        expected_screen = Screen(10, 10)
        ScreenHelper.draw_card(expected_screen, 1, 0, Card(5))
        ScreenHelper.draw_card(expected_screen, 1, 2, Card(4))

        self.assertListEqual(expected_screen.get_matrix(), screen.get_matrix())


class TestScreenHelperDrawGame(TestCase):
    def test_draw_game_with_empty_game(self):
        screen = Screen(10, 10)
        game = GameState(2)
        ScreenHelper.draw_game(screen, game)

        expected_screen = Screen(10, 10)

        self.assertListEqual(expected_screen.get_matrix(), screen.get_matrix())

    def test_draw_game_with_one_column(self):
        screen = Screen(10, 10)
        game = GameState(2)
        game.columns[0].cards.items = [Card(5), Card(4)]
        ScreenHelper.draw_game(screen, game)

        expected_screen = Screen(10, 10)
        column = Column()
        column.cards.items = [Card(5), Card(4)]
        ScreenHelper.draw_column(expected_screen, 0, 0, column)

        self.assertListEqual(expected_screen.get_matrix(), screen.get_matrix())

    def test_draw_game_with_multiple_columns(self):
        screen = Screen(30, 30)
        game = GameState(4)
        game.columns[0].cards.items = [Card(5), Card(4)]
        game.columns[1].cards.items = [Card(3), Card(2)]
        ScreenHelper.draw_game(screen, game)

        expected_screen = Screen(30, 30)
        column1 = Column()
        column2 = Column()
        column1.cards.items = [Card(5), Card(4)]
        column2.cards.items = [Card(3), Card(2)]
        ScreenHelper.draw_column(expected_screen, 0, 0, column1)
        ScreenHelper.draw_column(expected_screen, 10, 0, column2)

        self.assertListEqual(expected_screen.get_matrix(), screen.get_matrix())