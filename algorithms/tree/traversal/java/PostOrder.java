/*

Complexity Analysis:
Time Complexity: O(n), where n is the number of nodes in the tree, as we visit each node exactly once.
Space Complexity: O(h), where h is the height of the tree. This is for the memory on the recursion stack. In the worst case of a skewed tree, this can be O(n).
*/
public class PostOrder {

    // Definition of a tree node
    static class Node {
        int value;
        Node left, right;

        Node(int value) {
            this.value = value;
            left = right = null;
        }
    }
     /**
     * Perform post-order traversal of the binary tree.
     * @param node the root node of the tree/subtree
     */
    public static void postOrder(Node node) {
        if (node == null)
            return;
        // Recursively traverse the left subtree
        postOrder(node.left);
        // Recursively traverse the right subtree
        postOrder(node.right);
        // Process the root node (here: print its value)
        System.out.print(node.value + " ");
    }
    // Example usage
    // remove in case of general use as a module
    public static void main(String[] args) {
        /*
         * Sample binary tree:
         *         1
         *        / \
         *       2   3
         *      / \
         *     4   5
         */
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);

        System.out.print("Post-order Traversal: ");
        postOrder(root); // Output should be: 4 5 2 3 1
        System.out.println();
    }
}
