"""
Unit tests for Binary Search Algorithm (Iterative)

This module contains comprehensive unit tests for the binary_search_iterative function
to verify its correctness against various edge cases.
"""

import unittest
from binary_search_iterative import binary_search_iterative


class TestBinarySearch(unittest.TestCase):
    """Test cases for the binary_search_iterative function."""
    
    def test_element_exists(self):
        """Test for an element that exists in the array."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
        target = 7
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, 3)
    
    def test_element_does_not_exist(self):
        """Test for an element that does not exist in the array."""
        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
        target = 8
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, -1)
    
    def test_first_element(self):
        """Test for the first element in the array."""
        arr = [2, 4, 6, 8, 10, 12, 14]
        target = 2
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, 0)
    
    def test_last_element(self):
        """Test for the last element in the array."""
        arr = [2, 4, 6, 8, 10, 12, 14]
        target = 14
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, 6)
    
    def test_empty_list(self):
        """Test on an empty list."""
        arr = []
        target = 5
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, -1)
    
    def test_even_number_of_elements(self):
        """Test on an array with an even number of elements."""
        arr = [10, 20, 30, 40, 50, 60]
        target = 40
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, 3)
    
    def test_odd_number_of_elements(self):
        """Test on an array with an odd number of elements."""
        arr = [5, 15, 25, 35, 45]
        target = 25
        result = binary_search_iterative(arr, target)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
