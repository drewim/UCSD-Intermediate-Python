import unittest
from lab1_drewimhof import check_for_palindrome, score_password

class TestLab1(unittest.TestCase):

    palindrome_test_cases = [
        ('MOM', True),
        ('Redivider', True),
        ('LEVel', True),
        ('Was it a car or a cat I saw', True),
        ('test', False),
        ('dad', True),
        ('reset', False)
    ]

    password_test_cases = [
        {"password": "weak", "expected_score": 1},  # Only lowercase, length < 8
        {"password": "password", "expected_score": 2},  # Length = 8, only lowercase
        {"password": "password123", "expected_score": 4},  # Length > 8, lowercase, number
        {"password": "Password123", "expected_score": 5},  # Length > 8, upper, lower, number
        {"password": "Password123!", "expected_score": 6},  # Length > 8, upper, lower, number, symbol
        {"password": "LongPassword123!", "expected_score": 7},  # Length > 8, upper, lower, number, symbol
        {"password": "VeryLongPassword123!@#", "expected_score": 7},  # Length >= 16, upper, lower, number, symbol
        {"password": "SHORT1!", "expected_score": 3},  # Upper, lower, number, symbol, but length < 8
        {"password": "ALLUPPERCASE", "expected_score": 3},  # Length > 8, only uppercase
        {"password": "alllowercase", "expected_score": 3},  # Length > 8, only lowercase
        {"password": "12345678", "expected_score": 2},  # Length = 8, only numbers
        {"password": "!@#$%^&*", "expected_score": 2},  # Length = 8, only symbols
        {"password": "Mixed123", "expected_score": 4},  # Length = 8, upper, lower, number
        {"password": "a1B!", "expected_score": 4},  # Short but diverse, length < 8
        {"password": "abcdefghijklmnopqrstuvwxyz", "expected_score": 4},  # Length >= 16, only lowercase
        {"password": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "expected_score": 4},  # Length >= 16, only uppercase
        {"password": "01234567890123456789", "expected_score": 4},  # Length >= 16, only numbers
        {"password": "!@#$%^&*!@#$%^&*!@#$%^&*", "expected_score": 4},  # Length >= 16, only symbols
        {"password": "aA1!", "expected_score": 4},  # All categories but length < 8
        {"password": "aaaaaaaA1!", "expected_score": 6},  # Length > 8, all categories
        {"password": "", "expected_score": 0},  # Empty password
    ]

    def test_check_for_palindrome(self):
        for input_value, expected_output in self.palindrome_test_cases:
            with self.subTest(input_value):
                self.assertEqual(check_for_palindrome(input_value), expected_output, 
                                 f"Failed for string: {input_value}")


    def test_score_password(self):
        for case in self.password_test_cases:
            with self.subTest(password=case['password']):
                self.assertEqual(
                    score_password(case['password']),
                    case['expected_score'],
                    f"Failed for password: {case['password']}"
                )