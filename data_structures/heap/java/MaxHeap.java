import java.util.ArrayList;

/**
 * Max-Heap Implementation in Java
 *
 * Description:
 * A Max Heap is a complete binary tree where the value of each node
 * is greater than or equal to the values of its children.
 *
 * Time Complexity:
 * - insert(): O(log n)
 * - extractMax(): O(log n)
 * - getMax(): O(1)
 *
 * Space Complexity: O(n)
 */
public class MaxHeap {

    // Internal dynamic array to store heap elements
    private ArrayList<Integer> heap;

    // Constructor
    public MaxHeap() {
        heap = new ArrayList<>();
    }

    /**
     * Inserts a new element into the heap.
     */
    public void insert(int value) {
        heap.add(value);                // Add new value at end
        heapifyUp(heap.size() - 1);     // Restore heap property
    }

    /**
     * Returns the maximum element (root) without removing it.
     */
    public int getMax() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty!");
        }
        return heap.get(0);
    }

    /**
     * Removes and returns the maximum element from the heap.
     */
    public int extractMax() {
        if (heap.isEmpty()) {
            throw new IllegalStateException("Heap is empty!");
        }
        int max = heap.get(0);
        int last = heap.remove(heap.size() - 1);
        if (!heap.isEmpty()) {
            heap.set(0, last);
            heapifyDown(0);
        }
        return max;
    }

    // Restore heap property going upwards
    private void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap.get(index) > heap.get(parent)) {
                swap(index, parent);
                index = parent;
            } else break;
        }
    }

    // Restore heap property going downwards
    private void heapifyDown(int index) {
        int size = heap.size();
        while (true) {
            int left = 2 * index + 1;
            int right = 2 * index + 2;
            int largest = index;

            if (left < size && heap.get(left) > heap.get(largest)) largest = left;
            if (right < size && heap.get(right) > heap.get(largest)) largest = right;

            if (largest != index) {
                swap(index, largest);
                index = largest;
            } else break;
        }
    }

    // Helper function to swap two indices
    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    // Example usage
    public static void main(String[] args) {
        MaxHeap heap = new MaxHeap();

        heap.insert(10);
        heap.insert(25);
        heap.insert(15);
        heap.insert(40);

        System.out.println("Max element: " + heap.getMax());    // 40
        System.out.println("Extracted: " + heap.extractMax());   // 40
        System.out.println("New Max: " + heap.getMax());         // 25
    }
}
