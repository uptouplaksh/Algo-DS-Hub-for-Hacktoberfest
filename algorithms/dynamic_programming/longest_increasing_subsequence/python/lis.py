# algorithms/dynamic_programming/longest_increasing_subsequence.py

"""
Longest Increasing Subsequence (LIS) - O(n log n) implementation

Description:
    This program finds the length of the Longest Increasing Subsequence (LIS)
    in a given list of integers.

    It supports two modes:
    1. User input (interactive): Reads numbers from the console.
    2. Test mode (when imported or run with test flag): Runs predefined examples.

Example (User Input):
    Input:
        8
        10 9 2 5 3 7 101 18
    Output:
        Length of Longest Increasing Subsequence: 4
"""

from bisect import bisect_left


def longest_increasing_subsequence(nums):
    """
    Returns the length of the longest strictly increasing subsequence.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0

    sub = []  # holds the smallest tail for increasing subsequences of each length

    for x in nums:
        i = bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return len(sub)


def run_tests():
    """Run a few sample test cases."""
    print("\nRunning sample test cases...\n")

    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
    ]

    for arr, expected in test_cases:
        result = longest_increasing_subsequence(arr)
        print(f"Input: {arr}\nExpected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    print("Choose mode:")
    print("1. User Input Mode")
    print("2. Run Sample Tests")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print("\nEnter number of elements in the sequence:")
        n = int(input().strip())

        print(f"Enter {n} integers separated by space:")
        arr = list(map(int, input().strip().split()))

        result = longest_increasing_subsequence(arr)
        print(f"\nLength of Longest Increasing Subsequence: {result}")

    elif choice == "2":
        run_tests()
    else:
        print("Invalid choice. Please enter 1 or 2.")
