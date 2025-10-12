"""
Unit tests for Segment Tree implementation.

Tests cover:
- Range queries on various ranges
- Point updates
- Queries after updates to verify correctness
- Single element queries
"""

import unittest
from segment_tree import SegmentTree


class TestSegmentTree(unittest.TestCase):
    """Test cases for Segment Tree data structure."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.arr = [1, 3, 5, 7, 9, 11]
        self.seg_tree = SegmentTree(self.arr)
    
    def test_query_full_range(self):
        """Test query for the entire array range."""
        result = self.seg_tree.query(0, 5)
        expected = sum(self.arr)  # 1 + 3 + 5 + 7 + 9 + 11 = 36
        self.assertEqual(result, expected)
    
    def test_query_partial_range(self):
        """Test query for partial ranges."""
        # Test range [1, 3]
        result = self.seg_tree.query(1, 3)
        expected = 3 + 5 + 7  # 15
        self.assertEqual(result, expected)
        
        # Test range [2, 4]
        result = self.seg_tree.query(2, 4)
        expected = 5 + 7 + 9  # 21
        self.assertEqual(result, expected)
        
        # Test range [0, 2]
        result = self.seg_tree.query(0, 2)
        expected = 1 + 3 + 5  # 9
        self.assertEqual(result, expected)
    
    def test_query_single_element(self):
        """Test query for a single element."""
        # Query single element at index 0
        result = self.seg_tree.query(0, 0)
        self.assertEqual(result, 1)
        
        # Query single element at index 3
        result = self.seg_tree.query(3, 3)
        self.assertEqual(result, 7)
        
        # Query single element at index 5
        result = self.seg_tree.query(5, 5)
        self.assertEqual(result, 11)
    
    def test_update_single_element(self):
        """Test updating a single element."""
        # Update element at index 2 from 5 to 10
        self.seg_tree.update(2, 10)
        
        # Verify the update with a single element query
        result = self.seg_tree.query(2, 2)
        self.assertEqual(result, 10)
    
    def test_query_after_update(self):
        """Test queries on ranges including the updated element."""
        # Update element at index 3 from 7 to 20
        self.seg_tree.update(3, 20)
        
        # Query range [1, 4] which includes the updated element
        # Expected: 3 + 5 + 20 + 9 = 37
        result = self.seg_tree.query(1, 4)
        self.assertEqual(result, 37)
        
        # Query full range after update
        # Expected: 1 + 3 + 5 + 20 + 9 + 11 = 49
        result = self.seg_tree.query(0, 5)
        self.assertEqual(result, 49)
        
        # Query range that doesn't include updated element
        # Expected: 1 + 3 = 4 (should remain unchanged)
        result = self.seg_tree.query(0, 1)
        self.assertEqual(result, 4)
    
    def test_multiple_updates(self):
        """Test multiple updates and verify correctness."""
        # Update multiple elements
        self.seg_tree.update(0, 2)   # 1 -> 2
        self.seg_tree.update(2, 6)   # 5 -> 6
        self.seg_tree.update(4, 10)  # 9 -> 10
        
        # Query various ranges to verify all updates
        result = self.seg_tree.query(0, 0)
        self.assertEqual(result, 2)
        
        result = self.seg_tree.query(2, 2)
        self.assertEqual(result, 6)
        
        result = self.seg_tree.query(4, 4)
        self.assertEqual(result, 10)
        
        # Query range including all updated elements
        # Expected: 2 + 3 + 6 + 7 + 10 + 11 = 39
        result = self.seg_tree.query(0, 5)
        self.assertEqual(result, 39)
    
    def test_query_edge_cases(self):
        """Test edge cases for queries."""
        # Query at boundaries
        result = self.seg_tree.query(0, 0)
        self.assertEqual(result, 1)
        
        result = self.seg_tree.query(5, 5)
        self.assertEqual(result, 11)
        
        # Query two adjacent elements
        result = self.seg_tree.query(2, 3)
        self.assertEqual(result, 12)  # 5 + 7
    
    def test_update_then_query_same_index(self):
        """Test updating an element and querying the same index."""
        # Update index 1
        self.seg_tree.update(1, 100)
        
        # Query the same index
        result = self.seg_tree.query(1, 1)
        self.assertEqual(result, 100)
        
        # Query range including that index
        result = self.seg_tree.query(0, 2)
        self.assertEqual(result, 1 + 100 + 5)  # 106
    
    def test_empty_array(self):
        """Test segment tree with empty array."""
        empty_tree = SegmentTree([])
        with self.assertRaises(IndexError):
            empty_tree.query(0, 0)
    
    def test_single_element_array(self):
        """Test segment tree with single element."""
        single_tree = SegmentTree([42])
        
        # Query the single element
        result = single_tree.query(0, 0)
        self.assertEqual(result, 42)
        
        # Update and query again
        single_tree.update(0, 100)
        result = single_tree.query(0, 0)
        self.assertEqual(result, 100)
    
    def test_large_values(self):
        """Test segment tree with large values."""
        large_arr = [1000000, 2000000, 3000000]
        large_tree = SegmentTree(large_arr)
        
        result = large_tree.query(0, 2)
        self.assertEqual(result, 6000000)
        
        # Update and verify
        large_tree.update(1, 5000000)
        result = large_tree.query(0, 2)
        self.assertEqual(result, 9000000)
    
    def test_negative_values(self):
        """Test segment tree with negative values."""
        neg_arr = [-5, 10, -3, 8, -2]
        neg_tree = SegmentTree(neg_arr)
        
        result = neg_tree.query(0, 4)
        self.assertEqual(result, 8)  # -5 + 10 + (-3) + 8 + (-2)
        
        # Query partial range
        result = neg_tree.query(1, 3)
        self.assertEqual(result, 15)  # 10 + (-3) + 8
        
        # Update and verify
        neg_tree.update(0, 5)
        result = neg_tree.query(0, 4)
        self.assertEqual(result, 18)  # 5 + 10 + (-3) + 8 + (-2)


if __name__ == '__main__':
    unittest.main()

