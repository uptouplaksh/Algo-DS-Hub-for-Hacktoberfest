"""
Queue implementation using two stacks.

Author: Rebel Technology / ChatGPT
Description:
This module demonstrates how to implement a Queue (FIFO) using two stacks (LIFO).
We use two lists in Python to simulate stack behavior with append() and pop() operations.

File Location:
data_structures/Queue/python/queue_using_stacks.py
"""

class QueueUsingStacks:
    """
    A Queue implemented using two stacks.

    Stack operations used:
        - append(x)  → push operation (O(1))
        - pop()      → pop operation (O(1))
    """

    def __init__(self):
        # stack1 is used for enqueue operations
        # stack2 is used for dequeue operations
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        """
        Add an element to the end of the queue.
        Time Complexity: O(1)
        """
        self.stack1.append(item)
        # Debug info
        print(f"Enqueued: {item}, Stack1: {self.stack1}, Stack2: {self.stack2}")

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        If stack2 is empty, move all elements from stack1 to stack2 first.
        Time Complexity:
            - Amortized O(1)
            - Worst Case O(n) when transferring elements from stack1 to stack2
        """
        if not self.stack2:
            # Move all elements from stack1 to stack2
            while self.stack1:
                popped_item = self.stack1.pop()
                self.stack2.append(popped_item)
                # Debug info for each move
                print(f"Moved {popped_item} from Stack1 → Stack2")

        if not self.stack2:
            raise IndexError("Dequeue from empty queue")

        dequeued_item = self.stack2.pop()
        # Debug info
        print(f"Dequeued: {dequeued_item}, Stack1: {self.stack1}, Stack2: {self.stack2}")
        return dequeued_item

    def is_empty(self):
        """
        Check if the queue is empty.
        Time Complexity: O(1)
        """
        return not (self.stack1 or self.stack2)

    def peek(self):
        """
        Return the front element without removing it.
        Time Complexity: Amortized O(1)
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("Peek from empty queue")
        return self.stack2[-1]


# ------------------------- RUNNABLE EXAMPLE -------------------------
if __name__ == "__main__":
    print("Queue using Two Stacks Example:\n")

    queue = QueueUsingStacks()

    # Enqueue operations
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Peek front element
    print(f"Front element (peek): {queue.peek()}")

    # Dequeue operations
    print(f"Dequeued element: {queue.dequeue()}")
    print(f"Dequeued element: {queue.dequeue()}")

    # Enqueue another element
    queue.enqueue(40)

    # Final dequeues
    print(f"Dequeued element: {queue.dequeue()}")
    print(f"Dequeued element: {queue.dequeue()}")

    # Check if queue is empty
    print(f"Is queue empty? {queue.is_empty()}")
