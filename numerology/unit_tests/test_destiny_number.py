import unittest
from numerology.destiny_number import get_destiny_number


class TestDestinyNumber(unittest.TestCase):

    def test_get_destiny_number(self):
        self.assertEqual(get_destiny_number('Ana Gabriela Cantu De Leon'), 5)
