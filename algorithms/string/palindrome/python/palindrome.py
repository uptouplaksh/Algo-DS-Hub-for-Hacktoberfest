"""
Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

Time Complexity: O(n)
- The cleaning process iterates through the string once.
- The reversal/comparison also takes O(n) time.

Space Complexity: O(n)
- A new 'cleaned' string is created, which can be up to n characters long.
"""

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.
    A palindrome reads the same forwards and backwards.
    This function ignores case and non-alphanumeric characters.

    Args:
        s (str): Input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("Hello")
        False
    """

    # Step 1: A more efficient and Pythonic way to filter and clean the string.
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Step 2: Check if the cleaned string equals its reverse.
    return cleaned == cleaned[::-1]


# ------------------ RUNNABLE EXAMPLE ------------------
if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal: Panama",
        "Hello",
        "No lemon, no melon",
        "race a car" # A good false case
    ]

    print("Palindrome Check Example:\n")
    for text in test_strings:
        if is_palindrome(text):
            print(f"'{text}' -> Palindrome")
        else:
            print(f"'{text}' -> Not a palindrome")
