import unittest
from linear_search import linear_search

class TestLinearSearch(unittest.TestCase):
    """Unit tests for the linear_search function."""
    
    def test_linear_search_with_element_in_the_middle(self):
        input_data = [0, -15, 23, 42, 7, 3, 99, -8, 55]
        search_target = 7
        expected_output = 4
        self.assertEqual(linear_search(input_data, search_target), expected_output)

    def test_linear_search_with_element_at_the_beginning(self):
        input_data = [100, -50, 0, 23, 77, -8, 42, 3, 99, 17, -100]
        search_target = 100
        expected_output = 0
        self.assertEqual(linear_search(input_data, search_target), expected_output)

    def test_linear_search_with_element_at_the_end(self):
        input_data = [5, 12, -27, 33, 2, 18, 44, -21, 9]
        search_target = 9
        expected_output = 8
        self.assertEqual(linear_search(input_data, search_target), expected_output)

    def test_linear_search_with_nonexistent_element(self):
        input_data = [-5, 12, -27, 33, 2, -1, 44, 21, 9, 0]
        search_target = 77
        expected_output = -1
        self.assertEqual(linear_search(input_data, search_target), expected_output)

    def test_linear_search_with_empty_list(self):
        input_data = []
        search_target = 14
        expected_output = -1
        self.assertEqual(linear_search(input_data, search_target), expected_output)

if __name__ == "__main__":
    unittest.main()
