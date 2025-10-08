class Node:
    """Binary Tree Node class."""
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def invert_tree(node):
    """
    Recursively inverts (mirrors) a binary tree.

    This function swaps the left and right child nodes of every node
    in the tree to create its mirror image.

    Args:
    node (Node): Root node of the binary tree.

    Returns:
    Node: The root node of the inverted (mirrored) binary tree.

    Example:
    Original Tree:         Inverted Tree:
                1                      1
               / \                    / \
              2   3                  3   2

    Time Complexity: O(n)
        - Each node is visited exactly once.
    Space Complexity: O(h)
        - h is the height of the tree (due to recursion stack).
    """
    #Base case: If the node is None, nothing to invert
    if node is None:
        return None
    
    #Recursively invert left and right subtrees
    left_inverted = invert_tree(node.left)
    right_inverted = invert_tree(node.right)

    #Swap left and right children
    node.left = right_inverted
    node.right = left_inverted

    #Return current node (root of inverted subtree)
    return node
def print_tree(root):

    """function to print tree in level-order format"""
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


# ---- Runnable Example Block ----
# ---- Remove this if using as a general-purpose module ----
if __name__ == "__main__":
    # Build sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Original Tree (Level-order):", print_tree(root))

    # Invert the tree
    inverted_root = invert_tree(root)

    print("Inverted Tree (Level-order):", print_tree(inverted_root))
    # Output:
    # Original Tree (Level-order): [1, 2, 3, 4, 5]
    # Inverted Tree (Level-order): [1, 3, 2, 5, 4]
