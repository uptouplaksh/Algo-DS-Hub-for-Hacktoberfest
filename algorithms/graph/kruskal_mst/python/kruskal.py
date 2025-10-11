"""
=====================================================
   Kruskal's Algorithm — Minimum Spanning Tree (MST)
=====================================================

📘 Description:
This Python module implements Kruskal's Algorithm to find the
Minimum Spanning Tree (MST) of a connected, undirected,
and weighted graph.

Kruskal’s algorithm is a **greedy algorithm** that sorts all edges
in ascending order of weight and picks the smallest edge that
does not form a cycle — using the Union-Find data structure.

🧮 Time Complexity: O(E log E)
   (Sorting edges dominates; Union-Find operations are nearly O(1))
💾 Space Complexity: O(V)
"""

# ---------------------------------------------------------------
# 🧩 Disjoint Set (Union-Find) Implementation
# ---------------------------------------------------------------
class DisjointSet:
    """Union-Find structure with path compression and union by rank."""

    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        """Finds the representative (root) of the set that item belongs to."""
        if self.parent[item] != item:
            # Path compression
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        """Unites two sets by rank."""
        root1 = self.find(set1)
        root2 = self.find(set2)

        # Attach smaller rank tree under root of higher rank tree
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


# ---------------------------------------------------------------
# ⚙️ Kruskal's Algorithm Implementation
# ---------------------------------------------------------------
def kruskal_mst(vertices, edges):
    """
    Function to perform Kruskal's Algorithm and return MST.

    Args:
        vertices (list): List of vertices in the graph.
        edges (list): List of edges (u, v, weight).

    Returns:
        mst (list): List of edges in the Minimum Spanning Tree.
        total_cost (int/float): Sum of weights in the MST.
    """
    # Step 1: Sort all edges in non-decreasing order of weight
    edges.sort(key=lambda edge: edge[2])

    # Step 2: Create disjoint sets for all vertices
    ds = DisjointSet(vertices)

    mst = []
    total_cost = 0

    # Step 3: Iterate over edges
    for u, v, weight in edges:
        # Find roots of the sets to which u and v belong
        root_u = ds.find(u)
        root_v = ds.find(v)

        # If including this edge doesn't cause a cycle
        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            ds.union(root_u, root_v)

    return mst, total_cost


# ---------------------------------------------------------------
# 🧩 Runnable Example
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("🔹 Kruskal's Algorithm — Minimum Spanning Tree 🔹\n")

    # Example Graph (Undirected, Weighted)
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 4),
        ('C', 'D', 2),
        ('D', 'E', 2),
        ('C', 'E', 5)
    ]

    # Run Kruskal's algorithm
    mst, total_cost = kruskal_mst(vertices, edges)

    print("✅ Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"  {u} -- {v}  (weight: {weight})")

    print(f"\n💰 Total Cost of MST: {total_cost}")
