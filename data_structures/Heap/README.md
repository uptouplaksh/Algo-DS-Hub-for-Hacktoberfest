# Heap Data Structure

## Overview
A Heap is a specialized tree-based data structure that satisfies the heap property. This implementation provides both MinHeap and MaxHeap variants, where:
- In a MinHeap, the value of each node is less than or equal to the values of its children
- In a MaxHeap, the value of each node is greater than or equal to the values of its children

## Features

### MinHeap Operations
- `insert(key)`: Insert a new element
- `extract_min()`: Remove and return the minimum element
- `get_min()`: Get the minimum element without removing it
- Internal operations: `_sift_up()`, `_sift_down()`

### MaxHeap Operations
- `insert(key)`: Insert a new element
- `extract_max()`: Remove and return the maximum element
- `get_max()`: Get the maximum element without removing it
- Internal operations: `_sift_up()`, `_sift_down()`

## Time Complexity

| Operation     | Time Complexity |
|---------------|----------------|
| Insert        | O(log n)      |
| Extract Min/Max| O(log n)      |
| Get Min/Max   | O(1)          |
| Build Heap    | O(n)          |

## Space Complexity
- O(n) for storing n elements

## Usage Example

```python
# Create a MinHeap
min_heap = MinHeap()

# Insert elements
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)

# Get minimum element (without removing)
min_value = min_heap.get_min()  # Returns 1

# Extract minimum element
min_value = min_heap.extract_min()  # Returns and removes 1

# Create a MaxHeap
max_heap = MaxHeap()

# Insert elements
max_heap.insert(3)
max_heap.insert(1)
max_heap.insert(4)

# Get maximum element (without removing)
max_value = max_heap.get_max()  # Returns 4

# Extract maximum element
max_value = max_heap.extract_max()  # Returns and removes 4
```

## How to Run

```bash
# Navigate to the python directory
cd data_structures/Heap/python

# Run the implementation
python heap.py
```

## Applications

1. **MinHeap Applications**:
   - Priority Queues
   - Dijkstra's Shortest Path Algorithm
   - Event-driven Simulation
   - Task Scheduling

2. **MaxHeap Applications**:
   - Heap Sort
   - Finding k largest/smallest elements
   - Priority-based Systems
   - Game AI (for maintaining high scores)