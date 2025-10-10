
### This module contains a function to generate Pascal's Triangle
def pascals_triangle(numRows: int) -> list:
    """
    Generates the first numRows of Pascal's Triangle.

    Args:
        numRows: An integer representing the number of rows to generate.

    Returns:
        A list of lists of integers representing Pascal's Triangle.
        Returns an empty list if numRows is less than or equal to 0.

    Time Complexity: O(numRows^2)
        - The outer loop runs numRows times.
        - The inner loop runs up to i times, where i is the current row number.
        - The total number of operations is roughly proportional to 1 + 2 + 3 + ... + numRows,
          which is a triangular number series, simplified to O(n^2).

    Space Complexity: O(numRows^2)
        - The space required to store the triangle is proportional to the number of elements.
        - The total number of elements is also a triangular number series,
          proportional to numRows^2.
    """
    #if num rows 0 or less return empty list
    if numRows <= 0:
        return []
    #initiate first node of triangle always 1
    triangle = [[1]]
    #loop to generate second row to end row (numRows)
    for i in range(1, numRows):
        #variable initialize the prior row as increment minus 1
        prev_row = triangle[i - 1]
        #variable initialize the new row starting with 1 always
        new_row = [1]
        #loop through previous row elements except last
        for j in range(1, len(prev_row)):
            #calculate new elements by adding adjacent previous elements
            new_row.append(prev_row[j - 1] + prev_row[j])
            #add 1 to the end cap of row
        new_row.append(1)
        #add newly generated row into the triangle
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