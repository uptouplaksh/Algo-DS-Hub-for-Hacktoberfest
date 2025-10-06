# algorithms/tree/max_depth/python/max_depth.py

class Node:
    """Binary Tree Node class."""
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(node):
    """
    Recursively computes the maximum depth (height) of a binary tree.

    Args:
        node (Node): Root node of the binary tree.

    Returns:
        int: Maximum depth of the tree. Empty tree has depth 0.

    Time Complexity: O(n) where n is the number of nodes in the tree.
    Space Complexity: O(h) where h is the height of the tree (due to recursion stack).
    """
    # Base case: if the node is None, tree (or subtree) is empty; depth is 0
    if node is None:
        return 0
    # Recursively find max depth of left and right subtrees, then add 1 for current node
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    return 1 + max(left_depth, right_depth)

# ---- Runnable Example Block ----
# ----Remove it in case of general use as a module----
if __name__ == "__main__":
    # Build a simple binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    #    /
    #   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(6)

    print("Maximum Depth of the Binary Tree:", max_depth(root))
    # Expected Output: Maximum Depth of the Binary Tree: 4
