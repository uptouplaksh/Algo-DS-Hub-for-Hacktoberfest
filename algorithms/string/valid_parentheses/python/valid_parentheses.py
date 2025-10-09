# File: algorithms/string/valid_parentheses/python/valid_parentheses.py

def is_valid_parentheses(s: str) -> bool:
    """
    Check if the input string of parentheses is valid.
    
    A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.

    Args:
        s (str): Input string containing '(', ')', '{', '}', '[' and ']'

    Returns:
        bool: True if string is valid, False otherwise

    Approach:
    - Use a stack to keep track of opening brackets.
    - When a closing bracket is encountered:
        - If the stack is empty or top of stack doesn't match, the string is invalid.
        - Otherwise, pop the matching opening bracket from the stack.
    - At the end, the stack must be empty for the string to be valid.

    Time Complexity: O(n), where n is the length of the string.
        - Each character is pushed and popped at most once.
    Space Complexity: O(n), in the worst case all characters are opening brackets.
    """
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            # Opening bracket: push onto the stack
            stack.append(char)
        elif char in bracket_map:
            # Closing bracket: check if it matches top of stack
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # Pop the matched opening bracket
        else:
            # Invalid character (not part of problem constraints)
            return False

    # If stack is empty, all brackets matched correctly
    return len(stack) == 0


# -------------------------------
# Runnable example block
# -------------------------------
if __name__ == "__main__":
    # Test cases: each tuple contains (input_string, expected_output)
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([{}])", True),
        ("([)]", False),
        ("", True),
        ("{[()()]}", True),
        ("{[(])}", False)
    ]

    print("Testing valid parentheses function:\n")
    for s, expected in test_cases:
        result = is_valid_parentheses(s)
        print(f"is_valid_parentheses('{s}') = {result} | Expected = {expected}")
