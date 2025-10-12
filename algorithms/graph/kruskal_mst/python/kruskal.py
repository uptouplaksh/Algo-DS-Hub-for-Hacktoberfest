"""
Kruskal's Algorithm Implementation in Python

Finds the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph.
Uses Union-Find (Disjoint Set) to efficiently detect cycles.

"""

class UnionFind:
    """
    Union-Find (Disjoint Set) data structure with path compression and union by rank.
    Used to efficiently detect cycles when adding edges to the MST.
    """
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n           # Rank helps optimize unions

    def find(self, x):
        """Finds the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Unions the sets containing x and y.
        Returns False if x and y are already connected (cycle detected), True otherwise.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Edge would form a cycle

        # Union by rank to keep trees shallow
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal(n, edges):
    """
    Kruskal's Algorithm to find Minimum Spanning Tree (MST)

    Parameters:
    n (int): Number of vertices (0-indexed: 0 to n-1)
    edges (list of tuples): Each edge as (weight, u, v)

    Returns:
    mst (list of tuples): Edges in the MST in the form (u, v, weight)
    total_weight (int/float): Total weight of the MST

    Overall Complexity:
    Time Complexity: O(E log E), dominated by edge sorting
    Space Complexity: O(V + E), for Union-Find arrays and MST storage
    """
    # Step 1: Sort edges by weight
    edges.sort()

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    # Step 2: Iterate over edges and add them if they don't form a cycle
    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    # Edge case: graph not connected
    if len(mst) != n - 1:
        print("Warning: The graph is not connected; MST may not include all vertices.")

    return mst, total_weight


# ------------------------------
# Example Usage
# ------------------------------
if __name__ == "__main__":
    # Example graph with 4 vertices (0-3)
    # Each edge is a tuple: (weight, vertex1, vertex2)
    edges = [
        (1, 0, 1),
        (3, 0, 2),
        (3, 1, 2),
        (6, 1, 3),
        (2, 2, 3)
    ]
    n = 4

    mst, total_weight = kruskal(n, edges)

    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")

