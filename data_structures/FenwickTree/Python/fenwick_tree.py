#!/usr/bin/env python3

# Usage:
#   python fenwick_tree.py

class FenwickTree:
    """
    A Fenwick Tree (Binary Indexed Tree, a.k.a BIT).

    This is a data structure that can efficiently update elements and calculate prefix sums
    in a table of numbers.

    Args:
        n: The size of the array to be managed by the Fenwick Tree.
    """
    def __init__(self, n: int):
        self._n = n

        # Internal array to store the Fenwick Tree.
        # The items inside the array will be the same as the original array,
        # but the order will be different.
        self._array = [0] * (n + 1)

    def update(self, i: int, delta: int):
        """
        Update the value at specified index by adding delta.

        Args:
            i: The index to update.
            delta: The value to add to the element at the specified index.
        """
        # Convert to 1-based index.
        i += 1

        while i <= self._n:
            self._array[i] += delta

            # Determine the next index to update.
            #
            # Think of numbers as boxes of switches, each number has switches.
            # A `1` means that switch is ON.
            # The lowest switch that's on (the rightmost 1) is what `i & -i` finds.
            #
            # Example:
            #   i	Binary  Lowest switch ON    i & -i  Detail
            #   ------------------------------------------------------------
            #   0	0000	None	            0	    No switch on
            #   1	0001	1	                1	    rightmost 1 is bit 0
            #   2	0010	2	                2	    rightmost 1 is bit 1
            #   3	0011	1	                1	    rightmost 1 is bit 0
            #   4	0100	4	                4	    rightmost 1 is bit 2
            #
            # While loop steps example:
            #   i   i + (i & -i)
            #   -----------------
            #   0   0
            #   1   2
            #   2   4
            #   3   4
            #   4   8
            i += i & -i

    def query(self, i: int) -> int:
        """
        Compute the prefix sum from index 0 to `i` (inclusive).

        Args:
            i: The index up to which to compute the prefix sum.

        Returns:
            The prefix sum.
        """
        # Convert to 1-based index.
        i += 1

        result = 0
        while i > 0:
            result += self._array[i]

            # Determine the next index to query.
            #
            # This is similar to the update function, but instead of moving to the next
            # index to update, we move to the parent index in the tree.
            # We do this by turning off the lowest switch that's ON.
            #
            # Example:
            #   i	Binary  Lowest switch ON    i & -i  Detail
            #   ------------------------------------------------------------
            #   0	0000	None	            0	    No switch on
            #   1	0001	1	                1	    rightmost 1 is bit 0
            #   2	0010	2	                2	    rightmost 1 is bit 1
            #   3	0011	1	                1       rightmost 1 is bit 0
            #   4	0100	4                   4	    rightmost 1 is bit 2
            #
            # While loop steps example:
            #   i   i - (i & -i)
            #   -----------------
            #   0   0
            #   1   0
            #   2   0
            #   3   2
            #   4   0
            i -= i & -i

        return result

    def range_query(self, l: int, r: int) -> int:
        """
        Compute the sum of the range [l, r] (inclusive).

        Args:
            l: The left index (starting index of the range).
            r: The right index (ending index of the range).

        Returns:
            The sum of the elements in the specified range.
        """
        return self.query(r) - self.query(l - 1)


def tests():
    # Build tree.
    array = [0, 3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
    ft = FenwickTree(len(array))
    for i, val in enumerate(array):
        ft.update(i, val)

    # Query tests.
    assert ft.query(0) == 0 == sum(array[:1])
    assert ft.query(1) == 3 == sum(array[:2])
    assert ft.query(2) == 5 == sum(array[:3])
    assert ft.query(3) == 4 == sum(array[:4])
    assert ft.query(4) == 10 == sum(array[:5])
    assert ft.query(5) == 15 == sum(array[:6])
    assert ft.query(-5) == 0 == sum(array[:1])

    # Range query tests.
    assert ft.range_query(2, 2) == 2 == sum(array[2:3])
    assert ft.range_query(2, 4) == 7 == sum(array[2:5])
    assert ft.range_query(0, 9) == 26 == sum(array[0:10])
    assert ft.range_query(-5, 9) == 26 == sum(array[0:10])

    # Update tests.
    ft.update(3, 2)
    array[3] += 2  # -1 + 2 = 1
    assert ft.query(3) == 6 == sum(array[:4])
    assert ft.range_query(3, 3) == 1 == sum(array[3:4])
    assert ft.range_query(2, 4) == 9 == sum(array[2:5])


if __name__ == "__main__":
    tests()
