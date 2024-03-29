import unittest
from logical_test_2 import convert_number_to_roman


class TestConvertNumberToThai(unittest.TestCase):
    def tests(self):
        self.assertEqual(convert_number_to_roman(0), "")
        self.assertEqual(convert_number_to_roman(3), "III")
        self.assertEqual(convert_number_to_roman(58), "LVIII")
        self.assertEqual(convert_number_to_roman(999), "CMXCIX")
        self.assertEqual(convert_number_to_roman(1000), "M")


if __name__ == "__main__":
    unittest.main()
