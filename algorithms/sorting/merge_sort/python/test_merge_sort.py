"""
Unit tests for Merge Sort Algorithm

This module contains comprehensive unit tests for the merge_sort function
to verify its correctness against various edge cases.
"""

import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    """Test cases for the merge_sort function."""

    def test_odd_length_unsorted_list(self):
        """Test with an odd-lengthed, unsorted list."""
        input_list = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        result = merge_sort(input_list)
        self.assertEqual(result, expected)

    def test_even_length_unsorted_list(self):
        """Test with an even-lengthed, unsorted list."""
        input_list = [38, 27, 43, 3, 9, 82]
        expected = [3, 9, 27, 38, 43, 82]
        result = merge_sort(input_list)
        self.assertEqual(result, expected)

    def test_already_sorted_list(self):
        """Test with an already sorted list."""
        input_list = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        result = merge_sort(input_list)
        self.assertEqual(result, expected)

    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        input_list = [5, 2, 8, 2, 9, 1, 5, 5]
        expected = [1, 2, 2, 5, 5, 5, 8, 9]
        result = merge_sort(input_list)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test with an empty list."""
        input_list = []
        expected = []
        result = merge_sort(input_list)
        self.assertEqual(result, expected)

    def test_single_element_list(self):
        """Test with a list containing a single element."""
        input_list = [42]
        expected = [42]
        result = merge_sort(input_list)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
