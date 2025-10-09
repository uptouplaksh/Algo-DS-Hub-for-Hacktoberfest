import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_with_unsorted_list(self):
        input_data = [10, -3, 5, 2, 9, 0, 1, 5, 6, -1]
        expected_output = [-3, -1, 0, 1, 2, 5, 5, 6, 9, 10]
        self.assertEqual(bubble_sort(input_data), expected_output)

    def test_bubble_sort_with_sorted_list(self):
        input_data = [-5, -2, 0, 3, 7, 8, 12]
        expected_output = [-5, -2, 0, 3, 7, 8, 12]
        self.assertEqual(bubble_sort(input_data), expected_output)

    def test_bubble_sort_with_reverse_sorted_list(self):
        input_data = [20, 15, 10, 5, 0, -5, -10]
        expected_output = [-10, -5, 0, 5, 10, 15, 20]
        self.assertEqual(bubble_sort(input_data), expected_output)

    def test_bubble_sort_with_list_having_duplicates(self):
        input_data = [4, 2, 5, 2, 8, 4, 2, 9, 5, 0, -1, 2, 8, 0, 4]
        expected_output = [-1, 0, 0, 2, 2, 2, 2, 4, 4, 4, 5, 5, 8, 8, 9]
        self.assertEqual(bubble_sort(input_data), expected_output)

    def test_bubble_sort_with_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_with_one_element_list(self):
        input_data = [-77]
        expected_output = [-77]
        self.assertEqual(bubble_sort(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()