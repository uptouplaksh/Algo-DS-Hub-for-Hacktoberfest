#
# Singly Linked List Implementation in Python
#

class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes: data and the link to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """
    A class representing a Singly Linked List.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Checks if the linked list is empty."""
        return self.head is None

    def append(self, data):
        """Adds a new Node with data to the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def display(self):
        """Returns a list of the data in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next_node
        return elements


# Example Usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    print("Is list empty?", sll.is_empty())  # True

    sll.append(10)
    sll.append(20)
    sll.append("thirty")

    print("Is list empty?", sll.is_empty())  # False
    print("List contents:", sll.display())  # [10, 20, 'thirty']