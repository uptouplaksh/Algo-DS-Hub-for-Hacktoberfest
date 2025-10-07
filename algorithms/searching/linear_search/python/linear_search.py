#
# Linear Search Algorithm in Python
#

# Time Complexity: O(n) - In the worst case, we have to scan the entire list.
# Space Complexity: O(1) - No extra space is needed.
#

def linear_search(arr, target):
    """
    Finds the index of a target element in an array using Linear Search.

    Args:
        arr: A list of elements.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target was found
    return -1  # Return -1 if the target is not in the list


# Example Usage:
if __name__ == "__main__":
    sample_array = [10, 50, 30, 70, 80, 20, 90, 40]
    search_target = 20

    result = linear_search(sample_array, search_target)

    if result != -1:
        print(f"Element {search_target} is present at index {result}")
    else:
        print(f"Element {search_target} is not present in the array")