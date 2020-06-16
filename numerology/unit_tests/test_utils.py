import unittest
from numerology.utils import add_digits, transliterate


class TestDestinyNumber(unittest.TestCase):

    def test_add_digits(self):
        self.assertEqual(add_digits(86), 5)
        self.assertEqual(add_digits(865), 1)

    def test_transliterate(self):
        self.assertEqual(transliterate('A'), 1)
        self.assertEqual(transliterate('Z'), 8)
