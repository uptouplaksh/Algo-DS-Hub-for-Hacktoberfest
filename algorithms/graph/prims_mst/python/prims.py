"""
Prim's Algorithm - Minimum Spanning Tree (MST)
-------------------------------------------------
This script implements Prim's Algorithm using a
priority queue (min-heap) to find the MST of a
connected, undirected, weighted graph.

Time Complexity:
    O(E log V) — where E is the number of edges
    and V is the number of vertices.

Space Complexity:
    O(V + E) — for storing adjacency list and visited nodes.

Author: Aman Vaibhav
"""

import heapq


def prims_mst(graph, start=0):
    """
    Function to find the Minimum Spanning Tree (MST)
    of a connected, undirected, weighted graph using Prim's Algorithm.

    Parameters:
        graph (dict): Adjacency list representation of the graph.
                      Example: {0: [(1, 2), (3, 6)], 1: [(0, 2), (2, 3), (3, 8)], ...}
        start (int): Starting vertex (default = 0)

    Returns:
        total_weight (int): Total weight of the MST
        mst_edges (list): List of edges (u, v, weight) included in MST
    """

    visited = set()  # Track visited nodes
    min_heap = [(0, start, -1)]  # (weight, vertex, parent)
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        # Skip already visited vertices
        if u in visited:
            continue

        visited.add(u)
        total_weight += weight

        # Ignore parent for starting vertex
        if parent != -1:
            mst_edges.append((parent, u, weight))

        # Explore all adjacent vertices
        for v, w in graph.get(u, []):
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    return total_weight, mst_edges


# Example runnable block
if __name__ == "__main__":
    # Example graph (undirected)
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }

    total_weight, mst_edges = prims_mst(graph, start=0)

    print("Minimum Spanning Tree (MST) Edges:")
    for u, v, w in mst_edges:
        print(f"{u} -- {v}  weight: {w}")

    print(f"\nTotal weight of MST: {total_weight}")
