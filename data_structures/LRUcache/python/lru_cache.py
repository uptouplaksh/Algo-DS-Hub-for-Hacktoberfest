"""
Time Complexity:
- get(key): O(1) average
- put(key, value): O(1) average

Space Complexity: O(capacity)
We store up to 'capacity' items in the cache using a hash map and a doubly linked list.
"""

class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:


    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes to avoid edge checks
        self.head = Node(0, 0)  # Most recently used
        self.tail = Node(0, 0)  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1  # Not found

    def put(self, key: int, value: int):

        if key in self.cache:
            # Remove old node
            self._remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # Remove LRU item (from the tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        # Insert new node
        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node


# 🧪 Runnable Example
def main():
    print("Creating LRU Cache with capacity 2")
    lru = LRUCache(2)

    lru.put(1, 1)      # Cache: {1=1}
    lru.put(2, 2)      # Cache: {2=2, 1=1}
    print(lru.get(1))  # Returns 1, Cache: {1=1, 2=2}

    lru.put(3, 3)      # Evicts key 2, Cache: {3=3, 1=1}
    print(lru.get(2))  # Returns -1 (not found)

    lru.put(4, 4)      # Evicts key 1, Cache: {4=4, 3=3}
    print(lru.get(1))  # Returns -1 (not found)
    print(lru.get(3))  # Returns 3
    print(lru.get(4))  # Returns 4

if __name__ == "__main__":
    main()
