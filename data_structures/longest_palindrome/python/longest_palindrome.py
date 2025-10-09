"""
Time Complexity: O(n^2)
- We expand around each character (and each pair of characters) to check for palindromes.
- For each center, expansion takes O(n) time in the worst case, and we do this for 2n-1 centers.

Space Complexity: O(1)
- No extra space used except a few pointers for tracking indices.
"""


def longest_palindrome(s: str) -> str:


    if not s or len(s) == 1:
        return s

    start, end = 0, 0

    def expand_around_center(left: int, right: int) -> int:

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Subtract overshoot

    for i in range(len(s)):
        len1 = expand_around_center(i, i)  # Odd-length palindrome
        len2 = expand_around_center(i, i + 1)  # Even-length palindrome
        max_len = max(len1, len2)

        if max_len > (end - start):
            # Update the start and end pointers
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


# 🧪 Runnable Example Block
def main():
    test_cases = [
        "babad",  # Expected: "bab" or "aba"
        "cbbd",  # Expected: "bb"
        "a",  # Expected: "a"
        "ac",  # Expected: "a" or "c"
        "",  # Expected: ""
        "racecar",  # Expected: "racecar"
    ]

    for s in test_cases:
        result = longest_palindrome(s)
        print(f"Input: '{s}' | Longest Palindromic Substring: '{result}'")


if __name__ == "__main__":
    main()
