#!/usr/bin/env python3
# ---------------------------------------------------------------
# Interactive Singly Linked List CLI Demonstration
# Improved UX version with enhanced command-line interface
# ---------------------------------------------------------------

from typing import Optional, Any


class Node:
    """Represents a single node in a linked list."""

    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    """A class representing a Singly Linked List and its core operations."""

    def __init__(self):
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        """Returns a string representation of the linked list."""
        if self.head is None:
            return "List is empty."
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"

    def display(self) -> None:
        """Displays the linked list contents."""
        print(f"\n📜 Current Linked List:\n{self}\n")

    def add_at_beginning(self, data: Any) -> None:
        """Adds a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"✅ Node '{data}' added at the beginning.")

    def add_at_end(self, data: Any) -> None:
        """Adds a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"✅ Node '{data}' added as the first node.")
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        print(f"✅ Node '{data}' added at the end.")

    def insert_by_position(self, pos: int, data: Any) -> None:
        """Inserts a new node with the given data at a specific 0-indexed position."""
        if pos < 0:
            print("⚠️ Error: Position cannot be negative.")
            return

        if pos == 0:
            self.add_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        current_pos = 0

        # Traverse to node *before* desired position
        while current_pos < pos - 1 and current is not None:
            current = current.next
            current_pos += 1

        if current is None:
            print(f"⚠️ Error: Position {pos} is out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node
        print(f"✅ Node '{data}' inserted at position {pos}.")


# -----------------------------
# Interactive Menu
# -----------------------------
def print_menu() -> None:
    """Displays the interactive command menu with colors."""
    print("\033[96m" + "\n╔════════════════════════════════════════════╗")
    print("║          🔗 Singly Linked List Menu         ║")
    print("╚════════════════════════════════════════════╝\033[0m")
    print("1️⃣  Display List")
    print("2️⃣  Add Node at Beginning")
    print("3️⃣  Add Node at End")
    print("4️⃣  Add Node at Specific Position")
    print("5️⃣  Create a New List (clears old one)")
    print("0️⃣  Exit")


def main():
    linked_list = LinkedList()
    while True:
        print_menu()
        choice = input("\n👉 Enter your choice: ").strip()

        if not choice.isdigit():
            print("⚠️ Please enter a valid number.")
            continue

        choice = int(choice)
        print()

        if choice == 1:
            linked_list.display()

        elif choice == 2:
            data = input("Enter data for the new node: ").strip()
            linked_list.add_at_beginning(data)
            linked_list.display()

        elif choice == 3:
            data = input("Enter data for the new node: ").strip()
            linked_list.add_at_end(data)
            linked_list.display()

        elif choice == 4:
            pos_input = input("Enter position (0-indexed): ").strip()
            if not pos_input.isdigit():
                print("⚠️ Invalid position. Please enter a number.")
                continue
            pos = int(pos_input)
            data = input("Enter data for the new node: ").strip()
            linked_list.insert_by_position(pos, data)
            linked_list.display()

        elif choice == 5:
            confirm = input("Are you sure you want to clear the current list? (y/n): ").lower()
            if confirm == 'y':
                linked_list.head = None
                print("🧹 Old list cleared. Let's create a new one.")
                while True:
                    data = input("Enter node data (or type 'done' to finish): ").strip()
                    if data.lower() == 'done':
                        break
                    linked_list.add_at_end(data)
                linked_list.display()
            else:
                print("Operation cancelled.")

        elif choice == 0:
            print("\n👋 Exiting program. Goodbye!\n")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
