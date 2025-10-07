"""
Level-Order Traversal of a Binary Tree (Breadth-First Search)
Description:
    Performs a level-order traversal of a binary tree using a queue.
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) due to the queue storing nodes at each level
"""

from collections import deque

class Node:
    """Class representing a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    """
    Perform level-order traversal of a binary tree.
    
    Args:
        root (Node): The root node of the binary tree.
    
    Returns:
        list: List of values in level-order.
    """
    if not root:
        return []

    result = []
    queue = deque([root])  # Initialize queue with root

    while queue:
        current = queue.popleft()  # Pop node from front of the queue
        result.append(current.value)  # Process current node

        # Add child nodes to the queue
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

# 🧪 Example Run
if __name__ == "__main__":
    # Construct example binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print("Level-order Traversal:", level_order_traversal(root))
    # Output: [1, 2, 3, 4, 5, 6]
