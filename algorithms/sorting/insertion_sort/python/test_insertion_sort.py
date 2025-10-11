import os
import sys
import unittest

# Ensure the insertion_sort module in this directory can be imported when tests
# are run from the repository root.
sys.path.insert(0, os.path.dirname(__file__))

from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_standard_unsorted(self):
        arr = [12, 11, 13, 5, 6]
        expected = sorted(arr)
        result = insertion_sort(arr.copy())
        self.assertEqual(result, expected)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = sorted(arr)
        result = insertion_sort(arr.copy())
        self.assertEqual(result, expected)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = sorted(arr)
        result = insertion_sort(arr.copy())
        self.assertEqual(result, expected)

    def test_with_duplicates(self):
        arr = [3, 1, 2, 3, 2, 1]
        expected = sorted(arr)
        result = insertion_sort(arr.copy())
        self.assertEqual(result, expected)

    def test_empty_list(self):
        arr = []
        expected = []
        result = insertion_sort(arr.copy())
        self.assertEqual(result, expected)

    def test_single_element(self):
        arr = [42]
        expected = [42]
        result = insertion_sort(arr.copy())
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
