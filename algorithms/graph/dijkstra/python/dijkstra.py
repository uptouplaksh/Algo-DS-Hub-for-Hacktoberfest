"""
Dijkstra's Shortest Path Algorithm Implementation

This implementation finds the shortest path between nodes in a graph using Dijkstra's algorithm.
The algorithm uses a min-heap priority queue for efficient node selection.

Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges
Space Complexity: O(V)
"""

from heapq import heappush, heappop
from typing import Dict, List, Set, Tuple
import math

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implementation of Dijkstra's shortest path algorithm using a priority queue.
    
    Args:
        graph: A dictionary representing the weighted graph {node: {neighbor: distance}}
        start: Starting node
        
    Returns:
        Tuple containing:
        - Dictionary of shortest distances from start to all nodes
        - Dictionary of previous nodes in the shortest path
        
    Example:
        >>> graph = {
        ...     'A': {'B': 4, 'C': 2},
        ...     'B': {'A': 4, 'D': 3},
        ...     'C': {'A': 2, 'D': 1},
        ...     'D': {'B': 3, 'C': 1}
        ... }
        >>> distances, previous = dijkstra(graph, 'A')
        >>> distances
        {'A': 0, 'C': 2, 'D': 3, 'B': 4}
    """
    # Initialize distances to infinity and previous nodes to None
    distances = {node: math.inf for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    
    # Priority queue to store (distance, node)
    pq = [(0, start)]
    
    # Set to keep track of visited nodes
    visited: Set[str] = set()
    
    while pq:
        # Get node with minimum distance
        current_distance, current_node = heappop(pq)
        
        # If we've already processed this node, skip it
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
                
            # Calculate new distance to neighbor
            distance = current_distance + weight
            
            # If we found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heappush(pq, (distance, neighbor))
                
    return distances, previous

def get_shortest_path(previous: Dict[str, str], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path from start to end using the previous nodes dictionary.
    
    Args:
        previous: Dictionary of previous nodes in shortest path
        start: Starting node
        end: End node
        
    Returns:
        List of nodes representing the shortest path
        
    Example:
        >>> previous = {'A': None, 'B': 'A', 'C': 'A', 'D': 'C'}
        >>> get_shortest_path(previous, 'A', 'D')
        ['A', 'C', 'D']
    """
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
        
    return path[::-1]  # Reverse the path to get start->end order


# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list with weights
    example_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 3},
        'C': {'A': 2, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }
    
    # Find shortest paths from node 'A'
    start_node = 'A'
    distances, previous = dijkstra(example_graph, start_node)
    
    # Print distances from 'A' to all other nodes
    print(f"\nShortest distances from node {start_node}:")
    for node, distance in distances.items():
        print(f"{start_node} -> {node}: {distance}")
        
    # Print shortest path from 'A' to 'D'
    end_node = 'D'
    path = get_shortest_path(previous, start_node, end_node)
    print(f"\nShortest path from {start_node} to {end_node}:")
    print(" -> ".join(path))