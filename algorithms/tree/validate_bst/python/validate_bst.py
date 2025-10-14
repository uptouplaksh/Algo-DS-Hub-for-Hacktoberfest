"""
Module: validate_bst
--------------------
This module provides a function to validate whether a given binary tree
is a valid Binary Search Tree (BST) using a recursive approach with
min/max constraints.

A BST satisfies the property that for every node:
- All values in the left subtree are smaller than the node's value.
- All values in the right subtree are greater than the node's value.
"""

from __future__ import annotations
from typing import Optional


class TreeNode:
    """
    Definition of a binary tree node.

    Attributes:
        val (int): The value of the node.
        left (Optional[TreeNode]): Pointer to the left child.
        right (Optional[TreeNode]): Pointer to the right child.
    """

    def __init__(self, val: int, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode], min_val: float = float("-inf"), max_val: float = float("inf")) -> bool:
    """
    Recursively checks if a binary tree is a valid BST.

    Args:
        root (Optional[TreeNode]): The root node of the binary tree.
        min_val (float): The minimum allowed value for the current node.
        max_val (float): The maximum allowed value for the current node.

    Returns:
        bool: True if the tree is a valid BST, False otherwise.

    Time Complexity:
        O(n) — each node is visited once.
    Space Complexity:
        O(h) — recursion stack, where h is the height of the tree.
    """
    if root is None:
        return True

    if not (min_val < root.val < max_val):
        return False

    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)


if __name__ == "__main__":
    # Example usage
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)

    print("Is the given tree a valid BST?", is_valid_bst(root))
