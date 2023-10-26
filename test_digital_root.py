import unittest
from digital_root import digital_root

class TestDigitalRoot(unittest.TestCase):

    def test_digital_root_two_digits(self):
        self.assertEqual(digital_root(16), 7)

    def test_digital_root_three_digits(self):
        self.assertEqual(digital_root(942), 6)

    def test_digital_root_large_number(self):
        self.assertEqual(digital_root(132189), 6)

    def test_digital_root_single_digit(self):
        self.assertEqual(digital_root(5), 5)

    def test_digital_root_negative_number(self):
        self.assertEqual(digital_root(-10), -1)
