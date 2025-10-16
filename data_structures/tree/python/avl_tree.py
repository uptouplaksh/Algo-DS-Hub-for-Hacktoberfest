from __future__ import annotations

import doctest


class AVLNode:
    """A node structure for an AVL Tree."""

    def __init__(self, key: int):
        self.key: int = key
        self.height: int = 1
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None


class AVLTree:
    """
    A self-balancing Binary Search Tree (BST) where the difference between
    heights of left and right subtrees (the balance factor) cannot be more
    than one for all nodes.

    Time Complexity Analysis:
    - Search: O(log n)
    - Insert: O(log n)
    - Delete: O(log n)
    """

    def __init__(self):
        self.root: AVLNode | None = None

    def _get_height(self, node: AVLNode | None) -> int:
        """Helper function to get the height of a node or 0 if None."""
        return node.height if node else 0

    def _get_balance(self, node: AVLNode | None) -> int:
        """Helper function to get the balance factor of a node."""
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _update_height(self, node: AVLNode) -> None:
        """Helper function to update the height of a node after rotation/insertion."""
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _right_rotate(self, y: AVLNode) -> AVLNode:
        """
        Perform a right rotation (LL case).

        Args:
            y: The root node of the subtree to rotate.

        Returns:
            The new root node of the rotated subtree.
        """
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        return x

    def _left_rotate(self, x: AVLNode) -> AVLNode:
        """
        Perform a left rotation (RR case).

        Args:
            x: The root node of the subtree to rotate.

        Returns:
            The new root node of the rotated subtree.
        """
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        return y

    def _balance_node(self, root: AVLNode, balance: int) -> AVLNode:
        """
        Balance the node based on the balance factor.

        Args:
            root: The current node to balance.
            balance: The balance factor of the node.

        Returns:
            The new root node after balancing.
        """
        # Case 1: Left Left (LL)
        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)

        # Case 2: Right Right (RR)
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)

        # Case 3: Left Right (LR)
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Case 4: Right Left (RL)
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def insert(self, root: AVLNode | None, key: int) -> AVLNode:
        """
        Recursively inserts a key and performs rotations if the tree becomes unbalanced.

        Args:
            root: The current root of the subtree.
            key: The value to insert.

        Returns:
            The new root node of the subtree.

        >>> avl = AVLTree()
        >>> avl.root = avl.insert(avl.root, 10)
        >>> avl.root = avl.insert(avl.root, 20)
        >>> avl.root = avl.insert(avl.root, 30) # RR Case, 20 becomes new root
        >>> avl.root.key
        20
        >>> avl.root.left.key
        10
        >>> avl.root.right.key
        30
        >>> avl.root = avl.insert(avl.root, 25) # Insert 25
        >>> avl.root = avl.insert(avl.root, 7)
        >>> avl.root.key
        20
        """
        # 1. Standard BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update height of current node
        self._update_height(root)

        # 3. Get the balance factor
        balance = self._get_balance(root)

        # 4. Balance the node
        return self._balance_node(root, balance)

    def _get_min_value_node(self, node: AVLNode) -> AVLNode:
        """Finds the node with the minimum key value in a subtree."""
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, root: AVLNode | None, key: int) -> AVLNode | None:
        """
        Recursively deletes a key and performs rotations if the tree becomes unbalanced.

        Args:
            root: The current root of the subtree.
            key: The value to delete.

        Returns:
            The new root node of the subtree.

        >>> avl = AVLTree()
        >>> keys = [30, 20, 40, 10, 25, 50]
        >>> for k in keys:
        ...     avl.root = avl.insert(avl.root, k)
        >>> avl.root = avl.delete(avl.root, 10) # Delete a leaf node (10)
        >>> avl.root.left.left # Check if 10 is gone
        >>> avl.root = avl.delete(avl.root, 40) # Delete 40 (RR case in balancing)
        >>> avl.root.key
        25
        """
        # 1. Standard BST deletion
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # If the tree had only one node, return the root.
        if not root:
            return root

        # 2. Update height of current node
        self._update_height(root)

        # 3. Get the balance factor
        balance = self._get_balance(root)

        # 4. Balance the node
        return self._balance_node(root, balance)


# --- Runnable Example Block ---

def in_order_traversal(root: AVLNode | None, result: list[int]):
    """Helper function to verify the tree structure."""
    if root:
        in_order_traversal(root.left, result)
        result.append(root.key)
        in_order_traversal(root.right, result)


if __name__ == "__main__":
    # Run doctests for automated verification
    doctest.testmod()

    # Create an AVL Tree and test insertion with rotations
    avl_tree = AVLTree()
    keys_to_insert = [10, 20, 30, 40, 50, 25]

    print("--- Inserting Keys ---")
    for key in keys_to_insert:
        avl_tree.root = avl_tree.insert(avl_tree.root, key)
        print(f"Inserted {key}. Root is now: {avl_tree.root.key if avl_tree.root else 'None'}")

    # Verify In-Order Traversal (should be sorted)
    sorted_keys = []
    in_order_traversal(avl_tree.root, sorted_keys)
    print("\nIn-Order Traversal (Sorted Keys):", sorted_keys)
    print(f"Final Root: {avl_tree.root.key}")
    print(f"Final Root Balance Factor: {avl_tree._get_balance(avl_tree.root)}")

    # Test Deletion
    key_to_delete = 20
    print(f"\n--- Deleting Key: {key_to_delete} ---")
    avl_tree.root = avl_tree.delete(avl_tree.root, key_to_delete)

    # Verify new In-Order Traversal
    new_sorted_keys = []
    in_order_traversal(avl_tree.root, new_sorted_keys)
    print("In-Order Traversal after deletion:", new_sorted_keys)
    print(f"New Root: {avl_tree.root.key if avl_tree.root else 'None'}")
