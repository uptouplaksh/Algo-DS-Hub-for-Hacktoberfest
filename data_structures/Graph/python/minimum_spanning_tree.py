"""
minimum_spanning_tree.py

Implementation of Kruskal's Minimum Spanning Tree (MST) algorithm.

Time Complexity:
  - Sorting edges: O(E log E)
  - Union-Find operations: O(E α(V)) where α is the inverse Ackermann function
Overall: O(E log E)

Space Complexity:
  - O(V + E) to store edges and Union-Find data.
"""

class UnionFind:
    """Union-Find (Disjoint Set) with path compression and union by rank."""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        # attach smaller rank under larger rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def kruskal_mst(num_vertices, edges):
    """
    Compute the MST of an undirected, connected, weighted graph.

    Args:
        num_vertices (int): vertices labeled 0..num_vertices-1
        edges (List[tuple(weight, u, v)]): each edge as (weight, u, v)

    Returns:
        mst_edges (List[tuple(u, v, weight)]): edges in the MST
        total_weight (int/float): sum of weights in the MST
    """
    # sort edges by weight
    sorted_edges = sorted(edges, key=lambda e: e[0])
    uf = UnionFind(num_vertices)

    mst_edges = []
    total_weight = 0

    for w, u, v in sorted_edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            if len(mst_edges) == num_vertices - 1:
                break

    return mst_edges, total_weight


if __name__ == "__main__":
    # Sample graph
    sample_edges = [
        (1, 0, 1),
        (3, 0, 2),
        (4, 1, 2),
        (2, 1, 3),
        (5, 2, 3),
        (7, 2, 4),
        (6, 3, 4),
    ]
    num_vertices = 5

    mst, weight = kruskal_mst(num_vertices, sample_edges)
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"  {u} -- {v} (weight {w})")
    print(f"Total weight of MST: {weight}")
