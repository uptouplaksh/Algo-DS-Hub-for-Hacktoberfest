package Open-Source-DS-Algo.data_structures.heap.java;

import java.util.Arrays;
import java.util.Scanner;

public class MaxHeap {
    private int[] heap;      // Array to store heap elements
    private int size;        // Number of elements currently in heap
    private int capacity;    // Maximum capacity of heap

    // Constructor
    public MaxHeap(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.heap = new int[capacity];
    }

    // Get parent index
    private int parent(int i) {
        return (i - 1) / 2;
    }

    // Get left child index
    private int leftChild(int i) {
        return (2 * i) + 1;
    }

    // Get right child index
    private int rightChild(int i) {
        return (2 * i) + 2;
    }

    // Swap two nodes
    private void swap(int i, int j) {
        int temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    // Insert a new value
    // Time: O(log n), Space: O(1)
    public void insert(int value) {
        if (size == capacity) {
            expandHeap();
        }

        heap[size] = value; // Place value at the end
        size++;
        heapifyUp(size - 1); // Fix heap property
    }

    // Double the heap size when full
    private void expandHeap() {
        capacity *= 2;
        heap = Arrays.copyOf(heap, capacity);
        System.out.println("Heap expanded to capacity: " + capacity);
    }

    // Restore heap upwards after insertion
    private void heapifyUp(int index) {
        while (index > 0 && heap[parent(index)] < heap[index]) {
            swap(parent(index), index);
            index = parent(index);
        }
    }

    // Get maximum value (root)
    // Time: O(1)
    public int getMax() {
        if (size == 0) {
            System.out.println("Heap is empty!");
            return -1;
        }
        return heap[0];
    }

    // Remove and return maximum element
    // Time: O(log n), Space: O(1)
    public int extractMax() {
        if (size == 0) {
            System.out.println("Heap is empty!");
            return -1;
        }

        int max = heap[0];           // Save root
        heap[0] = heap[size - 1];    // Move last element to root
        size--;
        heapifyDown(0);              // Restore heap property
        return max;
    }

    // Restore heap downwards after extraction
    private void heapifyDown(int index) {
        int largest = index;
        int left = leftChild(index);
        int right = rightChild(index);

        if (left < size && heap[left] > heap[largest]) {
            largest = left;
        }

        if (right < size && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != index) {
            swap(index, largest);
            heapifyDown(largest);
        }
    }

    // Print heap contents
    public void printHeap() {
        if (size == 0) {
            System.out.println("Heap is empty!");
        } else {
            System.out.println("Heap: " + Arrays.toString(Arrays.copyOf(heap, size)));
        }
    }

    // Main method for demonstration
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        MaxHeap heap = new MaxHeap(5);

        System.out.println("=== MAX HEAP DEMO ===");
        System.out.println("1 → Insert element");
        System.out.println("2 → Get Max");
        System.out.println("3 → Extract Max");
        System.out.println("4 → Print Heap");
        System.out.println("0 → Exit");

        while (true) {
            System.out.print("\nEnter choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value: ");
                    heap.insert(sc.nextInt());
                    break;

                case 2:
                    System.out.println("Max Element: " + heap.getMax());
                    break;

                case 3:
                    int extracted = heap.extractMax();
                    if (extracted != -1) {
                        System.out.println("Extracted Max: " + extracted);
                    }
                    break;

                case 4:
                    heap.printHeap();
                    break;

                case 0:
                    System.out.println("Exiting...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice! Try again.");
            }
        }
    }
}

