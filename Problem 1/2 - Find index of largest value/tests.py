import unittest
from main import find_index_largest_value


class TestFindIndexMaxInt(unittest.TestCase):
    def test_small(self):
        self.assertEqual(find_index_largest_value([]), 0)
        self.assertEqual(find_index_largest_value([42]), 0)
        self.assertEqual(find_index_largest_value([5, 2, 3, 5]), 3)
        self.assertEqual(find_index_largest_value([1, 5, 3, 2]), 1)
        self.assertEqual(find_index_largest_value([1, 2, 1, 3, 5, 6, 4]), 5)

    def test_large(self):
        self.assertEqual(
            find_index_largest_value([4] * (2 * 10**5)), 199999
        )  # 200000 elements


if __name__ == "__main__":
    unittest.main()
