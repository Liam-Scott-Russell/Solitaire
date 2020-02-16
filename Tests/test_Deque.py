from unittest import TestCase
from Deque import Deque


class TestDeque(TestCase):
    def test_add_front_and_rear(self):
        deque = Deque()
        deque.add_front(0)
        deque.add_rear(1)
        deque.add_front(2)
        deque.add_rear(3)

        actual_items = deque.items
        expected_items = [3, 1, 0, 2]

        self.assertListEqual(actual_items, expected_items)

    def test_remove_front_with_items_in_deque(self):
        deque = Deque()
        deque.add_front(0)
        deque.add_front(1)
        deque.add_front(2)
        deque.add_front(3)

        actual_front = deque.remove_front()
        expected_front = 3

        self.assertEqual(actual_front, expected_front)
        self.assertListEqual(deque.items, [0, 1, 2])

    def test_remove_front_without_items_in_deque(self):
        deque = Deque()

        self.assertRaises(IndexError, deque.remove_front)

    def test_remove_rear_with_items_in_deque(self):
        deque = Deque()
        deque.add_front(0)
        deque.add_front(1)
        deque.add_front(2)
        deque.add_front(3)

        actual_rear = deque.remove_rear()
        expected_front = 0

        self.assertEqual(actual_rear, expected_front)
        self.assertListEqual(deque.items, [1, 2, 3])

    def test_remove_rear_without_items_in_deque(self):
        deque = Deque()

        self.assertRaises(IndexError, deque.remove_rear)

    def test_peek_front_with_items_in_deque(self):
        deque = Deque()
        deque.add_front(0)
        deque.add_front(1)
        deque.add_front(2)
        deque.add_front(3)

        actual_front = deque.peek_front()
        expected_front = 3

        self.assertEqual(actual_front, expected_front)
        self.assertListEqual(deque.items, [0, 1, 2, 3])

    def test_peek_front_without_items_in_deque(self):
        deque = Deque()

        self.assertRaises(IndexError, deque.peek_front)

    def test_peek_rear(self):
        deque = Deque()
        deque.add_front(0)
        deque.add_front(1)
        deque.add_front(2)
        deque.add_front(3)

        actual_rear = deque.peek_rear()
        expected_rear = 0

        self.assertEqual(actual_rear, expected_rear)
        self.assertListEqual(deque.items, [0, 1, 2, 3])

    def test_peek_rear_without_items_in_deque(self):
        deque = Deque()

        self.assertRaises(IndexError, deque.peek_rear)
