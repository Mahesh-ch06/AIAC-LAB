def primechecker(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
import unittest
class TestPrimeChecker(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(primechecker(2))
        self.assertTrue(primechecker(3))
        self.assertTrue(primechecker(5))
        self.assertTrue(primechecker(7))
        self.assertTrue(primechecker(11))

    def test_non_prime_numbers(self):
        self.assertFalse(primechecker(0))
        self.assertFalse(primechecker(1))
        self.assertFalse(primechecker(4))
        self.assertFalse(primechecker(6))
        self.assertFalse(primechecker(9))
if __name__ == '__main__':
    unittest.main()
    