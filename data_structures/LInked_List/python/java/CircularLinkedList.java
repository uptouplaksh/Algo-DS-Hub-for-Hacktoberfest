/**
 * Circular Linked List Implementation in Java
 * 
 * Description:
 * This class demonstrates a Circular Linked List where the last node points
 * back to the first node. Supports insertion, deletion, and traversal.
 * 
 * Time Complexity:
 * - Insertion: O(1) at head/tail
 * - Deletion: O(n) in general case
 * - Traversal: O(n)
 * 
 * Space Complexity: O(n)
 */

class CircularLinkedList {

    // Node class representing each element in the list
    private static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node tail; // tail points to the last node

    // Constructor: Initialize an empty list
    public CircularLinkedList() {
        tail = null;
    }

    /**
     * Insert a new node at the end of the list
     */
    public void insert(int data) {
        Node newNode = new Node(data);
        if (tail == null) {
            tail = newNode;
            tail.next = tail; // points to itself
        } else {
            newNode.next = tail.next;
            tail.next = newNode;
            tail = newNode;
        }
    }

    /**
     * Delete a node with the given value
     */
    public void delete(int data) {
        if (tail == null) return; // empty list

        Node current = tail.next;
        Node prev = tail;
        boolean found = false;

        do {
            if (current.data == data) {
                found = true;
                break;
            }
            prev = current;
            current = current.next;
        } while (current != tail.next);

        if (!found) return; // element not found

        // single node case
        if (current == tail && current.next == tail) {
            tail = null;
        } else {
            prev.next = current.next;
            if (current == tail) {
                tail = prev;
            }
        }
    }

    /**
     * Traverse and print the circular linked list
     */
    public void traverse() {
        if (tail == null) {
            System.out.println("List is empty.");
            return;
        }

        Node current = tail.next;
        do {
            System.out.print(current.data + " -> ");
            current = current.next;
        } while (current != tail.next);
        System.out.println("(back to head)");
    }

    // ------------------------- MAIN METHOD -------------------------
    public static void main(String[] args) {
        CircularLinkedList list = new CircularLinkedList();

        System.out.println("Circular Linked List Example\n");

        // Insert elements
        list.insert(10);
        list.insert(20);
        list.insert(30);
        list.insert(40);

        System.out.println("Traversal after insertion:");
        list.traverse();

        // Delete element
        list.delete(20);
        System.out.println("\nTraversal after deleting 20:");
        list.traverse();

        // Delete tail element
        list.delete(40);
        System.out.println("\nTraversal after deleting 40:");
        list.traverse();
    }
}
