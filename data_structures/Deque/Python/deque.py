"""
Deque (Double-Ended Queue) Implementation in Python
---------------------------------------------------
A Deque allows insertion and deletion of elements from both the front and rear ends.
This implementation uses the built-in `collections.deque` class, which provides
O(1) time complexity for append and pop operations from both ends.

🧠 Time Complexity:
    - add_front(): O(1)
    - add_rear(): O(1)
    - remove_front(): O(1)
    - remove_rear(): O(1)
    - is_empty(): O(1)
    - size(): O(1)
    - peek_front(): O(1)
    - peek_rear(): O(1)

💾 Space Complexity:
    - O(n), where n is the number of elements in the deque.

"""

from collections import deque

class Deque:
    """A class representing a Double-Ended Queue (Deque)."""

    def __init__(self):
        """Initialize an empty deque using collections.deque."""
        self._items = deque()

    def is_empty(self):
        """Check if the deque is empty.
        
        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self._items) == 0

    def add_front(self, item):
        """Add an item to the front of the deque.
        
        Args:
            item: Element to be added to the front.
        """
        self._items.appendleft(item)

    def add_rear(self, item):
        """Add an item to the rear (end) of the deque.
        
        Args:
            item: Element to be added to the rear.
        """
        self._items.append(item)

    def remove_front(self):
        """Remove and return an item from the front of the deque.
        
        Returns:
            The item removed from the front.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot remove from front.")
        return self._items.popleft()

    def remove_rear(self):
        """Remove and return an item from the rear of the deque.
        
        Returns:
            The item removed from the rear.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot remove from rear.")
        return self._items.pop()

    def size(self):
        """Return the number of elements in the deque.
        
        Returns:
            int: The number of items in the deque.
        """
        return len(self._items)
    
    def peek_front(self):
        """Return the item at the front without removing it.
        
        Returns:
            The item at the front of the deque
        
        Raises:
            IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("peek_front from empty deque")
        return self._items[0] 
    
    def peek_rear(self):
        """Return the item at the rear without removing it.
        
        Returns:
            The item at the rear of the deque
        
        Raises:
            IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("peek_rear from empty deque")
        return self._items[-1]


if __name__ == "__main__":
    # 🧪 Example usage of Deque class
    print("☕ Demonstrating Efficient Deque Implementation\n")

    dq = Deque()

    print("Adding elements to rear: 10, 20, 30")
    dq.add_rear(10)
    dq.add_rear(20)
    dq.add_rear(30)
    print("Current Deque:", list(dq._items))

    print("\nAdding element to front: 5")
    dq.add_front(5)
    print("Current Deque:", list(dq._items))

    print("\nRemoving element from rear:", dq.remove_rear())
    print("Current Deque:", list(dq._items))

    print("\nRemoving element from front:", dq.remove_front())
    print("Current Deque:", list(dq._items))

    print("\nIs deque empty?", dq.is_empty())
    print("Size of deque:", dq.size())

    print("\nPeek First Element:", dq.peek_front())
    print("Peek Last Element:", dq.peek_rear())

"""
Example Output:
  Demonstrating Deque Data Structure

Adding elements to rear: 10, 20, 30
Current Deque: [10, 20, 30]

Adding element to front: 5
Current Deque: [5, 10, 20, 30]

Removing element from rear: 30
Current Deque: [5, 10, 20]

Removing element from front: 5
Current Deque: [10, 20]

Is deque empty? False
Size of deque: 2

Peek First Element: 10
Peek Last Element: 20

"""