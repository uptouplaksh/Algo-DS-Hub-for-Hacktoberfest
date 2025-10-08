# Quick Sort Algorithm

## Overview
Quick Sort is a highly efficient, comparison-based sorting algorithm that uses a divide-and-conquer strategy. It is widely used in practice due to its good average-case performance and efficient memory usage.

## Algorithm Complexity

- **Time Complexity**:
  - Best Case: O(n log n)
  - Average Case: O(n log n)
  - Worst Case: O(n²)
- **Space Complexity**: O(log n)
- **Stability**: Unstable

## Key Features

- In-place sorting algorithm (in the optimized version)
- Efficient for large datasets
- Works well with virtual memory systems
- Can be optimized for different types of input data

## Implementation Details

This directory contains two implementations of Quick Sort:

1. **Standard Quick Sort** (`quick_sort(arr)`)
   - Creates new arrays for partitioning
   - More intuitive and easier to understand
   - Uses more memory but can be more efficient in some cases

2. **In-Place Quick Sort** (`quick_sort_in_place(arr, low, high)`)
   - Modifies the array in place
   - More memory efficient
   - Typically used in practice

## How to Run

### Python Implementation
```bash
# Navigate to the python directory
cd algorithms/sorting/quick_sort/python

# Run the Quick Sort implementation
python quick_sort.py
```

## Example Output
```python
Input array: [64, 34, 25, 12, 22, 11, 90]
Sorted array: [11, 12, 22, 25, 34, 64, 90]
```

## When to Use Quick Sort

Quick Sort is ideal when:
1. You need a fast, in-place sorting algorithm
2. Memory space is a concern
3. Average-case performance is more important than worst-case performance
4. The input array is large

## Common Optimizations

1. **Choosing the pivot**:
   - Using median-of-three
   - Random selection
   - First, middle, or last element

2. **Handling small subarrays**:
   - Switch to insertion sort for small partitions
   - Usually more efficient for arrays < 10 elements