"""
move_zeroes.py

A Python program to move all zeroes in a list to the end
while keeping the order of the other (non-zero) elements the same.

This operation is done in-place, meaning we modify the same list
instead of creating a new one.

Author: @uptouplaksh
Date: 2025-10-09
"""

def move_zeroes(nums):
    """
    Moves all zeros in the given list to the end, in-place.

    Parameters:
        nums (list): A list of integers (can contain zeros and non-zeros)

    Returns:
        None: The list is modified directly (no new list is returned)
    """

    # Imagine we have to push all zeroes to the back of the list
    # but we cannot use extra space (like making a new list).
    # So we’ll do it in-place using one pointer.

    # 'insert_pos' will keep track of the position
    # where the next non-zero element should go.
    insert_pos = 0

    # Loop through the list from start to end
    for i in range(len(nums)):
        # If the current element is NOT zero,
        # we place it at the current 'insert_pos' and move the pointer ahead.
        if nums[i] != 0:
            # Swap the non-zero element to its correct position.
            # If 'i' and 'insert_pos' are the same, this swap does nothing.
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]

            # Move the 'insert_pos' forward for the next non-zero element.
            insert_pos += 1

    # When the loop finishes, all non-zero numbers are shifted to the front,
    # and all zeros are automatically moved to the back of the list.

    # Note: We don’t need to return anything since we’re modifying the list itself.


if __name__ == "__main__":
    # Below are a few example cases to help you understand how the code works.

    print("---- Example 1 ----")
    # Input list contains zeroes in between
    arr1 = [0, 1, 0, 3, 12]
    print("Before moving zeroes:", arr1)
    move_zeroes(arr1)
    print("After moving zeroes: ", arr1)
    print()

    print("---- Example 2 ----")
    # Input list with all zeroes at the start
    arr2 = [0, 0, 0, 1]
    print("Before moving zeroes:", arr2)
    move_zeroes(arr2)
    print("After moving zeroes: ", arr2)
    print()

    print("---- Example 3 ----")
    # Input list with no zeroes at all
    arr3 = [4, 5, 6]
    print("Before moving zeroes:", arr3)
    move_zeroes(arr3)
    print("After moving zeroes: ", arr3)
    print()

    print("---- Example 4 ----")
    # A mixed case with zeroes spread across the list
    arr4 = [0, 2, 0, 0, 5, 7, 0, 8]
    print("Before moving zeroes:", arr4)
    move_zeroes(arr4)
    print("After moving zeroes: ", arr4)
    print()

    print("---- Example 5 ----")
    # All elements are zero
    arr5 = [0, 0, 0, 0]
    print("Before moving zeroes:", arr5)
    move_zeroes(arr5)
    print("After moving zeroes: ", arr5)
    print()

"""
🧠 Explanation Summary:
-----------------------
1️⃣ We maintain a pointer (insert_pos) to decide where to put the next non-zero.
2️⃣ We scan each element:
    - If non-zero → swap it to insert_pos, move insert_pos forward.
    - If zero → skip it.
3️⃣ At the end, all non-zeros are in front, and all zeros move behind automatically.

⏱ Time Complexity: O(n)
   → We visit each element once.

💾 Space Complexity: O(1)
   → We don't use extra memory (operation is done in-place).
"""
