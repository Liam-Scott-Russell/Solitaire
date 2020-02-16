import unittest
from Screen import Screen


class TestScreen(unittest.TestCase):
    def test_get_point_with_valid_coordinates(self):
        """
        Test that a certain point on the screen can be accessed
        """
        test_screen = Screen(2, 2)

        actual_point = test_screen.get_point(1, 1)
        expected_point = " "

        self.assertEqual(actual_point, expected_point)

    def test_get_point_with_invalid_coordinates(self):
        """
        Test that the correct error is returned when trying to access invalid points
        """
        test_screen = Screen(2, 2)

        self.assertRaises(IndexError, test_screen.get_point, -1, 23)

    def test_set_point_with_valid_coordinates(self):
        """
        Test that a point on the screen can be set with a value
        """
        test_screen = Screen(2, 2)
        test_screen.set_point(1, 1, "#")

        expected_point = "#"
        actual_point = test_screen.get_point(1, 1)

        self.assertEqual(expected_point, actual_point)

    def test_set_point_with_invalid_coordinates(self):
        """
        Test that an invalid coordinate won't change the state of the screen
        """
        test_screen = Screen(2, 2)

        self.assertRaises(IndexError, test_screen.set_point, 1, 2, "#")

        self.assertEqual(test_screen.get_matrix(), Screen(2, 2).get_matrix())

    def test_get_dimensions(self):
        """
        Test that the screen returns the correct dimensions
        """
        test_screen = Screen(1, 2)

        actual_dimensions = test_screen.get_dimensions()
        expected_dimensions = (1, 2)

        self.assertTupleEqual(expected_dimensions, actual_dimensions)

    def test_get_matrix(self):
        """
        Test that the screen returns the correct matrix
        """
        test_screen = Screen(2, 2)
        test_screen.set_point(0, 0, "1")
        test_screen.set_point(1, 0, "2")
        test_screen.set_point(0, 1, "3")
        test_screen.set_point(1, 1, "4")

        actual_matrix = test_screen.get_matrix()
        expected_matrix = [["1", "2"], ["3", "4"]]

        self.assertListEqual(expected_matrix, actual_matrix)

    def test_point_is_valid_with_valid_coordinates(self):
        """
        Test that the screen can invalidate incorrect points
        """
        test_screen = Screen(2, 2)

        self.assertFalse(test_screen.point_is_valid(2, 1))
        self.assertFalse(test_screen.point_is_valid(2, 2))
        self.assertFalse(test_screen.point_is_valid(1, 2))
        self.assertFalse(test_screen.point_is_valid(-1, 0))
        self.assertFalse(test_screen.point_is_valid(0, -1))
