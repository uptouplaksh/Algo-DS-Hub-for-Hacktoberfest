# Dijkstra's Shortest Path Algorithm

## Overview
Dijkstra's algorithm is a graph search algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights, producing a shortest path tree.

## Algorithm Description

The algorithm maintains a set of unvisited nodes and continuously selects the unvisited node with the smallest tentative distance, marks it as visited, and updates the tentative distances to all unvisited neighbors.

### Key Components:
1. Priority Queue: For efficient selection of minimum distance nodes
2. Distance Array: Stores shortest distances from source to each node
3. Previous Array: Stores the previous node in the shortest path

## Time Complexity

- **Time Complexity**: O((V + E) log V)
  - V: number of vertices
  - E: number of edges
  - The log V factor comes from priority queue operations

- **Space Complexity**: O(V)
  - Stores distances and previous nodes for each vertex

## Features

- Finds shortest path between nodes in a weighted graph
- Works with any graph with non-negative edge weights
- Guarantees optimal solution
- Can be used for both directed and undirected graphs

## Usage Example

```python
# Create a graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 3, 'C': 1}
}

# Find shortest paths from node 'A'
distances, previous = dijkstra(graph, 'A')

# Get shortest path from 'A' to 'D'
path = get_shortest_path(previous, 'A', 'D')
```

## Running the Implementation

```bash
# Navigate to the python directory
cd algorithms/graph/dijkstra/python

# Run the implementation
python dijkstra.py
```

## Applications

1. **Network Routing Protocols**
   - Finding efficient paths in computer networks
   - IP routing optimization

2. **Geographic Information Systems (GIS)**
   - Navigation systems
   - Route planning
   - Maps and GPS applications

3. **Social Networks**
   - Finding shortest connection between users
   - Degrees of separation

4. **Operations Research**
   - Supply chain optimization
   - Resource allocation

## Limitations

1. Cannot handle negative edge weights
2. May not be the best choice for dense graphs
3. Requires all edge weights to be known in advance

## Optimization Techniques

1. **Bidirectional Search**
   - Search from both source and destination
   - Can significantly reduce the search space

2. **A* Algorithm**
   - An extension of Dijkstra's algorithm
   - Uses heuristics to guide the search

3. **Priority Queue Optimizations**
   - Fibonacci heap implementation
   - Can improve theoretical time complexity