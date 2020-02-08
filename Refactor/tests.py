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


if __name__ == "__main__":
    unittest.main()
