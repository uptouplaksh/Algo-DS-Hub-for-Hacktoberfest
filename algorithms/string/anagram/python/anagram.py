"""
Anagram Checker (implementation in python)

Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for storing sorted strings
"""

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters
    exactly once. This function ignores spaces and is case-insensitive.
    
    Args:
        str1 (str): The first string.
        str2 (str): The second string.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """

    # To remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Different lengths can't be anagrams
    if len(str1) != len(str2):
        return False
    
    # Compare sorted strings
    return sorted(str1) == sorted(str2)


def main():
    """Run test cases"""
    
    print("Anagram Checker Examples")
    print("-" * 40)
    
    # Test 1: Basic anagram
    print("\nTest 1: listen vs silent")
    print(f"Result: {is_anagram('listen', 'silent')}")
    
    # Test 2: Not anagrams
    print("\nTest 2: hello vs world")
    print(f"Result: {is_anagram('hello', 'world')}")
    
    # Test 3: Case insensitive
    print("\nTest 3: Triangle vs Integral")
    print(f"Result: {is_anagram('Triangle', 'Integral')}")
    
    # Test 4: With spaces
    print("\nTest 4: conversation vs 'voices rant on'")
    print(f"Result: {is_anagram('conversation', 'voices rant on')}")
    
    # Test 5: Empty strings
    print("\nTest 5: empty strings")
    print(f"Result: {is_anagram('', '')}")


if __name__ == "__main__":
    main()
