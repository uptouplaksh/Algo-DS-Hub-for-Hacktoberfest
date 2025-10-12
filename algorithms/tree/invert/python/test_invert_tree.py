import unittest
from typing import Optional, List
from invert_tree import invert_tree, Node

class TestInvertTree(unittest.TestCase):
    """Unit tests for the invert_tree function."""

    def example_tree(self, tree_type: str = 'multi-level') -> Optional[Node]:
        """
        Creates example binary trees for testing.

        Args:
            tree_type (str): Type of tree to create ('multi-level', 'simple', 'empty').

        Returns:
            Optional[Node]: Root node of the created binary tree, or None for empty.
        """
        if tree_type == 'multi-level':
            #         6
            #        / \
            #       7   8
            #      / \
            #     9   10
            #    / \
            #   11  12
            root = Node(6)
            root.left = Node(7)
            root.right = Node(8)
            root.left.left = Node(9)
            root.left.right = Node(10)
            root.left.left.left = Node(11)
            root.left.left.right = Node(12)
        elif tree_type == 'simple':
            #         13
            #        / \
            #       14   15
            root = Node(13)
            root.left = Node(14)
            root.right = Node(15)
        elif tree_type == 'empty':
            root = None
        else:
            raise ValueError("Unknown tree type")

        return root

    def inorder_traversal(self, node: Optional[Node]) -> List[int]:
        """
        Helper function to perform inorder traversal of the tree.

        Args:
            node (Optional[Node]): Root node of the binary tree.

        Returns:
            List[int]: List of node values in inorder.
        """
        if node is None:
            return []
        return (
            self.inorder_traversal(node.left)
            + [node.value]
            + self.inorder_traversal(node.right)
        )

    def test_invert_multi_level_tree(self) -> None:
        """Tests inversion of a multi-level binary tree."""
        tree = self.example_tree('multi-level')
        original_inorder = self.inorder_traversal(tree)
        invert_tree(tree)
        inverted_inorder = self.inorder_traversal(tree)

        # After inversion, the tree should look like:
        #         6
        #        / \
        #       8   7
        #          / \
        #         10  9
        #            / \
        #           12 11
        self.assertEqual(original_inorder, inverted_inorder[::-1])

    def test_invert_simple_tree(self) -> None:
        """Tests inversion of a simple binary tree."""
        tree = self.example_tree('simple')
        original_inorder = self.inorder_traversal(tree)
        invert_tree(tree)
        inverted_inorder = self.inorder_traversal(tree)

        # After inversion, the tree should look like:
        #         13
        #        / \
        #       15  14
        self.assertEqual(original_inorder, inverted_inorder[::-1])

    def test_invert_empty_tree(self) -> None:
        """Tests inversion of an empty binary tree."""
        tree = self.example_tree('empty')
        inverted_tree = invert_tree(tree)
        self.assertIsNone(inverted_tree)

if __name__ == '__main__':
    unittest.main()
