#!/usr/bin/env python3
"""Unit tests for insertion_sort using Python's built-in unittest.

Tests included:
- standard unsorted list
- already sorted list
- reverse-sorted list
- list with duplicate elements
- empty list
- single-element list
"""
import os
import sys
import unittest

# Ensure the insertion_sort module in this directory can be imported
TEST_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(TEST_DIR))

from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_unsorted_list(self):
        arr = [12, 11, 13, 5, 6]
        result = insertion_sort(arr.copy())
        self.assertEqual(result, sorted(arr))

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        result = insertion_sort(arr.copy())
        self.assertEqual(result, arr)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        result = insertion_sort(arr.copy())
        self.assertEqual(result, sorted(arr))

    def test_duplicates(self):
        arr = [3, 1, 2, 3, 2, 1]
        result = insertion_sort(arr.copy())
        self.assertEqual(result, sorted(arr))

    def test_empty_list(self):
        arr = []
        result = insertion_sort(arr.copy())
        self.assertEqual(result, [])

    def test_single_element(self):
        arr = [42]
        result = insertion_sort(arr.copy())
        self.assertEqual(result, [42])


if __name__ == "__main__":
    unittest.main()
