#
# An interactive command-line script to demonstrate Singly Linked List operations.
#

from typing import Optional, Any


class Node:
    """Represents a single node in a linked list."""

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None


class LinkedList:
    """A class representing a Singly Linked List and its core operations."""

    def __init__(self):
        self.head: Optional[Node] = None

    def display(self) -> None:
        """
        Prints the contents of the linked list.
        Time Complexity: O(n)
        """
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def add_at_beginning(self, data: Any) -> None:
        """
        Adds a new node with the given data to the beginning of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data: Any) -> None:
        """
        Adds a new node with the given data to the end of the list.
        Time Complexity: O(n)
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def insert_by_position(self, pos: int, data: Any) -> None:
        """
        Inserts a new node with the given data at a specific 0-indexed position.
        Time Complexity: O(n) in the worst case (inserting at the end).
        """
        if pos < 0:
            print("Error: Position cannot be negative.")
            return

        if pos == 0:
            self.add_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        current_pos = 0

        # Traverse to the node *before* the desired position
        while current_pos < pos - 1 and current is not None:
            current = current.next
            current_pos += 1

        if current is None:
            print(f"Error: Position {pos} is out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node
        print(f"Node with data '{data}' inserted at position {pos}.")


def main():
    """Main function to run the interactive command-line menu."""
    linked_list = LinkedList()
    while True:
        print("\n--- Interactive Linked List Menu ---")
        print("1. Display List")
        print("2. Add Node at Beginning")
        print("3. Add Node at End")
        print("4. Add Node at Specific Position")
        print("5. Create a new list from scratch (clears the old one)")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            linked_list.display()
        elif choice == 2:
            data = input("Enter data for the new node: ")
            linked_list.add_at_beginning(data)
            linked_list.display()
        elif choice == 3:
            data = input("Enter data for the new node: ")
            linked_list.add_at_end(data)
            linked_list.display()
        elif choice == 4:
            try:
                pos = int(input("Enter position (0-indexed): "))
                data = input("Enter data for the new node: ")
                linked_list.insert_by_position(pos, data)
                linked_list.display()
            except ValueError:
                print("Invalid position. Please enter a number.")
        elif choice == 5:
            linked_list.head = None  # Clear the list
            while True:
                data = input("Enter node data (or type 'done' to finish): ")
                if data.lower() == 'done':
                    break
                linked_list.add_at_end(data)
            linked_list.display()
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()