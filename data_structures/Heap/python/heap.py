"""
Heap Data Structure Implementation

This module implements both MinHeap and MaxHeap data structures using a binary heap.
A binary heap is a complete binary tree where the value of each node is either greater
than or equal to (max-heap) or less than or equal to (min-heap) the values of its children.

Time Complexity:
- Insert: O(log n)
- Delete: O(log n)
- Get Min/Max: O(1)
- Build Heap: O(n)

Space Complexity:
- O(n) for storing n elements
"""

class MinHeap:
    """
    MinHeap class implementation where the root is the minimum element.
    
    Attributes:
        heap (list): List to store heap elements
    """
    
    def __init__(self):
        """Initialize an empty min heap."""
        self.heap = []
        
    def parent(self, i):
        """Return the parent index of element at index i."""
        return (i - 1) // 2
        
    def left_child(self, i):
        """Return the left child index of element at index i."""
        return 2 * i + 1
        
    def right_child(self, i):
        """Return the right child index of element at index i."""
        return 2 * i + 2
        
    def swap(self, i, j):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        """
        Insert a new key into the min heap.
        
        Args:
            key: The value to insert
            
        Time Complexity: O(log n)
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        """Move a node up in the tree to maintain heap property."""
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
            
    def extract_min(self):
        """
        Remove and return the minimum element from the heap.
        
        Returns:
            The minimum element
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(log n)
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
            
        if len(self.heap) == 1:
            return self.heap.pop()
            
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return min_val
        
    def _sift_down(self, i):
        """Move a node down in the tree to maintain heap property."""
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
            
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)
            
    def get_min(self):
        """
        Get the minimum element without removing it.
        
        Returns:
            The minimum element
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(1)
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]


class MaxHeap:
    """
    MaxHeap class implementation where the root is the maximum element.
    
    Attributes:
        heap (list): List to store heap elements
    """
    
    def __init__(self):
        """Initialize an empty max heap."""
        self.heap = []
        
    def parent(self, i):
        """Return the parent index of element at index i."""
        return (i - 1) // 2
        
    def left_child(self, i):
        """Return the left child index of element at index i."""
        return 2 * i + 1
        
    def right_child(self, i):
        """Return the right child index of element at index i."""
        return 2 * i + 2
        
    def swap(self, i, j):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        """
        Insert a new key into the max heap.
        
        Args:
            key: The value to insert
            
        Time Complexity: O(log n)
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        """Move a node up in the tree to maintain heap property."""
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
            
    def extract_max(self):
        """
        Remove and return the maximum element from the heap.
        
        Returns:
            The maximum element
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(log n)
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
            
        if len(self.heap) == 1:
            return self.heap.pop()
            
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return max_val
        
    def _sift_down(self, i):
        """Move a node down in the tree to maintain heap property."""
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left
            
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right
            
        if i != max_index:
            self.swap(i, max_index)
            self._sift_down(max_index)
            
    def get_max(self):
        """
        Get the maximum element without removing it.
        
        Returns:
            The maximum element
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(1)
        """
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]


# Example usage and testing
if __name__ == "__main__":
    # Test MinHeap
    min_heap = MinHeap()
    print("Testing MinHeap:")
    
    # Insert some elements
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for element in elements:
        min_heap.insert(element)
        
    print("Extracting elements from MinHeap:")
    try:
        while True:
            print(min_heap.extract_min(), end=" ")
    except IndexError:
        print("\n")
        
    # Test MaxHeap
    max_heap = MaxHeap()
    print("\nTesting MaxHeap:")
    
    # Insert the same elements
    for element in elements:
        max_heap.insert(element)
        
    print("Extracting elements from MaxHeap:")
    try:
        while True:
            print(max_heap.extract_max(), end=" ")
    except IndexError:
        print("\n")