class Node {
    constructor(v) {
        this.data = v;
        this.left = null;
        this.right = null;
    }
    printNode() {
        console.log(this.data);
    }
}

class Stack {
  constructor() {
    this.items = [];
  }

  // Add element to top
  push(element) {
    this.items.push(element);
  }

  // Remove top element
  pop() {
    if (this.isEmpty()) return "Stack is empty";
    return this.items.pop();
  }

  // Look at the top element without removing
  peek() {
    if (this.isEmpty()) return "Stack is empty";
    return this.items[this.items.length - 1];
  }

  // Check if stack is empty
  isEmpty() {
    return this.items.length === 0;
  }

  // Get size of stack
  size() {
    return this.items.length;
  }

  // Clear all elements
  clear() {
    this.items = [];
  }
}

function PreOrderTraversalRecursive(root) {
    if (root === null) {
        return;
    }
    root.printNode();
    PreOrderTraversalRecursive(root.left);
    PreOrderTraversalRecursive(root.right);
}

function PreOrderTraversalIterative(root) {

    const items = new Stack();
    items.push(root);
    while(!items.isEmpty()) {
        let node = items.pop();
        if(node === null){
            continue;
        }
        node.printNode();
        items.push(node.right);
        items.push(node.left);
    }

}

function main() {
    const root = new Node(1);
    root.left = new Node(2);
    root.right = new Node(3);
    root.left.left = new Node(4);
    root.left.right = new Node(6);
    root.right.right = new Node(6);

    PreOrderTraversalRecursive(root);
    PreOrderTraversalIterative(root);
}

main();

