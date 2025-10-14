"""
Longest Increasing Subsequence (LIS)
Description:
Finds the length and actual longest increasing subsequence of a list of integers.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from bisect import bisect_left


def longest_increasing_subsequence(nums: list) -> tuple:
    """
    Returns the length and the actual longest strictly increasing subsequence.

    Args:
        nums: List of integers to analyze.

    Returns:
        A tuple of two elements:
        - int: length of the longest increasing subsequence
        - list: the actual longest increasing subsequence
    """
    if not nums:
        return 0, []

    sub = []  # smallest tail for subsequences of each length
    parent = [None] * len(nums)  # for reconstructing the LIS
    sub_idx = []  # indices of the current smallest tails

    for i, x in enumerate(nums):
        pos = bisect_left(sub, x)
        if pos == len(sub):
            sub.append(x)
            sub_idx.append(i)
        else:
            sub[pos] = x
            sub_idx[pos] = i

        # track predecessors
        if pos != 0:
            parent[i] = sub_idx[pos - 1]

    # Reconstruct LIS
    lis = []
    k = sub_idx[-1] if sub_idx else None
    while k is not None:
        lis.append(nums[k])
        k = parent[k]
    lis.reverse()

    return len(sub), lis


def run_tests():
    """Run sample test cases for LIS."""
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], (4, [2, 3, 7, 101])),
        ([0, 1, 0, 3, 2, 3], (4, [0, 1, 2, 3])),
        ([7, 7, 7, 7, 7], (1, [7])),
        ([1, 2, 3, 4, 5], (5, [1, 2, 3, 4, 5])),
        ([5, 4, 3, 2, 1], (1, [5])),
    ]

    print("\nRunning sample test cases...\n")
    for arr, expected in test_cases:
        length, subseq = longest_increasing_subsequence(arr)
        print(f"Input: {arr}")
        print(f"Expected Length: {expected[0]}, Got: {length}")
        print(f"Expected LIS: {expected[1]}, Got: {subseq}\n")


if __name__ == "__main__":
    print("Choose mode:")
    print("1. User Input Mode")
    print("2. Run Sample Tests")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        n = int(input("\nEnter number of elements: ").strip())
        arr = list(map(int, input(f"Enter {n} integers separated by space:\n").split()))
        length, subseq = longest_increasing_subsequence(arr)
        print(f"\nLength of Longest Increasing Subsequence: {length}")
        print(f"Longest Increasing Subsequence: {subseq}")

    elif choice == "2":
        run_tests()
    else:
        print("Invalid choice. Please enter 1 or 2.")
