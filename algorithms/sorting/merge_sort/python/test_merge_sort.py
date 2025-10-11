import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_odd_length_unsorted(self):
        arr = [3, 1, 4, 5, 2]
        expected = sorted(arr)
        self.assertEqual(merge_sort(arr), expected)

    def test_even_length_unsorted(self):
        arr = [8, 4, 2, 7, 1, 3]
        expected = sorted(arr)
        self.assertEqual(merge_sort(arr), expected)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = arr.copy()
        self.assertEqual(merge_sort(arr), expected)

    def test_duplicates(self):
        arr = [4, 1, 3, 4, 2, 1]
        expected = sorted(arr)
        self.assertEqual(merge_sort(arr), expected)

    def test_empty_list(self):
        arr = []
        expected = []
        self.assertEqual(merge_sort(arr), expected)

    def test_single_element(self):
        arr = [42]
        expected = [42]
        self.assertEqual(merge_sort(arr), expected)


if __name__ == '__main__':
    unittest.main()
