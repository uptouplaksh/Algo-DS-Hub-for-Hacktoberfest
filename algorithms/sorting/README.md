# Sorting Algorithms

## Overview
This directory contains various sorting algorithm implementations. Each algorithm has its own strengths and use cases, making them suitable for different scenarios.

## Comparison of Sorting Algorithms

| Algorithm      | Time (Best) | Time (Average) | Time (Worst) | Space  | Stable | In-Place |
|---------------|-------------|----------------|--------------|---------|---------|-----------|
| Quick Sort    | O(n log n)  | O(n log n)    | O(n²)       | O(log n)| No     | Yes       |
| Bubble Sort   | O(n)        | O(n²)         | O(n²)       | O(1)    | Yes    | Yes       |
| Insertion Sort| O(n)        | O(n²)         | O(n²)       | O(1)    | Yes    | Yes       |
| Merge Sort    | O(n log n)  | O(n log n)    | O(n log n)  | O(n)    | Yes    | No        |

## Key Terms

- **Stable Sort**: Preserves the relative order of equal elements
- **In-Place Sort**: Uses O(1) extra space
- **Comparison Sort**: Based on comparing elements
- **Adaptive Sort**: Performance improves with partially sorted data

## When to Use Each Algorithm

### Quick Sort
- Best for large datasets
- When average case performance is important
- When in-place sorting is required
- Not suitable when stability is required

### Bubble Sort
- For educational purposes
- Small datasets
- Nearly sorted arrays
- When code simplicity is preferred over efficiency

### Insertion Sort
- Small datasets
- Nearly sorted arrays
- When simplicity is needed
- Online sorting (sorting as data arrives)

### Merge Sort
- When stable sorting is required
- Large datasets
- External sorting
- When consistent performance is needed

## Implementation Details

Each algorithm's directory contains:
1. Implementation in various languages
2. README with detailed explanation
3. Example usage
4. Performance analysis
5. Unit tests (where applicable)

## Running the Implementations

### Python
```bash
cd algorithms/sorting/<algorithm_name>/python
python <algorithm_name>.py
```

### JavaScript
```bash
cd algorithms/sorting/<algorithm_name>/javascript
node <algorithm_name>.js
```

### Java
```bash
cd algorithms/sorting/<algorithm_name>/java
javac <Algorithm_name>.java
java <Algorithm_name>
```

## Contributing New Sorting Algorithms

When adding a new sorting algorithm:
1. Create a new directory under `sorting/`
2. Include implementations in one or more languages
3. Add comprehensive documentation
4. Include example usage
5. Add time and space complexity analysis
6. Include test cases