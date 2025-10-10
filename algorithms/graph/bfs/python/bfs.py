"""
Breadth-First Search (BFS) Traversal Implementation In Python
===================================================
Time Complexity:
----------------
O(V + E) where:
- V = Number of vertices (nodes)
- E = Number of edges

Space Complexity:
-----------------
O(V) for storing visited nodes and queue.

"""

from collections import deque
from typing import Dict, List, Any


# SIMPLE BFS TRAVERSAL
def bfs_traversal(graph: dict, start_node) -> List[Any]:
    """
    Perform Breadth-First Search traversal on a given graph.

    Parameters:
    -----------
    graph : dict
        A dictionary representing the adjacency list of the graph.
        Example: {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']}
    start_node : an
        The node from which BFS traversal should begin.

    Returns:
    --------
    list
        A list containing the nodes in the order they were visited.
    """

    visited = set()          # Keep track of visited nodes
    queue = deque([start_node])  # Initialize queue with the start node
    traversal_order = []     # Store the order of traversal

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            # Enqueue all unvisited neighbors
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

# BFS TRAVERSAL WITH RETURN LEVELS
def bfs_with_levels(graph: Dict[Any, List[Any]], start_node: Any) -> Dict[Any, int]:
    """
    Perform BFS and return the level (distance) of each node from the start node.
    
    Args:
        graph: A dictionary representing the graph as an adjacency list.
        start_node: The node from which to start the BFS traversal.
    
    Returns:
        A dictionary mapping each reachable node to its level/distance from start_node.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
   
    visited = set()
    queue = deque([(start_node, 0)])  # Store (node, level) tuples
    levels = {}
    
    visited.add(start_node)
    
    while queue:
        current_node, level = queue.popleft()
        levels[current_node] = level
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    
    return levels


def bfs_main(graph: Dict[Any, List[Any]], start_node: Any,is_withLevel:bool=False) ->   List[Any] | Dict[Any, int] :
     if start_node not in graph:
        raise KeyError(f"Start node '{start_node}' not found in graph")
     if is_withLevel :
         return bfs_with_levels(graph,start_node)
     return bfs_traversal(graph,start_node)

# Example usage
if __name__ == "__main__":
    #  adjacency list
    graph_example = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'
    print("Graph adjacency list:", graph_example)
    print(f"BFS traversal starting from '{start_node}':", bfs_main(graph_example, 'A'))
    print(f"BFS with levels from '{start_node}':", bfs_main(graph_example, 'A', is_withLevel=True))
