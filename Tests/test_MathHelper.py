from unittest import TestCase
from MathHelper import MathHelper


class TestMathHelper(TestCase):
    def test_calculate_points_on_line_for_horizontal_line(self):
        """
        Test that the implementation of bresenham's algorithm works for horizontal lines
        """
        actual_points = MathHelper.calculate_points_on_line(0, 0, 3, 0)
        expected_points = [(0, 0), (1, 0), (2, 0), (3, 0)]

        self.assertListEqual(actual_points, expected_points)

    def test_calculate_points_on_line_for_vertical_line(self):
        """
        Test that the implementation of bresenham's algorithm works for vertical lines
        """
        actual_points = MathHelper.calculate_points_on_line(0, 0, 0, 3)
        expected_points = [(0, 0), (0, 1), (0, 2), (0, 3)]

        self.assertListEqual(actual_points, expected_points)

    def test_calculate_points_on_line_for_perfect_diagonal_line(self):
        """
        Test that the implementation of bresenham's algorithm works for perfect diagonal lines
        """
        actual_points = MathHelper.calculate_points_on_line(0, 0, 3, 3)
        expected_points = [(0, 0), (1, 1), (2, 2), (3, 3)]

        self.assertListEqual(actual_points, expected_points)

    def test_calculate_points_on_line_for_imperfect_diagonal_line(self):
        """
        Test that the implementation of bresenham's algorithm works for imperfect diagonal lines
        """
        actual_points = MathHelper.calculate_points_on_line(0, 0, 3, 4)
        expected_points = [(0, 0), (1, 1), (2, 2), (3, 3), (3, 4)]

        self.assertListEqual(actual_points, expected_points)
