import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    """Unit tests for the factorial function."""

    def test_factorial_of_zero(self):
        input_data = 0
        expected_output = 1
        self.assertEqual(factorial(input_data), expected_output)

    def test_factorial_of_one(self):
        input_data = 1
        expected_output = 1
        self.assertEqual(factorial(input_data), expected_output)

    def test_factorial_of_five(self):
        input_data = 5
        expected_output = 120
        self.assertEqual(factorial(input_data), expected_output)

    def test_factorial_of_negative_number(self):
        with self.assertRaisesRegex(ValueError, "Factorial is not defined for negative numbers"):
            factorial(-1)

if __name__ == "__main__":
    unittest.main()