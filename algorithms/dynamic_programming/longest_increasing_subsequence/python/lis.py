"""
Longest Increasing Subsequence (LIS) - O(n log n) implementation

Description:
    Finds the length of the Longest Increasing Subsequence (LIS)
    in a given list of integers.

    Supports two modes:
    1. User input (interactive)
    2. Test mode (predefined examples)
"""

from bisect import bisect_left
from typing import List, Tuple


def longest_increasing_subsequence(nums: List[int]) -> Tuple[int, List[int]]:
    """
    Returns the length and the actual longest strictly increasing subsequence.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0, []

    sub = []  # smallest tail for increasing subsequences of each length
    sub_indices = []  # stores indices in original array
    parent = [-1] * len(nums)  # to reconstruct LIS

    for i, x in enumerate(nums):
        idx = bisect_left(sub, x)
        if idx == len(sub):
            sub.append(x)
            sub_indices.append(i)
        else:
            sub[idx] = x
            sub_indices[idx] = i

        if idx != 0:
            parent[i] = sub_indices[idx - 1]

    # Reconstruct LIS
    lis = []
    k = sub_indices[-1]
    while k != -1:
        lis.append(nums[k])
        k = parent[k]
    lis.reverse()

    return len(sub), lis


def run_tests() -> None:
    """Run a few sample test cases."""
    print("\nRunning sample test cases...\n")

    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
    ]

    for arr, expected_len in test_cases:
        result_len, result_seq = longest_increasing_subsequence(arr)
        print(
            f"Input: {arr}\nExpected length: {expected_len}, "
            f"Got length: {result_len}, LIS: {result_seq}\n"
        )


def user_input_mode() -> None:
    """Interactive mode to read numbers from the user."""
    print("\nEnter number of elements in the sequence:")
    n = int(input().strip())

    print(f"Enter {n} integers separated by space:")
    arr = list(map(int, input().strip().split()))

    length, sequence = longest_increasing_subsequence(arr)
    print(f"\nLength of Longest Increasing Subsequence: {length}")
    print(f"Longest Increasing Subsequence: {sequence}")


if __name__ == "__main__":
    print("Choose mode:")
    print("1. User Input Mode")
    print("2. Run Sample Tests")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        user_input_mode()
    elif choice == "2":
        run_tests()
    else:
        print("Invalid choice. Please enter 1 or 2.")
