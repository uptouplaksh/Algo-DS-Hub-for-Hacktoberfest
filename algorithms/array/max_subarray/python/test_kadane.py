import unittest
from kadane import kadane

class TestKadane(unittest.TestCase):
    """Unit tests for the kadane function."""

    def test_kadane_with_mixed_array(self):
        input_data = [4, -1, 2, 1, -7, 5, -3, 2, 6, -5, 4]
        expected_output = 10  # The maximum subarray is [5, -3, 2, 6]
        self.assertEqual(kadane(input_data), expected_output)

    def test_kadane_with_positive_numbers_array(self):
        input_data = [3, 7, 2, 8, 10, 6]
        expected_output = 36  # The sum of the entire array
        self.assertEqual(kadane(input_data), expected_output)

    def test_kadane_with_negative_numbers_array(self):
        input_data = [-8, -3, -6, -2, -5, -4]
        expected_output = -2  # The maximum subarray is [-2]
        self.assertEqual(kadane(input_data), expected_output)

    def test_kadane_with_empty_array(self):
        input_data = []
        expected_output = 0
        self.assertEqual(kadane(input_data), expected_output)

    def test_kadane_with_single_element_array(self):
        input_data = [7]
        expected_output = 7
        self.assertEqual(kadane(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()
