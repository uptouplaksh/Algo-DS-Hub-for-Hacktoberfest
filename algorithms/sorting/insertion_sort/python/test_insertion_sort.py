import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_standard_unsorted(self):
        arr = [12, 11, 13, 5, 6, 7]
        expected = sorted(arr)
        self.assertEqual(insertion_sort(arr.copy()), expected)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = arr.copy()
        self.assertEqual(insertion_sort(arr.copy()), expected)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = sorted(arr)
        self.assertEqual(insertion_sort(arr.copy()), expected)

    def test_duplicates(self):
        arr = [4, 1, 3, 4, 2, 1]
        expected = sorted(arr)
        self.assertEqual(insertion_sort(arr.copy()), expected)

    def test_empty_list(self):
        arr = []
        expected = []
        self.assertEqual(insertion_sort(arr.copy()), expected)

    def test_single_element(self):
        arr = [42]
        expected = [42]
        self.assertEqual(insertion_sort(arr.copy()), expected)


if __name__ == '__main__':
    unittest.main()
