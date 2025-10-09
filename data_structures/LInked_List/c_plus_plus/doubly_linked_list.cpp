/*
Doubly Linked List Implementation in C++
----------------------------------------
Each node contains references (pointers) to both the previous and next nodes.

Functions Implemented:
- append(data): Add a node at the end of the list.
- prepend(data): Add a node at the beginning of the list.
- deleteNode(data): Delete the first node with the given data.
- displayForward(): Display the list from head to tail.
- displayBackward(): Display the list from tail to head.

Time Complexity:
append(data):       O(1)
prepend(data):      O(1)
deleteNode(data):   O(n)
displayForward():   O(n)
displayBackward():  O(n)

Space Complexity: O(n) — for storing n nodes in the list.
*/

#include <iostream>
using namespace std;

// Node structure for doubly linked list
class Node {
public:
    int data;
    Node* prev;
    Node* next;

    Node(int val) {
        data = val;
        prev = nullptr;
        next = nullptr;
    }
};

// Doubly Linked List class
class DoublyLinkedList {
private:
    Node* head;
    Node* tail;

public:
    DoublyLinkedList() {
        head = nullptr;
        tail = nullptr;
    }

    // Append a node at the end
    void append(int data) {
        Node* newNode = new Node(data);
        if (!head) { // If list is empty
            head = tail = newNode;
            return;
        }
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }

    // Prepend a node at the beginning
    void prepend(int data) {
        Node* newNode = new Node(data);
        if (!head) { // If list is empty
            head = tail = newNode;
            return;
        }
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }

    // Delete a node by value
    void deleteNode(int data) {
        if (!head) {
            cout << "List is empty. Nothing to delete." << endl;
            return;
        }

        Node* current = head;

        while (current && current->data != data)
            current = current->next;

        if (!current) {
            cout << "Node with value " << data << " not found." << endl;
            return;
        }

        // If node to be deleted is head
        if (current == head)
            head = head->next;
        // If node to be deleted is tail
        if (current == tail)
            tail = tail->prev;

        // Update pointers
        if (current->prev)
            current->prev->next = current->next;
        if (current->next)
            current->next->prev = current->prev;

        delete current;
        cout << "Node with value " << data << " deleted successfully." << endl;
    }

    // Display list from head to tail
    void displayForward() {
        Node* current = head;
        cout << "List (Forward): ";
        while (current) {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }

    // Display list from tail to head
    void displayBackward() {
        Node* current = tail;
        cout << "List (Backward): ";
        while (current) {
            cout << current->data << " ";
            current = current->prev;
        }
        cout << endl;
    }
};

// -------------------------------
// Example Usage (main function)
// -------------------------------
int main() {
    DoublyLinkedList dll;

    dll.append(10);
    dll.append(20);
    dll.append(30);

    dll.displayForward();
    dll.displayBackward();

    dll.prepend(5);
    dll.displayForward();

    dll.deleteNode(20);
    dll.displayForward();
    dll.displayBackward();

    dll.deleteNode(100); // Non-existent node example

    return 0;
}
