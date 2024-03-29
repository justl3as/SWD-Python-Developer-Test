import unittest
from logical_test import convert_number_to_thai


class TestConvertNumberToThai(unittest.TestCase):
    def tests(self):
        self.assertEqual(convert_number_to_thai(0), "ศูนย์")
        self.assertEqual(convert_number_to_thai(1), "หนึ่ง")
        self.assertEqual(convert_number_to_thai(10), "สิบ")

        self.assertEqual(convert_number_to_thai(11), "สิบเอ็ด")
        self.assertEqual(convert_number_to_thai(21), "ยี่สิบเอ็ด")

        self.assertEqual(convert_number_to_thai(121), "หนึ่งร้อยยี่สิบเอ็ด")
        self.assertEqual(convert_number_to_thai(201), "สองร้อยเอ็ด")

        self.assertEqual(convert_number_to_thai(1340845), "หนึ่งล้านสามแสนสี่หมื่นแปดร้อยสี่สิบห้า")
        self.assertEqual(convert_number_to_thai(10000000), "สิบล้าน")


if __name__ == "__main__":
    unittest.main()
