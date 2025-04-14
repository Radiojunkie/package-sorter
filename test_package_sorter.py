import unittest
from package_sorter import sort

class TestPackageSorter(unittest.TestCase):
    def run_test(self, width, height, length, mass, expected):
        result = sort(width, height, length, mass)
        print(f"Testing: sort({width}, {height}, {length}, {mass}) -> Expected: {expected}, Got: {result}")
        self.assertEqual(result, expected)

    def test_standard(self):
        self.run_test(50, 50, 50, 10, "STANDARD")

    def test_special_bulky(self):
        self.run_test(200, 50, 50, 10, "SPECIAL")  # Bulky but not heavy

    def test_special_heavy(self):
        self.run_test(50, 50, 50, 20, "SPECIAL")  # Heavy but not bulky

    def test_rejected(self):
        self.run_test(200, 200, 200, 50, "REJECTED")  # Both bulky and heavy

    def test_invalid_input(self):
        self.run_test(-50, 50, 50, 10, "INVALID INPUT")  # Negative dimension
        self.run_test(None, 50, 50, 10, "INVALID INPUT")  # None value
        self.run_test("abc", 50, 50, 10, "INVALID INPUT")  # String input

if __name__ == "__main__":
    unittest.main()
