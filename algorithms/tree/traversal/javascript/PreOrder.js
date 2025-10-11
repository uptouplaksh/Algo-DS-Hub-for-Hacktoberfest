/**
 * Algorithm: Pre-order Traversal of a Binary Tree (Root -> Left -> Right)
 *
 * Description:
 * Pre-order traversal is a depth-first traversal technique where:
 * 1. The current (root) node is processed first.
 * 2. Then, the left subtree is traversed.
 * 3. Finally, the right subtree is traversed.
 *
 * This traversal is often used to create a copy of the tree or get prefix expressions of expressions trees.
 *
 * Approaches:
 * 1. Recursive Solution:
 *    - Visit the root node.
 *    - Recursively traverse the left subtree.
 *    - Recursively traverse the right subtree.
 *
 * 2. Iterative Solution (using a stack):
 *    - Push the root node to a stack.
 *    - Pop from the stack, process it, then push its right and left children.
 *
 * Time Complexity:
 * O(n): Each node is visited exactly once.
 *
 * Space Complexity:
 * Recursive: O(h), where h is the height of the tree (due to call stack).
 * Iterative: O(h) due to explicit stack usage.
 */

// ----------------------------
// Definition for a Binary Tree Node
// ----------------------------
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// ----------------------------
// Recursive Pre-order Traversal
// ----------------------------
function preorderRecursive(root) {
  const result = [];

  function traverse(node) {
    if (!node) return;
    result.push(node.value); // Visit root
    traverse(node.left);     // Visit left
    traverse(node.right);    // Visit right
  }

  traverse(root);
  return result;
}

// ----------------------------
// Iterative Pre-order Traversal
// ----------------------------
function preorderIterative(root) {
  if (!root) return [];
  const stack = [root];
  const result = [];

  while (stack.length > 0) {
    const node = stack.pop();
    result.push(node.value); // Visit root

    // Push right first so left is processed first (stack is LIFO)
    if (node.right) stack.push(node.right);
    if (node.left) stack.push(node.left);
  }

  return result;
}

// ----------------------------
// Example Usage
// ----------------------------
/**
 * Example Binary Tree:
 *         1
 *        / \
 *       2   3
 *      / \
 *     4   5
 *
 * Expected Pre-order Traversal: [1, 2, 4, 5, 3]
 */

const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);

console.log("Pre-order Traversal (Recursive):", preorderRecursive(root));
console.log("Pre-order Traversal (Iterative):", preorderIterative(root));
