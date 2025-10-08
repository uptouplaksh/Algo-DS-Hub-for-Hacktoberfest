def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    A palindrome reads the same forwards and backwards.
    This function ignores case and non-alphanumeric characters.

    Parameters:
        s (str): Input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Example:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("Hello")
        False
    """

    # Step 1: Filter out non-alphanumeric characters and convert to lowercase
    cleaned = ""
    for char in s:
        if char.isalnum():          # Keep only letters and digits
            cleaned += char.lower()  # Convert to lowercase

    # Step 2: Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]


# ------------------ RUNNABLE EXAMPLE ------------------
if __name__ == "__main__":
    test_strings = [
        "A man, a plan, a canal: Panama",
        "Hello",
        "No lemon, no melon"
    ]

    for text in test_strings:
        if is_palindrome(text):
            print(f"'{text}' -> Palindrome")
        else:
            print(f"'{text}' -> Not a palindrome")


"""  
    output:-
    
    'A man, a plan, a canal: Panama' -> Palindrome
    'Hello' -> Not a palindrome
    'No lemon, no melon' -> Palindrome

""" 

"""
------------------ COMPLEXITY ANALYSIS ------------------
Let n be the length of the input string.

Time Complexity:
    O(n)
    - We loop through the string once to clean it, and once to reverse it.

Space Complexity:
    O(n)
    - The cleaned string and its reverse both require O(n) space.
---------------------------------------------------------
"""
