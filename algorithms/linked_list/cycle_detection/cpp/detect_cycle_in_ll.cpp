/*
 * C++ Solution: Detect Cycle in Linked List
 *
 * Description:
 * This program detects whether a given singly linked list contains a cycle (loop)
 * using Floyd’s Cycle Detection Algorithm (Tortoise and Hare method).
 *
 * Algorithm:
 * - Use two pointers, `slow` and `fast`.
 * - Move `slow` by one step and `fast` by two steps.
 * - If they meet, there is a cycle.
 * - If `fast` or `fast->next` becomes NULL, there is no cycle.
 *
 * Time Complexity: O(n)
 *   - Each pointer traverses at most 'n' nodes.
 *
 * Space Complexity: O(1)
 *   - Uses constant extra space.
 */

#include <iostream>
using namespace std;

// Node structure representing each element of the linked list
class Node {
public:
    int data;
    Node* next;

    Node(int value) {
        data = value;
        next = nullptr;
    }
};

// LinkedList class encapsulating list operations
class LinkedList {
private:
    Node* head;

public:
    LinkedList() {
        head = nullptr;
    }

    void insert(int value) {
        Node* newNode = new Node(value);
        if (!head) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    void createCycle(int position) {
        if (position <= 0) return;

        Node* temp = head;
        Node* cycleNode = nullptr;
        int count = 1;

        while (temp->next != nullptr) {
            if (count == position)
                cycleNode = temp;
            temp = temp->next;
            count++;
        }

        if (cycleNode)
            temp->next = cycleNode;
    }

    // Function to detect if a cycle exists using Floyd’s algorithm
    bool detectCycle() {
        Node* slow = head;
        Node* fast = head;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;      
            fast = fast->next->next;   

            if (slow == fast)
                return true;
        }

        return false;  // No cycle
    }
};


int main() {
    LinkedList list;
    list.insert(10);
    list.insert(20);
    list.insert(30);
    list.insert(40);
    list.insert(50);

    // Create a cycle for demonstration (link last node to 2nd node)
    list.createCycle(2);

    if (list.detectCycle())
        cout << "Cycle detected in the linked list." << endl;
    else
        cout << "No cycle found in the linked list." << endl;

    return 0;
}
