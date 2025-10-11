"""
Algorithm: Bellman-Ford Algorithm

Time Complexity: O(V * E)
- For each vertex, we relax all edges once, resulting in V-1 iterations.
- Each relaxation takes O(E), so total time is O(VE).

Space Complexity: O(V)
- We store only the distance to each vertex.

Explanation:
-------------
The Bellman-Ford algorithm computes shortest paths from a single source vertex
to all other vertices in a weighted graph. Unlike Dijkstra’s algorithm, it works
with negative edge weights.

Key Steps:
1. Initialize distances from the source to all vertices as infinity, except the source itself (0).
2. Relax all edges V-1 times (V = number of vertices).
3. Check for negative weight cycles — if a shorter path is still found after V-1 iterations,
   it means a negative cycle exists.
"""

def bellman_ford(graph, source):
    """
    graph: list of edges, where each edge is a tuple (u, v, w)
           representing an edge from u → v with weight w.
    source: starting vertex
    """
    # Extract all vertices
    vertices = set()
    for u, v, _ in graph:
        vertices.add(u)
        vertices.add(v)
    V = len(vertices)

    # Step 1: Initialize distances
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0

    # Step 2: Relax edges V-1 times
    for _ in range(V - 1):
        for u, v, w in graph:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Step 3: Check for negative weight cycles
    for u, v, w in graph:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distance


# Example runs
if __name__ == "__main__":
    print("Example 1: Simple Graph")
    graph1 = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 3),
        ('B', 'D', 2),
        ('B', 'E', 3),
        ('C', 'B', 1),
        ('C', 'D', 4),
        ('D', 'E', -5)
    ]
    print("Shortest distances from A:", bellman_ford(graph1, 'A'))
    print()

    print("Example 2: Graph with Negative Edge (No Cycle)")
    graph2 = [
        ('S', 'A', 4),
        ('S', 'E', 5),
        ('A', 'C', 6),
        ('B', 'A', 3),
        ('C', 'B', -2),
        ('D', 'C', 3),
        ('E', 'D', -1)
    ]
    print("Shortest distances from S:", bellman_ford(graph2, 'S'))
    print()

    print("Example 3: Graph with Negative Weight Cycle")
    graph3 = [
        ('A', 'B', 1),
        ('B', 'C', -1),
        ('C', 'A', -1)
    ]
    try:
        print("Shortest distances from A:", bellman_ford(graph3, 'A'))
    except ValueError as e:
        print("Error:", e)
