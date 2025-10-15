# Detect Cycle in a Directed Graph using DFS

# Explanation of the algorithm:
# 1. We use Depth First Search (DFS) to traverse the graph.
# 2. We maintain two sets: one for visited vertices and another for the recursion stack.
# 3. If we encounter a vertex that has already been visited and is in the recursion stack,
#    it indicates a cycle in the graph.

# DFS Time Complexity:  O(|V|+|E|), where |V| is the number of vertices and |E| is the number of edges.
# DFS Space Complexity: O(|V|) to store the stack of vertices on the current search path as well as the set of already-visited vertices.
# Source: https://en.wikipedia.org/wiki/Depth-first_search

# Example graphs:

graph_cycle = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],  
    "D": ["E"],
    "E": ["C"],  # This edge creates a cycle (C -> D -> E -> C)
    "F": ["G"],
    "G": []
}

graph_no_cycle = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],  
    "D": ["E"]
}

def check_for_cycle(graph: dict[str, list[str]]) -> bool:
    """
    Check for a cycle in a directed graph using DFS.
    Args:
        graph (dict): A dictionary representing a graph where keys are vertices and values are lists of adjacent vertices.
    Returns:
        bool: True if a cycle is detected, False otherwise.
    """

    visited = set()
    recursion_stack = set()

    def dfs(vertex: str) -> bool:
        """
        Perform a DFS search.
        Args:
            vertex: Vertex to be checked
        Returns:
            bool: True if a cycle is detected, False otherwise.
        """

        if vertex in recursion_stack:
            return True
        if vertex in visited:
            return False
        
        visited.add(vertex)
        recursion_stack.add(vertex)

        for neighbor in graph.get(vertex, []):
            if dfs(neighbor):
                return True
        
        recursion_stack.remove(vertex)
        return False
    
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True
    return False

def main():
    # Test the function with both graphs
    print("Graph with cycle:", check_for_cycle(graph_cycle))  # Expected output: True
    print("Graph without cycle:", check_for_cycle(graph_no_cycle))  # Expected output: False

if __name__ == "__main__":
    main()
