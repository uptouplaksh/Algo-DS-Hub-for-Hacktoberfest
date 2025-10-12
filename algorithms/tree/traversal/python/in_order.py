"""
Algorithm: In-order Traversal of a Binary Tree (Left -> Root -> Right)

Description:
In-order traversal is a depth-first traversal technique for binary trees.
It first visits the left subtree, then the root node, and finally the right subtree.
This traversal is commonly used for binary search trees (BSTs) to retrieve nodes in sorted order.

Approach:
1. Recursive Solution:
   - Base case: If the node is None, return.
   - Recursively traverse the left subtree.
   - Visit (print/store) the current node.
   - Recursively traverse the right subtree.

2. Iterative Solution (using stack):
   - Use a stack to simulate the recursive behavior.
   - Traverse down to the leftmost node, pushing nodes onto the stack.
   - Pop nodes from the stack, process them, and move to the right subtree.

Time Complexity:
- O(n): Each node is visited exactly once.

Space Complexity:
- Recursive: O(h) where h is the height of the tree (due to recursion stack).
- Iterative: O(h) due to explicit stack usage.
"""

# ----------------------------
# Definition for a binary tree node
# ----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ----------------------------
# Recursive In-order Traversal
# ----------------------------
def inorder_recursive(root):
    """Performs in-order traversal recursively."""
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result


# ----------------------------
# Iterative In-order Traversal
# ----------------------------
def inorder_iterative(root):
    """Performs in-order traversal iteratively using a stack."""
    result, stack = [], []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    """
    Example Binary Tree:
            1
           / \
          2   3
         / \
        4   5
    Expected In-order Traversal: [4, 2, 5, 1, 3]
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("In-order Traversal (Recursive):", inorder_recursive(root))
    print("In-order Traversal (Iterative):", inorder_iterative(root))
