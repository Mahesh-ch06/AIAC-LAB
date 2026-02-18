def sqroot(a):
    if a < 0:
        return "Cannot compute square root of a negative number."
    elif a == 0:
        return 0
    else:
        return a ** 0.5
import unittest
class TestSqroot(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sqroot(16), 4.0)
        self.assertEqual(sqroot(25), 5.0)

    def test_zero(self):
        self.assertEqual(sqroot(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sqroot(-4), "Cannot compute square root of a negative number.")
if __name__ == '__main__':
    unittest.main()