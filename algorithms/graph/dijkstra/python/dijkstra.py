"""
Dijkstra's Algorithm Implementation in Python

Time Complexity:
- Using Priority Queue (heapq): O((V + E) log V)
  where V = number of vertices, E = number of edges
- Each edge relaxation takes O(log V) due to the priority queue.

Space Complexity:
- O(V) for distance and visited tracking
- O(E) for storing the graph

This algorithm finds the shortest path from a single source
to all other vertices in a weighted graph with non-negative edge weights.
"""

import heapq


def dijkstra(graph, start):
    """
    Dijkstra's Algorithm for shortest paths from a source node.

    :param graph: Adjacency list representation of the graph
                  Example: {'A': {'B': 4, 'C': 2}, 'B': {'C': 5, 'D': 10}, ...}
    :param start: The starting node
    :return: Dictionary of shortest distances from start to all nodes
    """
    # Initialize distances to infinity, except for the start node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Priority queue for exploring nodes (distance, node)
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Skip if we already found a better path
        if current_dist > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# -------------------------------
# Example 1: Simple Graph
# -------------------------------
if __name__ == "__main__":
    print("Example 1: Simple Graph")
    graph1 = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
        'E': {'C': 10, 'D': 2, 'Z': 3},
        'Z': {'D': 6, 'E': 3}
    }
    distances1 = dijkstra(graph1, 'A')
    print("Shortest distances from A:", distances1, "\n")

    # -------------------------------
    # Example 2: Graph with multiple routes
    # -------------------------------
    print("Example 2: Graph with multiple routes")
    graph2 = {
        'S': {'A': 7, 'B': 2},
        'A': {'S': 7, 'B': 3, 'C': 4},
        'B': {'S': 2, 'A': 3, 'D': 6},
        'C': {'A': 4, 'D': 5, 'E': 6},
        'D': {'B': 6, 'C': 5, 'E': 1},
        'E': {'C': 6, 'D': 1, 'T': 2},
        'T': {'E': 2}
    }
    distances2 = dijkstra(graph2, 'S')
    print("Shortest distances from S:", distances2, "\n")

    # -------------------------------
    # Example 3: Disconnected Graph
    # -------------------------------
    print("Example 3: Disconnected Graph")
    graph3 = {
        'X': {'Y': 3},
        'Y': {'X': 3},
        'Z': {}  # Disconnected node
    }
    distances3 = dijkstra(graph3, 'X')
    print("Shortest distances from X:", distances3)
