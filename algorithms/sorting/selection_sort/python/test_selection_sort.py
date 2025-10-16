import unittest

# Import the selection_sort function from your implementation file
# Update this import according to your project’s structure if needed
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    """Unit tests for the Selection Sort algorithm."""

    def test_unsorted_list(self):
        """Test sorting a standard unsorted list."""
        data = [64, 25, 12, 22, 11]
        expected = [11, 12, 22, 25, 64]
        self.assertEqual(selection_sort(data.copy()), expected)

    def test_already_sorted_list(self):
        """Test sorting an already sorted list."""
        data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(data.copy()), expected)

    def test_reverse_sorted_list(self):
        """Test sorting a reverse-sorted list."""
        data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(data.copy()), expected)

    def test_list_with_duplicates(self):
        """Test sorting a list containing duplicate elements."""
        data = [4, 2, 5, 2, 3, 4]
        expected = [2, 2, 3, 4, 4, 5]
        self.assertEqual(selection_sort(data.copy()), expected)

    def test_empty_list(self):
        """Test sorting an empty list."""
        data = []
        expected = []
        self.assertEqual(selection_sort(data.copy()), expected)

    def test_single_element_list(self):
        """Test sorting a list with a single element."""
        data = [42]
        expected = [42]
        self.assertEqual(selection_sort(data.copy()), expected)


if __name__ == "__main__":
    unittest.main()
