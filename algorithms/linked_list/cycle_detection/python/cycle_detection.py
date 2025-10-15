"""
Floyd's Cycle Detection Algorithm (Tortoise and Hare)

Description:
This program detects whether a given singly linked list contains a cycle (loop)
using Floyd’s Cycle Detection Algorithm (Tortoise and Hare method).

Algorithm:
- Use two pointers, `slow` and `fast`.
- Move `slow` by one step and `fast` by two steps.
- If they meet, there is a cycle.
- If `fast` or `fast.next` becomes None, there is no cycle.

Time Complexity: O(n)
    - Each pointer traverses at most 'n' nodes.

Space Complexity: O(1)
    - Uses constant extra space.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert a new node with the given value at the end of the list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def create_cycle(self, position):
        """
        Create a cycle in the linked list for testing purposes.
        The last node will point to the node at the given position (1-based index).
        """
        if position <= 0:
            return

        temp = self.head
        cycle_node = None
        count = 1

        while temp.next:
            if count == position:
                cycle_node = temp
            temp = temp.next
            count += 1

        if cycle_node:
            temp.next = cycle_node

    def detect_cycle(self):
        """
        Detects if the linked list has a cycle using Floyd's algorithm.
        Returns True if a cycle is present, otherwise False.
        """
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next   
            fast = fast.next.next     


            if slow == fast:
                return True


        return False



if __name__ == "__main__":

    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)

    # Create a cycle (last node points to 2nd node)
    ll.create_cycle(2)


    if ll.detect_cycle():
        print("Cycle detected in the linked list.")
    else:
        print("No cycle found in the linked list.")

    ll2 = LinkedList()
    ll2.insert(1)
    ll2.insert(2)
    ll2.insert(3)

    if ll2.detect_cycle():
        print("Cycle detected in the linked list.")
    else:
        print("No cycle found in the linked list.")
