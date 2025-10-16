"""
Checks if a string of parentheses (brackets) is valid.

A string is considered valid if:
- Every opening bracket has a corresponding closing bracket of the same type.
- Brackets are closed in the correct order (i.e., properly nested).

Example:
    Input: "([{}])"
    Output: True

Approach:
    We use a stack to keep track of opening brackets.
    - When we encounter an opening bracket, we push it onto the stack.
    - When we encounter a closing bracket, we check whether it matches the
      top element of the stack (the most recent opening bracket).
    - If it matches, we pop the stack; otherwise, the string is invalid.

Time Complexity: O(n)
    We traverse the string once, performing constant-time operations per character.
Space Complexity: O(n)
    In the worst case (all opening brackets), we store all characters in the stack.
"""


def is_valid_parentheses(s: str) -> bool:
    """
    Determines whether the given string of parentheses is valid.

    Args:
        s (str): The input string consisting of characters '(', ')', '{', '}', '[' and ']'.

    Returns:
        bool: True if the parentheses string is valid, False otherwise.

    Example:
        >>> is_valid_parentheses("()[]{}")
        True
        >>> is_valid_parentheses("(]")
        False
    """

    # Stack to store opening brackets as they appear
    stack = []

    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            # Opening bracket → push onto stack
            stack.append(char)
        elif char in bracket_map:
            # Closing bracket → check if top of stack matches
            if not stack:
                # No opening bracket to match
                return False
            if stack[-1] != bracket_map[char]:
                # Mismatched bracket type
                return False
            stack.pop()  # Matched pair, remove top element
        else:
            # Ignore any non-bracket characters (not required for this problem)
            continue

    # Valid if no unmatched opening brackets remain
    return len(stack) == 0


if __name__ == "__main__":
    # -------------------------------
    # Runnable Example Block
    # -------------------------------

    print("Testing Valid Parentheses Function\n" + "-" * 40)

    # Test cases: (input_string, expected_output)
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([{}])", True),
        ("([)]", False),
        ("", True),  # Empty string is valid
        ("{[()()]}", True),
        ("{[(])}", False),
        ("(", False),  # Unmatched opening bracket
        ("}", False)   # Unmatched closing bracket
    ]

    # Run each test and display results clearly
    for s, expected in test_cases:
        result = is_valid_parentheses(s)
        status = "✅ PASSED" if result == expected else "❌ FAILED"
        print(f"{status}: is_valid_parentheses('{s}') → {result} (Expected: {expected})")
