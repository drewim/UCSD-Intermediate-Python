import unittest
from unittest.mock import patch
from parameterized import parameterized
from io import StringIO
import sys

# Import the functions you want to test
from Helpers import *

class TestInputFunctions(unittest.TestCase):

    @parameterized.expand([
        ("valid_int", ["42"], 0, 100, 42, ""),
        ("min_value", ["0"], 0, 100, 0, ""),
        ("max_value", ["100"], 0, 100, 100, ""),
        ("negative value", ["-5", "2"], 0, 100, 2, "-5 is out of range. Please enter a value between 0 and 100\n"),
        ("invalid_then_valid", ["abc", "42"], 0, 100, 42, "Invalid entry: abc. Input needs to be in the int format.\n"),
        ("out_of_range_then_valid", ["101", "50"], 0, 100, 50, "101 is out of range. Please enter a value between 0 and 100\n"),
        ("multiple_invalid_then_valid", ["abc", "101", "42"], 0, 100, 42, "Invalid entry: abc. Input needs to be in the int format.\n101 is out of range. Please enter a value between 0 and 100\n"),
    ])
    @patch('builtins.input')
    def test_inputInt(self, name, input_values, min_value, max_value, expected_output, expected_print, mock_input):
        mock_input.side_effect = input_values
        captured_output = StringIO()
        sys.stdout = captured_output

        result = inputInt("Enter an integer: ", min_value, max_value)

        sys.stdout = sys.__stdout__
        self.assertEqual(result, expected_output, f"inputInt failed for {name}")
        self.assertEqual(captured_output.getvalue(), expected_print, f"Unexpected print output for {name}")

    @parameterized.expand([
        ("valid_float", ["3.14"], 0, 100, 3.14, ""),
        ("min_value", ["0.0"], 0, 100, 0.0, ""),
        ("max_value", ["100.0"], 0, 100, 100.0, ""),
        ("invalid_then_valid", ["abc", "3.14"], 0, 100, 3.14, "Invalid entry: abc. Input needs to be in the float format. Try again.\n"),
        ("out_of_range_then_valid", ["101.0", "50.5"], 0, 100, 50.5, "101.0 is out of range. Please enter a value between 0 and 100\n"),
        ("multiple_invalid_then_valid", ["abc", "101.0", "3.14"], 0, 100, 3.14, "Invalid entry: abc. Input needs to be in the float format. Try again.\n101.0 is out of range. Please enter a value between 0 and 100\n"),
    ])
    @patch('builtins.input')
    def test_inputFloat(self, name, input_values, min_value, max_value, expected_output, expected_print, mock_input):
        mock_input.side_effect = input_values
        captured_output = StringIO()
        sys.stdout = captured_output

        result = inputFloat("Enter a float: ", min_value, max_value)

        sys.stdout = sys.__stdout__
        self.assertAlmostEqual(result, expected_output, places=2, msg=f"inputFloat failed for {name}")
        self.assertEqual(captured_output.getvalue(), expected_print, f"Unexpected print output for {name}")

    @parameterized.expand([
        ("valid_string", ["hello"], 0, 10, "hello", ""),
        ("min_length", ["a"], 1, 10, "a", ""),
        ("max_length", ["helloworld"], 0, 10, "helloworld", ""),
        ("too_short_then_valid", ["", "hello"], 1, 10, "hello", "Str length 0 for input  is out of range. Length must be between 1 and 10\n"),
        ("too_long_then_valid", ["toolongstring", "hello"], 0, 10, "hello", f"Str length 13 for input toolongstring is out of range. Length must be between 0 and 10\n"),
    ])
    @patch('builtins.input')
    def test_inputString(self, name, input_values, min_length, max_length, expected_output, expected_print, mock_input):
        mock_input.side_effect = input_values
        captured_output = StringIO()
        sys.stdout = captured_output

        result = inputString("Enter a string: ", min_length, max_length)

        sys.stdout = sys.__stdout__
        self.assertEqual(result, expected_output, f"inputString failed for {name}")
        self.assertEqual(captured_output.getvalue(), expected_print, f"Unexpected print output for {name}")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInputFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\nTest Summary:")
    print(f"Ran {result.testsRun} tests")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

if __name__ == '__main__':
    run_tests()