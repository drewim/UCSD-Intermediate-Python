from DataTypeHelpers import *
import unittest

class TestDataTypeFunctions(unittest.TestCase):

    def test_isInt(self):
        self.assertTrue(isInt("123"))
        self.assertTrue(isInt("-456"))
        self.assertTrue(isInt("0"))
        self.assertFalse(isInt("12.3"))
        self.assertFalse(isInt("abc"))
        self.assertFalse(isInt(""))
        self.assertFalse(isInt("1.23e4"))

    def test_isFloat(self):
        self.assertTrue(isFloat("123.45"))
        self.assertTrue(isFloat("-67.89"))
        self.assertTrue(isFloat("0.0"))
        self.assertTrue(isFloat("1.23e4"))
        self.assertTrue(isFloat("-4.56E-2"))
        self.assertTrue(isFloat("123"))  # Integers are valid floats
        self.assertFalse(isFloat("abc"))
        self.assertFalse(isFloat(""))
        self.assertFalse(isFloat("12.34.56"))

    def test_isDate(self):
        self.assertTrue(isDate("2023-04-01"))
        self.assertTrue(isDate("1990-01-01"))
        self.assertTrue(isDate("2024-02-29"))  # Leap year
        self.assertFalse(isDate("2023-13-01"))  # Invalid month
        self.assertFalse(isDate("2023-04-31"))  # Invalid day
        self.assertFalse(isDate("2023/04/01"))  # Wrong format
        self.assertTrue(isDate("20230401"))    # Wrong format
        self.assertFalse(isDate(""))
        self.assertFalse(isDate("abc"))

if __name__ == '__main__':
    unittest.main()