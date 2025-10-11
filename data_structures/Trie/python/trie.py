"""
Trie (Prefix Tree) Implementation in Python.
A Trie is a tree-like data structure that stores a dynamic set of strings, usually for retrieval by prefix.
Each node represents a character of a word. Words are inserted character by character, which allows for efficient prefix searches.
Time Complexity (Average Case):
Insert: O(L), where L is the length of the word
Search: O(L)
Starts with: O(P), where P is the length of the prefix

Space Complexity: O(N * L), where N is the number of words and L is the average length of the words.
"""

class TrieNode:
    """
    A node in the Trie.
    Each node stores:
    - children: a dictionary mapping characters to child TrieNodes
    - is_end_of_word: boolean indicating if the node is the end of a valid word
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    Trie (Prefix Tree) implementation.
    Supports insert, search, and prefix-matching (starts_with).
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
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a complete word in the Trie.

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

# -------------------------------
# Runnable example block
# -------------------------------
if __name__ == "__main__":
    trie = Trie()

    # Insert some words
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
