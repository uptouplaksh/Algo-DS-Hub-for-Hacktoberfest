#
# Stack Data Structure in Python (using a list)
#

class Stack:
    """
    A simple implementation of a Stack (LIFO).
    """
    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty."""
        return not self.items

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item from the top of the stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Returns the top item of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)

# Example Usage:
if __name__ == "__main__":
    s = Stack()
    print("Is stack empty?", s.is_empty()) # True
    s.push("A")
    s.push("B")
    print("Top item:", s.peek()) # "B"
    s.push("C")
    print("Size:", s.size()) # 3
    print("Popped item:", s.pop()) # "C"
    print("Is stack empty?", s.is_empty()) # False