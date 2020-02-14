from unittest import TestCase
from ScreenHelper import ScreenHelper
from Screen import Screen


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
