/**
 * MaxHeap.java
 *
 * This program implements a Max-Heap data structure in Java.
 * A Max-Heap is a type of complete binary tree where:
 *     - Each parent node is greater than or equal to its children.
 *     - The largest element is always at the root (top) of the heap.
 *
 * Common Operations:
 *     - insert(value): Adds a new element to the heap while keeping the structure valid.
 *     - getMax(): Returns the maximum element (root) without removing it.
 *     - extractMax(): Removes and returns the maximum element, then reorders the heap.
 *
 */

package data_structures.Heap.java;

import java.util.Arrays;

public class MaxHeap {

    // The array where heap elements are stored
    private int[] heap;

    // Number of elements currently in the heap
    private int size;

    // Maximum capacity (how many elements the heap can store)
    private int capacity;

    /**
     * Constructor: creates an empty heap of a given capacity
     */
    public MaxHeap(int capacity) {
        this.capacity = capacity; // set maximum possible size
        this.size = 0;            // initially heap is empty
        this.heap = new int[capacity]; // create an array of given capacity
    }

    // -------------------- Helper Methods --------------------

    // These methods help us navigate between nodes in the heap.

    // Given a child index, this returns the index of its parent node
    private int parent(int i) {
        return (i - 1) / 2;
    }

    // Returns the index of the left child of a given node
    private int leftChild(int i) {
        return (2 * i) + 1;
    }

    // Returns the index of the right child of a given node
    private int rightChild(int i) {
        return (2 * i) + 2;
    }

    // Swaps two elements in the heap (used frequently in rearranging)
    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    // -------------------- Core Operations --------------------

    /**
     * Inserts a new element into the heap.
     *
     * Steps:
     * 1️⃣ Place the new element at the end of the heap.
     * 2️⃣ "Bubble up" — keep swapping with its parent until
     *     the heap property (parent >= children) is restored.
     */
    public void insert(int value) {
        // Check if heap is already full
        if (size == capacity) {
            System.out.println("⚠️  Heap is full! Cannot insert value: " + value);
            return;
        }

        // Step 1: Place the new element at the end
        heap[size] = value;
        int current = size; // current index of newly inserted element
        size++; // increase heap size

        // Step 2: Bubble up the element until heap property is satisfied
        // Keep checking while current element is greater than its parent
        while (current > 0 && heap[current] > heap[parent(current)]) {
            swap(current, parent(current)); // swap current node with its parent
            current = parent(current); // move up to parent index
        }
    }

    /**
     * Returns the maximum element (root of the heap).
     * Does not remove it.
     */
    public int getMax() {
        if (size == 0) {
            throw new IllegalStateException("Heap is empty.");
        }
        return heap[0]; // root element always contains the largest value
    }

    /**
     * Removes and returns the maximum element from the heap.
     *
     * Steps:
     * 1️⃣ Replace the root (first element) with the last element.
     * 2️⃣ Reduce heap size by 1 (since we removed one element).
     * 3️⃣ "Heapify down" — push the new root down until heap property is valid.
     */
    public int extractMax() {
        if (size == 0) {
            throw new IllegalStateException("Heap is empty.");
        }

        int max = heap[0]; // store the max (root)
        heap[0] = heap[size - 1]; // move last element to root
        size--; // reduce heap size

        // Fix heap property by heapifying downwards
        heapifyDown(0);

        return max; // return the extracted max value
    }

    /**
     * Restores the heap property from a given index downwards.
     * This is used after removing the root.
     */
    private void heapifyDown(int i) {
        int largest = i; // assume current node is largest
        int left = leftChild(i);
        int right = rightChild(i);

        // If left child exists and is greater than current largest
        if (left < size && heap[left] > heap[largest]) {
            largest = left;
        }

        // If right child exists and is greater than current largest
        if (right < size && heap[right] > heap[largest]) {
            largest = right;
        }

        // If largest is not the parent node, swap and continue heapifying
        if (largest != i) {
            swap(i, largest);
            heapifyDown(largest); // recursively fix affected subtree
        }
    }

    /**
     * Prints the current elements of the heap in array form.
     */
    public void printHeap() {
        System.out.println("Current Heap: " + Arrays.toString(Arrays.copyOf(heap, size)));
    }

    // -------------------- Example Use Cases --------------------

    public static void main(String[] args) {

        // Create a MaxHeap with capacity for 10 elements
        MaxHeap heap = new MaxHeap(10);

        System.out.println("=== Example 1: Inserting elements ===");
        heap.insert(15);
        heap.insert(10);
        heap.insert(30);
        heap.insert(40);
        heap.insert(5);
        heap.insert(25);
        heap.printHeap();
        // You should see the largest number (40) as the first element (root)

        System.out.println("\n=== Example 2: Get Maximum ===");
        System.out.println("Maximum element in heap: " + heap.getMax());
        // Expected output: 40

        System.out.println("\n=== Example 3: Extract Maximum ===");
        int max1 = heap.extractMax();
        System.out.println("Extracted Max: " + max1);
        heap.printHeap();
        // The heap will rearrange and the next largest (30) will become the new root

        System.out.println("\n=== Example 4: Insert New Element After Extraction ===");
        heap.insert(50); // this should become the new max
        heap.printHeap();
        // 50 should move to the top

        System.out.println("\n=== Example 5: Keep Extracting Until Empty ===");
        while (heap.size > 0) {
            int val = heap.extractMax();
            System.out.println("Extracted: " + val);
            heap.printHeap();
        }
        // At the end, heap will be empty
    }
}

/*
-------------------------------------------------------
🧠 DETAILED EXPLANATION SUMMARY
-------------------------------------------------------

📌 WHAT IS A MAX-HEAP?
A Max-Heap is a binary tree where:
  - Every node’s value is greater than or equal to its children.
  - The largest value is always at the top (index 0 in array form).

Example representation (as array):
   [40, 30, 25, 10, 5, 15]
   means:
           40
         /    \
       30      25
      /  \    /
     10   5  15

-------------------------------------------------------

⚙️ HOW INSERTION WORKS:
1. Add new value at the end of array.
2. Compare with its parent.
3. If new value is greater, swap with parent.
4. Keep repeating until parent is greater or root is reached.

Time Complexity: O(log n)

-------------------------------------------------------

⚙️ HOW EXTRACTION WORKS:
1. Take out the root (max value).
2. Move the last element to root.
3. Push this new root down ("heapify down") until max-heap property holds.

Time Complexity: O(log n)

-------------------------------------------------------

🧩 COMPLEXITY ANALYSIS:
Insert → O(log n)
ExtractMax → O(log n)
GetMax → O(1)
Space → O(n)

-------------------------------------------------------

✅ OUTPUT EXAMPLES:
Inserting elements:
Current Heap: [40, 30, 25, 10, 5, 15]
Maximum element: 40
Extracted Max: 40
Heap after extraction: [30, 10, 25, 15, 5]
After inserting 50: [50, 30, 25, 10, 5, 15]
Extracted: 50
Extracted: 30
Extracted: 25
... until heap empty.
-------------------------------------------------------
*/
