# File: data_structures/Heap/python/min_heap.py

"""
Min-Heap Implementation in Python

A min-heap is a complete binary tree where the value of each parent node
is less than or equal to the values of its children.
This implementation provides the following operations:
    - insert(key): Adds a new element to the heap.
    - get_min(): Returns the smallest element (root) without removing it.
    - extract_min(): Removes and returns the smallest element.
    
Example:
    >>> heap = MinHeap()
    >>> heap.insert(10)
    >>> heap.insert(5)
    >>> heap.insert(20)
    >>> print(heap.get_min())
    5
    >>> print(heap.extract_min())
    5
    >>> print(heap.get_min())
    10
"""

class MinHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def _parent(self, index):
        """Return the index of the parent node."""
        return (index - 1) // 2

    def _left_child(self, index):
        """Return the index of the left child node."""
        return 2 * index + 1

    def _right_child(self, index):
        """Return the index of the right child node."""
        return 2 * index + 2

    def _heapify_up(self, index):
        """Maintain heap property after insertion."""
        while index > 0 and self.heap[self._parent(index)] > self.heap[index]:
            # Swap parent and current node if heap property is violated
            self.heap[self._parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self._parent(index)],
            )
            index = self._parent(index)

    def _heapify_down(self, index):
        """Maintain heap property after deletion."""
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        # Find the smallest among current, left, and right
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and continue
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, key):
        """Insert a new key into the heap."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):
        """Return the minimum element without removing it."""
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        """Remove and return the minimum element."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to root and heapify down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def __str__(self):
        """String representation of the heap."""
        return str(self.heap)


# ---------------------------
# Runnable Example Block
# ---------------------------
if __name__ == "__main__":
    print("Min-Heap Example Run\n")

    heap = MinHeap()
    print("Inserting elements: 10, 5, 3, 2, 8")
    for num in [10, 5, 3, 2, 8]:
        heap.insert(num)
        print(f"Heap after inserting {num}: {heap}")

    print("\nCurrent Min:", heap.get_min())

    print("\nExtracting elements:")
    while heap.get_min() is not None:
        print(f"Extracted: {heap.extract_min()} | Current Heap: {heap}")
