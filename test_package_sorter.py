import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_special_bulky(self):
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")  # Bulky but not heavy

    def test_special_heavy(self):
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")  # Heavy but not bulky

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")  # Both bulky and heavy

    def test_invalid_input(self):
        self.assertEqual(sort(-50, 50, 50, 10), "INVALID INPUT")  # Negative dimension
        self.assertEqual(sort(None, 50, 50, 10), "INVALID INPUT")  # None value
        self.assertEqual(sort("abc", 50, 50, 10), "INVALID INPUT")  # String input

if __name__ == "__main__":
    unittest.main()
