from unittest import TestCase
from ScreenHelper import ScreenHelper
from Screen import Screen
from Card import Card


class TestScreenHelper(TestCase):
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

        with self.assertRaises(IndexError):
            ScreenHelper.draw_line(screen, 0, 0, 3, 0, "#")

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

        with self.assertRaises(IndexError):
            ScreenHelper.draw_line(screen, 0, 0, 0, 3, "#")

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

        with self.assertRaises(IndexError):
            ScreenHelper.draw_line(screen, 0, 0, 0, 3, "#")

        self.assertListEqual(screen.get_matrix(), Screen(2, 2).get_matrix())

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

        with self.assertRaises(IndexError):
            ScreenHelper.draw_card(screen, 0, 0, card)

        self.assertListEqual(Screen(4, 4).get_matrix(), screen.get_matrix())

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
