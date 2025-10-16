"""
Queue Implementation (FIFO - First In, First Out)
-------------------------------------------------
This module provides an implementation of a Queue data structure using Python lists.
The first element added to the queue will be the first one to be removed (FIFO principle).
"""

class Queue:
    """A simple Queue implementation using a Python list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Parameters:
            item: The element to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            The element that was first added to the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """
        Return the front item of the queue without removing it.
        
        Returns:
            The element at the front of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def is_empty(self):
        """
        Check whether the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Get the number of elements currently in the queue.
        
        Returns:
            int: The size of the queue.
        """
        return len(self.items)


# ----------------------- Example Usage -----------------------
if __name__ == "__main__":
    # Create a queue
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Display front element
    print("Front element:", q.front())  # Output: 10

    # Dequeue elements
    print("Dequeued:", q.dequeue())     # Output: 10
    print("Dequeued:", q.dequeue())     # Output: 20

    # Display remaining size
    print("Queue size:", q.size())      # Output: 1

    # Check if queue is empty
    print("Is queue empty?", q.is_empty())  # Output: False
