import unittest
from main import find_trailing_zeros


class TestFindTrailingZeros(unittest.TestCase):
    def test_small(self):
        self.assertEqual(find_trailing_zeros(0), 0)
        self.assertEqual(find_trailing_zeros(7), 1)
        self.assertEqual(find_trailing_zeros(10), 2)

    def test_large(self):
        self.assertEqual(find_trailing_zeros(45), 10)
        self.assertEqual(find_trailing_zeros(50), 12)
        self.assertEqual(find_trailing_zeros(200), 49)
        self.assertEqual(find_trailing_zeros(205), 50)
        self.assertEqual(find_trailing_zeros(300), 74)


if __name__ == "__main__":
    unittest.main()
