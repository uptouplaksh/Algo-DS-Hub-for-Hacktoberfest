"""
Depth-First Search (DFS) Traversal Algorithm in Python
--------------------------------------------------------
Author: Jatin Vishwakarma

Enhanced Features:
- Handles disconnected graphs
- Returns traversal order as a list
- Optionally tracks parent nodes for each vertex

Complexity Analysis:
- Time Complexity: O(V + E), where V = number of vertices, E = number of edges
- Space Complexity: O(V), for visited tracking, recursion/stack, and parent dictionary
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        # Dictionary to store adjacency list
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add an edge from vertex u to vertex v
        For undirected graphs, also add edge from v to u
        """
        self.graph[u].append(v)

    def dfs_recursive(self, start, visited=None, parent=None, traversal=None):
        """
        Recursive DFS traversal
        Returns:
            traversal (list): vertices in DFS order
            parent (dict): parent of each visited vertex
        """
        if visited is None:
            visited = set()
        if traversal is None:
            traversal = []
        if parent is None:
            parent = {start: None}

        visited.add(start)
        traversal.append(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                parent[neighbor] = start
                self.dfs_recursive(neighbor, visited, parent, traversal)

        return traversal, parent

    def dfs_iterative(self, start):
        """
        Iterative DFS traversal using stack
        Returns:
            traversal (list): vertices in DFS order
        """
        visited = set()
        stack = [start]
        traversal = []
        parent = {start: None}

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                # Track parent for each neighbor
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        parent[neighbor] = node
                        stack.append(neighbor)

        return traversal, parent

    def dfs_full(self):
        """
        Perform DFS on all components of a disconnected graph
        Returns:
            traversal (list): vertices in DFS order for all components
            parent (dict): parent mapping for all vertices
        """
        visited = set()
        full_traversal = []
        full_parent = {}

        for vertex in list(self.graph.keys()):
            if vertex not in visited:
                traversal, parent = self.dfs_recursive(vertex)
                full_traversal.extend(traversal)
                full_parent.update(parent)
                visited.update(traversal)

        return full_traversal, full_parent

# --------------------------
# Runnable Example
# --------------------------
if __name__ == "__main__":
    # Create graph instance
    g = Graph()
    # Add edges
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(4, 5)  # disconnected component

    print("DFS Recursive Traversal starting from vertex 2:")
    traversal, parent = g.dfs_recursive(2)
    print("Traversal Order:", traversal)
    print("Parent Mapping:", parent)

    print("\nDFS Iterative Traversal starting from vertex 2:")
    traversal_iter, parent_iter = g.dfs_iterative(2)
    print("Traversal Order:", traversal_iter)
    print("Parent Mapping:", parent_iter)

    print("\nDFS Full Traversal for Disconnected Graph:")
    full_traversal, full_parent = g.dfs_full()
    print("Traversal Order:", full_traversal)
    print("Parent Mapping:", full_parent)
