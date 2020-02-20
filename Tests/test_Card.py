from unittest import TestCase
from DTOs.Card import Card

class TestCard(TestCase):
    def test_get_representation_with_single_digit_and_number_shown(self):
        test_card = Card(2)
        actual_representation = test_card.get_representation()
        expected_representation = ""
        expected_representation += " ____\n"
        expected_representation += "|   2|\n"
        expected_representation += "|    |\n"
        expected_representation += "|    |\n"
        expected_representation += "|____|"

        self.assertEqual(expected_representation, actual_representation)

    def test_get_representation_with_double_digit_and_number_shown(self):
        test_card = Card(10)
        actual_representation = test_card.get_representation()
        expected_representation = ""
        expected_representation += " ____\n"
        expected_representation += "|  10|\n"
        expected_representation += "|    |\n"
        expected_representation += "|    |\n"
        expected_representation += "|____|"

        self.assertEqual(expected_representation, actual_representation)

    def test_get_representation_with_single_digit_and_number_not_shown(self):
        test_card = Card(2)
        actual_representation = test_card.get_representation(show_number=False)
        expected_representation = ""
        expected_representation += " ____\n"
        expected_representation += "|   *|\n"
        expected_representation += "|    |\n"
        expected_representation += "|    |\n"
        expected_representation += "|____|"

        self.assertEqual(expected_representation, actual_representation)

    def test_get_representation_with_double_digit_and_number_not_shown(self):
        test_card = Card(10)
        actual_representation = test_card.get_representation(show_number=False)
        expected_representation = ""
        expected_representation += " ____\n"
        expected_representation += "|   *|\n"
        expected_representation += "|    |\n"
        expected_representation += "|    |\n"
        expected_representation += "|____|"

        self.assertEqual(expected_representation, actual_representation)
