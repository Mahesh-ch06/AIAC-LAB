def add(a,b):
    return a + b
import unittest
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, -20), -30)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(10, -20), -10)
if __name__ == '__main__':
    unittest.main()
    