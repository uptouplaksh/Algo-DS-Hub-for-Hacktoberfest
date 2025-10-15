"""
Lowest Common Ancestor in Binary Search Tree

Description:
Finds the lowest common ancestor of two nodes in a BST using recursive traversal.

Time Complexity: O(h) where h is the height of the tree
Space Complexity: O(h) for the recursion stack
"""


class TreeNode:
    """Binary Search Tree Node structure."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_bst(root, p, q):
    """
    Finds the lowest common ancestor of two nodes in a BST.
    
    Args:
        root: Root node of the BST (TreeNode)
        p: First node value or TreeNode
        q: Second node value or TreeNode
    
    Returns:
        TreeNode: The lowest common ancestor node
    """
    p_val = p.val if isinstance(p, TreeNode) else p
    q_val = q.val if isinstance(q, TreeNode) else q
    
    if root is None:
        return None
    
    # Both nodes are in left subtree
    if p_val < root.val and q_val < root.val:
        return lca_bst(root.left, p_val, q_val)
    
    # Both nodes are in right subtree
    elif p_val > root.val and q_val > root.val:
        return lca_bst(root.right, p_val, q_val)
    
    # Split point found - this is the LCA
    else:
        return root


def build_sample_bst():
    """
    Builds a sample BST for testing.
    
    Returns:
        TreeNode: Root of the sample BST
    """
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root


if __name__ == "__main__":
    # Build sample BST
    root = build_sample_bst()
    
    print("Sample BST Structure:")
    print("        6")
    print("      /   \\")
    print("     2     8")
    print("    / \\   / \\")
    print("   0   4 7   9")
    print("      / \\")
    print("     3   5")
    print()
    
    # Test cases
    test_cases = [
        (2, 8, "LCA of 2 and 8"),
        (2, 4, "LCA of 2 and 4"),
        (3, 5, "LCA of 3 and 5"),
        (0, 5, "LCA of 0 and 5"),
        (7, 9, "LCA of 7 and 9"),
        (2, 2, "LCA of 2 and 2"),
    ]
    
    print("Results:")
    for p, q, description in test_cases:
        lca = lca_bst(root, p, q)
        print(f"  {description}: {lca.val}")