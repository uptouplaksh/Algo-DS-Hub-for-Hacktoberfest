"""
Segment Tree (range sum) implementation in Python.

File: data_structures/SegmentTree/python/segment_tree.py

Implements:
 - build(arr)         : builds the tree from a list/array
 - query(l, r)        : returns sum in inclusive range [l, r]
 - update(index, val) : updates the element at `index` to `val`

Usage:
  Place this file as instructed and run:
    python segment_tree.py
  It will run a small example and print outputs.

Complexity:
 - Build:  O(n)
 - Query:  O(log n) average / O(log n) worst-case (each query visits at most ~4*log n nodes)
 - Update: O(log n)
"""

from typing import List, Optional


class SegmentTree:
    """
    Segment Tree for range sum queries with point updates.

    This implementation stores the segment tree in a list `tree` sized 4*n to be safe.
    It is 0-indexed for the input array: array indices are 0..n-1.

    Public methods:
      - build(arr)
      - query(l, r)   # inclusive range [l, r]
      - update(i, v)  # set arr[i] = v
    """

    def __init__(self, arr: Optional[List[int]] = None):
        """
        Initialize the segment tree object. If `arr` is provided, automatically build.

        :param arr: optional initial list of numbers
        """
        self.n = 0
        self.tree: List[int] = []
        self.arr: List[int] = []
        if arr is not None:
            self.build(arr)

    def build(self, arr: List[int]) -> None:
        """
        Build the segment tree from the given array.

        :param arr: list of integers (or floats)
        Time complexity: O(n)
        """
        if arr is None:
            raise ValueError("Input array cannot be None")
        self.arr = arr[:]  # copy input array
        self.n = len(arr)
        if self.n == 0:
            self.tree = []
            return
        # safe size: 4 * n
        self.tree = [0] * (4 * self.n)
        self._build_rec(1, 0, self.n - 1)

    def _build_rec(self, node: int, left: int, right: int) -> None:
        """
        Recursively build the segment tree.

        node: current node index in self.tree (1-based indexing for convenience)
        left, right: current segment boundaries (inclusive)
        """
        if left == right:
            self.tree[node] = self.arr[left]
            return
        mid = (left + right) // 2
        self._build_rec(node * 2, left, mid)
        self._build_rec(node * 2 + 1, mid + 1, right)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, l: int, r: int) -> int:
        """
        Query sum in inclusive range [l, r].

        :param l: left index (0-based)
        :param r: right index (0-based)
        :return: sum of arr[l..r]
        Time complexity: O(log n) per query (amortized / typical)
        """
        if self.n == 0:
            raise IndexError("Segment tree is empty. Build it before querying.")
        if l < 0 or r < 0 or l >= self.n or r >= self.n:
            raise IndexError("Query indices out of bounds")
        if l > r:
            raise ValueError("Left index cannot be greater than right index")
        return self._query_rec(1, 0, self.n - 1, l, r)

    def _query_rec(self, node: int, left: int, right: int, ql: int, qr: int) -> int:
        """
        Recursive helper for query.
        """
        # total overlap
        if ql <= left and right <= qr:
            return self.tree[node]

        # no overlap
        if right < ql or left > qr:
            return 0

        mid = (left + right) // 2
        left_sum = self._query_rec(node * 2, left, mid, ql, qr)
        right_sum = self._query_rec(node * 2 + 1, mid + 1, right, ql, qr)
        return left_sum + right_sum

    def update(self, index: int, value: int) -> None:
        """
        Point update: set arr[index] = value and update segment tree.

        :param index: position to update (0-based)
        :param value: new value
        Time complexity: O(log n)
        """
        if self.n == 0:
            raise IndexError("Segment tree is empty. Build it before updating.")
        if index < 0 or index >= self.n:
            raise IndexError("Update index out of bounds")
        self._update_rec(1, 0, self.n - 1, index, value)

    def _update_rec(self, node: int, left: int, right: int, idx: int, val: int) -> None:
        """
        Recursive helper for update.
        """
        if left == right:
            # leaf node
            self.tree[node] = val
            self.arr[idx] = val
            return
        mid = (left + right) // 2
        if idx <= mid:
            self._update_rec(node * 2, left, mid, idx, val)
        else:
            self._update_rec(node * 2 + 1, mid + 1, right, idx, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    # Optional helper to pretty-print internal tree (for debugging)
    def __repr__(self) -> str:
        return f"SegmentTree(n={self.n}, arr={self.arr})"


# Runnable example block
if __name__ == "__main__":
    # Example: build, query, update, query again
    example = [2, 1, 5, 3, 4]  # sample array
    print("Original array:", example)

    st = SegmentTree(example)
    # Query the sum from index 1 to 3  (1 + 5 + 3 = 9)
    s1 = st.query(1, 3)
    print("Sum of range [1, 3]:", s1)

    # Update index 2 from 5 -> 10
    print("Update: arr[2] = 10")
    st.update(2, 10)

    # Now query [1, 3] again (1 + 10 + 3 = 14)
    s2 = st.query(1, 3)
    print("Sum of range [1, 3] after update:", s2)

    # Query full range
    print("Sum of full array [0, 4]:", st.query(0, 4))

    # Edge checks
    try:
        print("Attempting invalid query [4, 1] (should raise):")
        st.query(4, 1)
    except ValueError as e:
        print("Caught expected exception:", e)
