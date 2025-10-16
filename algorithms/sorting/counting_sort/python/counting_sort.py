"""
Counting Sort Algorithm Implementation in Python

Description:
Counting Sort is a non-comparison-based sorting algorithm that works efficiently 
for sorting integers within a known, limited range. It counts the occurrences 
of each unique element and uses this count to place the elements in sorted order.

Time Complexity:
- Best Case: O(n + k)
- Average Case: O(n + k)
- Worst Case: O(n + k)
(where n = number of elements, k = range of input values)

Space Complexity: O(n + k)
"""

def counting_sort(arr):
    """
    Function to perform Counting Sort on an integer array.
    """
    if not arr:
        return arr  # handle empty list case

    # Step 1: Find the maximum and minimum values in the array
    max_val = max(arr)
    min_val = min(arr)

    # Step 2: Initialize the count array
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements

    # Step 3: Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Step 4: Compute cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Place elements into the output array in sorted order
    output = [0] * len(arr)
    for num in reversed(arr):  # reversed for stable sorting
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Step 6: Copy sorted elements back to original array
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr


# ------------------------- RUNNABLE EXAMPLE -------------------------
if __name__ == "__main__":
    print("Counting Sort Algorithm Example\n")

    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Original Array:", arr)

    sorted_arr = counting_sort(arr)
    print("Sorted Array:", sorted_arr)
