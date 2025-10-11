"""
Binary Search Tree (BST) Implementation in Python.
A BST is a node-based binary tree data structure which has the following properties:
The left subtree of a node contains only nodes with keys lesser than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
The left and right subtree each must also be a binary search tree.

Time Complexity (Average Case):

Search: O(log n)
Insert: O(log n)

Time Complexity (Worst Case - skewed tree):

Search: O(n)
Insert: O(n)

Space Complexity: O(h), where h is the height of the tree.
(h is O(log n) on average, and O(n) in the worst case).
"""

class Node:
    """
    A Node in a Binary Search Tree.
    Each node stores:
    - key: the value of the node
    - left: reference to the left child
    - right: reference to the right child
    """
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation.
    Properties:
    - Left subtree has keys < node's key
    - Right subtree has keys > node's key
    Supports insert, search, and in-order traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, key: int) -> None:
        """
        Inserts a new key into the BST.

        Args:
            key (int): The key to insert.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node: Node, key: int) -> None:
        """Helper function to insert recursively."""
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        # If key == current_node.key, do nothing (no duplicates in BST)

    def search(self, key: int) -> bool:
        """
        Searches for a key in the BST.

        Args:
            key (int): The key to search.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node: Node, key: int) -> bool:
        """Helper function to search recursively."""
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    def in_order(self) -> list:
        """
        Performs in-order traversal of the BST.
        (Left → Root → Right)

        Returns:
            list: A list of keys in sorted order.
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, current_node: Node, result: list) -> None:
        """Helper function to perform in-order traversal recursively."""
        if current_node is not None:
            self._in_order_recursive(current_node.left, result)
            result.append(current_node.key)
            self._in_order_recursive(current_node.right, result)


# -------------------------------
# Runnable example block
# -------------------------------
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert some nodes
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)

    print("In-order Traversal:", bst.in_order())  
    # Output: [20, 30, 40, 50, 60, 70, 80]

    print("Search 40:", bst.search(40))  # True
    print("Search 90:", bst.search(90))  # False


"""
📌 How the BST is built for [50, 30, 70, 20, 40, 60, 80]

          50
         /  \
       30    70
      / \    / \
    20  40  60  80

✔ Insert 50 → becomes root
✔ Insert 30 → goes to left of 50
✔ Insert 70 → goes to right of 50
✔ Insert 20 → left of 30
✔ Insert 40 → right of 30
✔ Insert 60 → left of 70
✔ Insert 80 → right of 70

In-order Traversal → [20, 30, 40, 50, 60, 70, 80] ✅ (sorted order)
"""
