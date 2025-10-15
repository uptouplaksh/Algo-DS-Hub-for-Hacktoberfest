"""
Module: validate_bst
--------------------
This module provides a function to determine if a given binary tree is a valid
Binary Search Tree (BST).

A Binary Search Tree (BST) is a binary tree in which for every node:
- The value of all nodes in the left subtree is less than the node’s value.
- The value of all nodes in the right subtree is greater than the node’s value.

Algorithm:
----------
This implementation uses a recursive approach that passes down minimum and
maximum constraints for each node. If a node violates the constraint, the
tree is not a valid BST.

Complexity Analysis:
--------------------
Time Complexity: O(n), where n is the number of nodes in the tree.
Each node is visited once.
Space Complexity: O(h), where h is the height of the tree.
The space is used by the recursion stack.
"""


class TreeNode:
    """Class representing a node in a binary tree."""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    """
    Recursively checks if the binary tree rooted at `node` is a valid BST.

    Args:
        node (TreeNode): Current node being validated.
        min_val (float): Minimum allowed value for this subtree.
        max_val (float): Maximum allowed value for this subtree.

    Returns:
        bool: True if the subtree is a valid BST, otherwise False.
    """
    if node is None:
        return True

    if not (min_val < node.val < max_val):
        return False

    return (
        is_valid_bst(node.left, min_val, node.val)
        and is_valid_bst(node.right, node.val, max_val)
    )


if __name__ == "__main__":
    # Example 1: Valid BST
    root_valid = TreeNode(10)
    root_valid.left = TreeNode(5)
    root_valid.right = TreeNode(15)
    root_valid.left.left = TreeNode(2)
    root_valid.left.right = TreeNode(7)

    print("Valid BST check (should be True):", is_valid_bst(root_valid))

    # Example 2: Invalid BST
    root_invalid = TreeNode(10)
    root_invalid.left = TreeNode(5)
    root_invalid.right = TreeNode(8)  # Invalid: right child < root

    print("Invalid BST check (should be False):", is_valid_bst(root_invalid))

