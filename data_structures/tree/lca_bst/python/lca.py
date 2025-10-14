"""
Lowest Common Ancestor (LCA) in a Binary Search Tree

The LCA of two nodes p and q is the lowest node that has both p and q as 
descendants (a node can be a descendant of itself).
"""


class TreeNode:
    """Binary Search Tree Node structure."""
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_bst(root, p, q):
    """
    Find LCA of two nodes in BST using recursion.
    
    Leverages BST property: if both nodes are less than root, LCA is in left 
    subtree; if both are greater, LCA is in right subtree; otherwise root is LCA.
    
    Time Complexity: O(h) where h is tree height
    Space Complexity: O(h) for recursion stack
    
    Args:
        root: Root node of the BST
        p: First node (TreeNode or int value)
        q: Second node (TreeNode or int value)
    
    Returns:
        TreeNode: The LCA node
    """
    p_val = p.val if isinstance(p, TreeNode) else p
    q_val = q.val if isinstance(q, TreeNode) else q
    
    if root is None:
        return None
    
    if p_val < root.val and q_val < root.val:
        return lca_bst(root.left, p_val, q_val)
    elif p_val > root.val and q_val > root.val:
        return lca_bst(root.right, p_val, q_val)
    else:
        return root


def build_sample_bst():
    """
    Build sample BST:
            6
          /   \
         2     8
        / \   / \
       0   4 7   9
          / \
         3   5
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


# ============================================================================
# RUNNABLE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Lowest Common Ancestor in Binary Search Tree")
    print("=" * 60)
    
    root = build_sample_bst()
    print("\nSample BST Structure:")
    print("        6")
    print("      /   \\")
    print("     2     8")
    print("    / \\   / \\")
    print("   0   4 7   9")
    print("      / \\")
    print("     3   5")
    print()
    
    test_cases = [
        (2, 8, "LCA of 2 and 8"),
        (2, 4, "LCA of 2 and 4"),
        (3, 5, "LCA of 3 and 5"),
        (0, 5, "LCA of 0 and 5"),
        (7, 9, "LCA of 7 and 9"),
        (2, 2, "LCA of 2 and 2 (node with itself)"),
    ]
    
    print("RESULTS:")
    print("-" * 60)
    for p, q, description in test_cases:
        lca = lca_bst(root, p, q)
        print(f"{description}: {lca.val}")
    
    print("\n" + "=" * 60)
    print("COMPLEXITY ANALYSIS:")
    print("-" * 60)
    print("Time Complexity:  O(h) where h = height")
    print("Space Complexity: O(h) for recursion stack")
    print("\nFor balanced BST: h = log(n)")
    print("For skewed BST:   h = n")
    print("=" * 60)