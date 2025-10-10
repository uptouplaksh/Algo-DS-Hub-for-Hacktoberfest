"""
This module contains a function to generate Pascal's Triangle.
Time Complexity: O(numRows^2)

The total number of operations is proportional to the number of entries in the
triangle, which is a triangular number series (1 + 2 + ... + n), resulting
in O(n^2) complexity.

Space Complexity: O(numRows^2)

The space required to store the triangle is also proportional to the number
of entries, which is O(n^2).
"""

def pascals_triangle(numRows: int) -> list:
    """
    Generates the first numRows of Pascal's Triangle.

    Args:
        numRows (int): The number of rows to generate.
    Returns:
        list[list[int]]: A list of lists representing Pascal's Triangle.
                         Returns an empty list if numRows <= 0.
    """
    if numRows <= 0:
        return []
    triangle = [[1]]
    for i in range(1, numRows):
        prev_row = triangle[i - 1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)
    return triangle

# --- Runnable Example ---
if __name__ == "__main__":
    rows_to_generate = 5
    result = pascals_triangle(rows_to_generate)
    print(f"Pascal's Triangle with {rows_to_generate} rows:")
    for row in result:
        print(row)

    print("\n--- Another Example ---")
    rows_to_generate = 8
    result = pascals_triangle(rows_to_generate)
    print(f"Pascal's Triangle with {rows_to_generate} rows:")
    for row in result:
        print(row)