"""
Unit tests for Two Sum implementation.

Time Complexity: O(1) per test case - Each test runs in constant time
Space Complexity: O(1) per test case - No additional space beyond test data
"""
import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    """
    Comprehensive unit tests for the two_sum function.
    Tests cover various scenarios including basic cases, edge cases,
    and special conditions like duplicates and negative numbers.
    """

    def test_basic_case(self):
        """
        Test basic case where a solution exists.
        
        Input: [2, 7, 11, 15] with target 9
        Expected: [0, 1] because nums[0] + nums[1] = 2 + 7 = 9
        
        Time Complexity: O(n) where n is the length of the input list
        Space Complexity: O(n) for the hash map storage
        """
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_no_solution(self):
        """
        Test case where no solution exists - should return empty list.
        
        Input: [1, 2, 3] with target 10
        Expected: [] because no two numbers add up to 10
        
        Time Complexity: O(n) - must check all elements
        Space Complexity: O(n) - hash map stores all elements
        """
        nums = [1, 2, 3]
        target = 10
        result = two_sum(nums, target)
        self.assertEqual(result, [])

    def test_duplicate_numbers(self):
        """
        Test case involving duplicate numbers.
        
        Input: [3, 3] with target 6
        Expected: [0, 1] because nums[0] + nums[1] = 3 + 3 = 6
        
        This tests that the algorithm correctly handles using the same
        value at different indices.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nums = [3, 3]
        target = 6
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_negative_numbers(self):
        """
        Test case involving negative numbers.
        
        Input: [-1, -2, -3, -4, -5] with target -8
        Expected: Valid pair of indices where nums[i] + nums[j] = -8
        For example, nums[2] + nums[4] = -3 + -5 = -8, so [2, 4]
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = two_sum(nums, target)
        # Verify we got a valid result with two indices
        self.assertEqual(len(result), 2)
        # Verify the sum is correct
        self.assertEqual(nums[result[0]] + nums[result[1]], target)

    def test_empty_list(self):
        """
        Test empty list edge case.
        
        Input: [] with target 5
        Expected: [] because there are no elements to sum
        
        This tests the algorithm's handling of edge cases.
        
        Time Complexity: O(1) - no elements to process
        Space Complexity: O(1) - no storage needed
        """
        nums = []
        target = 5
        result = two_sum(nums, target)
        self.assertEqual(result, [])

    def test_two_elements_valid(self):
        """
        Additional test: Minimum valid case with exactly two elements.
        
        Input: [1, 2] with target 3
        Expected: [0, 1]
        """
        nums = [1, 2]
        target = 3
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_larger_list(self):
        """
        Additional test: Verify algorithm works with larger lists.
        
        Input: [1, 2, 3, 4, 5, 6, 7, 8, 9] with target 17
        Expected: [7, 8] because nums[7] + nums[8] = 8 + 9 = 17
        """
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 17
        result = two_sum(nums, target)
        self.assertEqual(result, [7, 8])


if __name__ == '__main__':
    unittest.main()
