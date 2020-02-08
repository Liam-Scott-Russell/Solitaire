import unittest
from new_screen import Screen


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
        with self.assertRaises(IndexError):
            test_screen.get_point(-1, 23)

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
        with self.assertRaises(IndexError):
            test_screen.set_point(1, 2, "#")

if __name__ == "__main__":
    unittest.main()
