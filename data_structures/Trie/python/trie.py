"""
Trie (Prefix Tree) implementation in Python.

Implements:
 - insert(word)        : inserts a word into the Trie
 - search(word)        : checks if a full word exists in the Trie
 - starts_with(prefix) : checks if any word in the Trie starts with the given prefix

Usage:
  Place this file as instructed and run:
    python trie.py
  It will run a small example and print outputs.

Complexity:
 - Insert: O(L)       where L is the length of the word
 - Search: O(L)       where L is the length of the word
 - Starts with: O(P)  where P is the length of the prefix
"""
# (No invalid escape sequences present.)

class TrieNode:
    """
    A TrieNode represents each character node in the Trie.
    Each node stores:
    - children: a dictionary mapping characters to TrieNodes
    - is_end_of_word: boolean to mark the end of a valid word
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Trie (Prefix Tree) implementation.
    Supports insertion of words, search for full words, and prefix matching.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        Args:
            word (str): The word to insert.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Searches for a full word in the Trie.

        Args:
            word (str): The word to search.

        Returns:
            bool: True if the word exists, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given prefix.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if any word starts with the prefix, False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("bat")

    print("Search 'apple':", trie.search("apple"))      # True
    print("Search 'app':", trie.search("app"))          # True
    print("Search 'appl':", trie.search("appl"))        # False
    print("Starts with 'ap':", trie.starts_with("ap"))  # True
    print("Starts with 'ba':", trie.starts_with("ba"))  # True
    print("Starts with 'cat':", trie.starts_with("cat"))  # False


"""
📌 How the Trie is built for ["apple", "app", "bat"]

(START)
⬇
root
├── 'a'
│     └── 'p'
│          └── 'p' (end of "app")
│               └── 'l'
│                    └── 'e' (end of "apple")
│
└── 'b'
        └── 'a'
            └── 't' (end of "bat")

✔ "app" ends at the second 'p'
✔ "apple" continues further down to 'e'
✔ "bat" starts a new branch from 'b'
"""

# 🔹 Trie Use Cases in DSA (Short Version)

# 1. Prefix Queries
# - Count or find words starting with a given prefix
# Example: starts_with("pre")

# 2. Autocomplete / Suggestions
# - Return all words starting with a prefix
# Example: search suggestions in IDE or search engines

# 3. Longest Common Prefix
# - Find the longest prefix among a list of strings
# Example: ["flower","flow","flight"] -> "fl"

# 4. Word Search in 2D Grid
# - Check if words from a dictionary exist in a grid
# Example: Leetcode Word Search II, Boggle game

# 5. Count Unique Substrings
# - Build Trie with all suffixes to count unique substrings

# 6. Max XOR / Bitwise Problems
# - Store binary of numbers to compute maximum XOR efficiently

# 7. Spell Checker / Dictionary Validation
# - Check word existence or suggest corrections

# 8. Compression / String Matching
# - Efficient storage and search for large dictionaries
