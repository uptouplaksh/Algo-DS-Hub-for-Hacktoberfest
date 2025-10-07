// ============================
// 📌 Node Class - Binary Tree Node
// ============================
class Node {
    constructor(v) {
        this.data = v;      // Value stored in the node
        this.left = null;   // Left child
        this.right = null;  // Right child
    }

    // Print the value of the current node
    printNode() {
        console.log(this.data);
    }
}


// ============================
// 📌 Stack Class (LIFO)
// ============================
// Used to implement iterative preorder traversal
class Stack {
  constructor() {
    this.items = [];
  }

  // Push element on top of the stack
  push(element) {
    this.items.push(element);
  }

  // Pop the top element from the stack
  pop() {
    if (this.isEmpty()) return "Stack is empty";
    return this.items.pop();
  }

  // Peek the top element without removing it
  peek() {
    if (this.isEmpty()) return "Stack is empty";
    return this.items[this.items.length - 1];
  }

  // Check if the stack is empty
  isEmpty() {
    return this.items.length === 0;
  }

  // Return number of elements in the stack
  size() {
    return this.items.length;
  }

  // Clear all elements
  clear() {
    this.items = [];
  }
}


// ============================
// 🌲 Recursive Pre-Order Traversal
// ============================
// Traversal order: Root → Left → Right
// Time Complexity: O(n) — Each node visited exactly once
// Space Complexity: O(h) — Due to recursive call stack (h = tree height)
function PreOrderTraversalRecursive(root) {
    if (root === null) return;

    root.printNode(); // Visit current node
    PreOrderTraversalRecursive(root.left);  // Traverse left subtree
    PreOrderTraversalRecursive(root.right); // Traverse right subtree
}


// ============================
// 🌲 Iterative Pre-Order Traversal (Using Stack)
// ============================
// Traversal order: Root → Left → Right
// Time Complexity: O(n) — Each node visited exactly once
// Space Complexity: O(h) — Stack holds nodes along the height of the tree
function PreOrderTraversalIterative(root) {
    const stack = new Stack();

    // Start with root node
    stack.push(root);

    while (!stack.isEmpty()) {
        // Pop top node from stack
        const node = stack.pop();
        if (node === null) continue;

        // Visit current node
        node.printNode();

        // Push right child first so that left is processed first (LIFO)
        stack.push(node.right);
        stack.push(node.left);
    }
}


// ============================
// 🧪 Main Function — Build Tree & Run Traversals
// ============================
function main() {
    // Build a sample binary tree
    /*
             1
           /   \
          2     3
         / \     \
        4   6     6
    */
    const root = new Node(1);
    root.left = new Node(2);
    root.right = new Node(3);
    root.left.left = new Node(4);
    root.left.right = new Node(6);
    root.right.right = new Node(6);

    console.log("🔸 Recursive Preorder Traversal:");
    PreOrderTraversalRecursive(root);

    console.log("🔸 Iterative Preorder Traversal:");
    PreOrderTraversalIterative(root);
}

main();
