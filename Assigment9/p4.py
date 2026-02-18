'''write a function leapyear and check functionallity of a function using unittest with a test case.'''
def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
import unittest
class TestLeapYear(unittest.TestCase):
    def test_leap_years(self):
        self.assertTrue(leapyear(2020))
        self.assertTrue(leapyear(2000))
        self.assertTrue(leapyear(2400))

    def test_non_leap_years(self):
        self.assertFalse(leapyear(2019))
        self.assertFalse(leapyear(1900))
        self.assertFalse(leapyear(2100))
if __name__ == '__main__':
    unittest.main()
    