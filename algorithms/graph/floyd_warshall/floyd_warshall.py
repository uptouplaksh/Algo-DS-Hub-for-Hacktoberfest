"""
Floyd–Warshall Algorithm (All-Pairs Shortest Paths)
Description:
A dynamic programming implementation of the Floyd–Warshall algorithm that computes shortest
path distances between every pair of vertices in a weighted directed graph. Also provides
path reconstruction information.

Time Complexity: O(V^3) where V is the number of vertices.
Space Complexity: O(V^2) for the distance and next (path reconstruction) matrices.
"""

from typing import List, Tuple, Optional

INF = float("inf")


def floyd_warshall(adj_matrix: List[List[Optional[float]]]) -> Tuple[List[List[float]], List[List[Optional[int]]]]:
    """
    Compute all-pairs shortest paths using the Floyd–Warshall dynamic programming approach.

    The algorithm:
      - Uses a 2D distance matrix `dist` where dist[i][j] is the length of the shortest path
        from i to j found so far.
      - Iteratively allows intermediate vertices k = 0..V-1 and tries to improve every pair
        (i, j) via `i -> k -> j`.
      - Optionally maintains a `next_node` (sometimes called "next" or "succ") matrix to
        reconstruct shortest paths: next_node[i][j] is the vertex after i on the path to j.

    Args:
        adj_matrix: adjacency matrix representation of the graph with shape (V x V).
                    Use a numeric weight for edges, and either None or float('inf') for
                    missing edges. The diagonal adj_matrix[i][i] should be 0 (or will be set to 0).

    Returns:
        dist: V x V matrix where dist[i][j] is the shortest distance from i to j (INF if no path).
        next_node: V x V matrix where next_node[i][j] is the index of the next vertex after i on
                   the shortest path to j, or None if no path exists.
    """
    V = len(adj_matrix)
    # Initialize distance and next matrices
    dist: List[List[float]] = [[INF] * V for _ in range(V)]
    next_node: List[List[Optional[int]]] = [[None] * V for _ in range(V)]

    # Copy adjacency information into dist, and set the next pointers for direct edges
    for i in range(V):
        for j in range(V):
            w = adj_matrix[i][j]
            if w is None:
                # treat None as no edge
                continue
            dist[i][j] = w
            if i != j and w < INF:
                # If there's a direct edge i->j, next on path from i to j is j
                next_node[i][j] = j

    # Ensure zero on diagonal (distance from vertex to itself)
    for i in range(V):
        dist[i][i] = 0.0
        # next_node[i][i] can stay None; path from i to i is trivial (empty)

    # Core Floyd–Warshall DP:
    # For each possible intermediate vertex k, try to improve dist[i][j] by going through k.
    # This is the triple-loop DP with O(V^3) time complexity.
    for k in range(V):
        # Use local references for slight micro-optimizations (not necessary, but common)
        dist_k = dist[k]
        for i in range(V):
            dist_i = dist[i]
            # If dist[i][k] is INF, we cannot use k as intermediate for i -> j
            if dist_i[k] == INF:
                continue
            via_ik = dist_i[k]
            for j in range(V):
                # Candidate distance using k as intermediate: dist[i][k] + dist[k][j]
                candidate = via_ik + dist_k[j]
                if candidate < dist_i[j]:
                    dist_i[j] = candidate
                    # Update next pointer: from i to j, the next vertex is what it was for i->k
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def reconstruct_path(u: int, v: int, next_node: List[List[Optional[int]]]) -> List[int]:
    """
    Reconstruct the shortest path from u to v using the `next_node` matrix returned by floyd_warshall.

    Args:
        u: source vertex index
        v: target vertex index
        next_node: the next matrix (V x V) where next_node[a][b] is the vertex after a on the path to b

    Returns:
        A list of vertex indices representing the path from u to v (inclusive).
        Returns an empty list if no path exists.
    """
    if next_node[u][v] is None:
        return []  # no path

    path = [u]
    current = u
    # Walk using next pointers until we reach v
    while current != v:
        current = next_node[current][v]
        if current is None:
            # path broken (shouldn't happen if next_node is consistent), return empty
            return []
        path.append(current)
    return path


# Example runnable block
if __name__ == "__main__":
    # Example graph:
    #   0 -> 1 (3)
    #   0 -> 2 (8)
    #   0 -> 4 (-4)
    #   1 -> 3 (1)
    #   1 -> 4 (7)
    #   2 -> 1 (4)
    #   3 -> 0 (2)
    #   3 -> 2 (-5)
    #   4 -> 3 (6)
    #
    # This example includes negative edges but no negative cycles.
    #
    # Adjacency matrix representation:
    # Use None for no direct edge, numeric weight for edge.
    graph = [
        [0,    3,    8,   None, -4],
        [None, 0,    None, 1,    7],
        [None, 4,    0,   None, None],
        [2,    None, -5,   0,   None],
        [None, None, None, 6,    0],
    ]

    dist_matrix, next_matrix = floyd_warshall(graph)

    V = len(graph)
    print("All-pairs shortest distances (INF means no path):")
    for i in range(V):
        row = []
        for j in range(V):
            d = dist_matrix[i][j]
            row.append("INF" if d == INF else f"{d:.1f}")
        print("  ", row)

    print("\nExample of path reconstruction:")
    pairs_to_test = [(0, 3), (3, 2), (0, 2), (1, 4), (4, 0)]
    for (a, b) in pairs_to_test:
        path = reconstruct_path(a, b, next_matrix)
        if path:
            # display path and distance
            print(f"  Path {a} -> {b}: {path}  Distance: {dist_matrix[a][b]:.1f}")
        else:
            print(f"  No path from {a} to {b}.")
