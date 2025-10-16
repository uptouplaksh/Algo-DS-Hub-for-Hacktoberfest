// File: /data_structures/Stack/javascript/Stack.js

/*
 * ----------------------------------------------------------------
 * Time and Space Complexity Analysis
 * ----------------------------------------------------------------
 *
 * All operations are performed on the end of the underlying array,
 * which is highly efficient.
 *
 * Let 'n' be the number of items in the stack.
 *
 * Method      | Time Complexity | Space Complexity
 * -------------------------------------------------
 * push(item)  | O(1) Amortized* | O(1)
 * pop()       | O(1)            | O(1)
 * peek()      | O(1)            | O(1)
 * isEmpty()   | O(1)            | O(1)
 * size()      | O(1)            | O(1)
 *
 * Overall Space Complexity for the Stack data structure: O(n)
 *
 * *Note on Amortized O(1) for push: While adding an element to a
 * dynamic array is usually O(1), occasionally the array may need to
* be resized if it runs out of capacity. This resizing operation
* takes O(n) time, but it happens so infrequently that the average
* cost, or "amortized" cost, over many push operations is still O(1).
 */

/**
 * Represents a Stack data structure (LIFO - Last-In, First-Out) 🥞.
 * This implementation uses a JavaScript array to store the stack elements.
 */
class Stack {
  /**
   * Initializes a new, empty stack.
   */
  constructor() {
    this.items = [];
  }

  /**
   * Adds an item to the top of the stack.
   * @param {*} item The item to be added to the stack.
   */
  push(item) {
    this.items.push(item);
  }

  /**
   * Removes and returns the item from the top of the stack.
   * If the stack is empty, it returns undefined.
   * @returns {*} The removed item from the top of the stack.
   */
  pop() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items.pop();
  }

  /**
   * Returns the top item of the stack without removing it.
   * If the stack is empty, it returns undefined.
   * @returns {*} The item at the top of the stack.
   */
  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.items.length - 1];
  }

  /**
   * Checks if the stack is empty.
   * @returns {boolean} Returns true if the stack contains no items, otherwise false.
   */
  isEmpty() {
    return this.items.length === 0;
  }

  /**
   * Returns the number of items in the stack.
   * @returns {number} The total number of items in the stack.
   */
  size() {
    return this.items.length;
  }
}

// Export the class for use in other modules (e.g., in a Node.js environment)
module.exports = Stack;