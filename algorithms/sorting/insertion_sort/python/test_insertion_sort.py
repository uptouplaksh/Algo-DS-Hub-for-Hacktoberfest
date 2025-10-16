"""
Unit tests for Insertion Sort Algorithm

This module contains comprehensive unit tests for the insertion_sort function
to verify its correctness against various edge cases.
"""

import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """Test cases for the insertion_sort function."""
    
    def test_standard_unsorted_list(self):
        """Test with a standard, unsorted list."""
        input_list = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        result = insertion_sort(input_list.copy())
        self.assertEqual(result, expected)
    
    def test_already_sorted_list(self):
        """Test with an already sorted list."""
        input_list = [1, 2, 3, 4, 5, 6, 7, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        result = insertion_sort(input_list.copy())
        self.assertEqual(result, expected)
    
    def test_reverse_sorted_list(self):
        """Test with a reverse-sorted list."""
        input_list = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        result = insertion_sort(input_list.copy())
        self.assertEqual(result, expected)
    
    def test_list_with_duplicates(self):
        """Test with a list containing duplicate elements."""
        input_list = [5, 2, 8, 2, 9, 1, 5, 5]
        expected = [1, 2, 2, 5, 5, 5, 8, 9]
        result = insertion_sort(input_list.copy())
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        """Test with an empty list."""
        input_list = []
        expected = []
        result = insertion_sort(input_list.copy())
        self.assertEqual(result, expected)
    
    def test_single_element_list(self):
        """Test with a list containing a single element."""
        input_list = [42]
        expected = [42]
        result = insertion_sort(input_list.copy())
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
