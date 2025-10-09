"""
group_anagrams.py

This module provides a function to group words that are anagrams of each other.

Anagrams are words that contain the same characters in different orders.
For example: "eat", "tea", and "ate" are all anagrams of each other.

Algorithm Used:
    Hash Map (Dictionary) based grouping using sorted character tuples as keys.

Time Complexity: O(n * k log k)
    - n: Number of strings
    - k: Maximum length of a string
Space Complexity: O(n * k)
"""

from collections import defaultdict

def group_anagrams(words):
    """
    Groups a list of words into lists of anagrams.

    Args:
        words (list[str]): A list of strings.

    Returns:
        list[list[str]]: A list of lists, where each inner list contains words
                         that are anagrams of each other.
    """
    anagram_map = defaultdict(list)

    # Create a mapping where sorted tuple of characters is the key
    for word in words:
        sorted_word = tuple(sorted(word))  # e.g., "eat" -> ('a', 'e', 't')
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


# Example usage
if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input words:", words)
    grouped = group_anagrams(words)
    print("Grouped anagrams:", grouped)
