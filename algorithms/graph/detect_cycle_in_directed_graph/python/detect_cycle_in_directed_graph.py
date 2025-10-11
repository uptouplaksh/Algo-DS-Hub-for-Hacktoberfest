# Problem: Detect Cycle in a Directed Graph
# -----------------------------------------
# Given a directed graph with V vertices and a list of edges, determine whether
# the graph contains a cycle or not.
#
# The function should return True if there is a cycle, otherwise False.
#
# Examples:
#
# Example 1:
# Input:  V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]
# Diagram: 0 → 1 → 2 → 0 forms a cycle
# Output:  True
# Explanation: The directed edges create a cycle (0 → 1 → 2 → 0).
#
# Example 2:
# Input:  V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
# Diagram: 0 → 1 → 2 → 3 has no cycles
# Output:  False
# Explanation: The graph is acyclic as all edges lead forward without looping back.
#
# -----------------------------------------

# Helper function for DFS-based cycle detection
def isCyclicUtil(adj, u, visited, recStack):
    """
    Utility function to perform DFS and detect cycles.
    
    Args:
        adj (list): Adjacency list representation of the graph.
        u (int): The current vertex being visited.
        visited (list): A boolean list to keep track of visited vertices.
        recStack (list): A boolean list to keep track of vertices in the current recursion stack.
        
    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    # If the node is already in the current recursion stack, a cycle is detected
    if recStack[u]:
        return True

    # If the node is already visited and not part of the recursion stack, skip it
    if visited[u]:
        return False

    # Mark the current node as visited and add it to the recursion stack
    visited[u] = True
    recStack[u] = True

    # Recur for all the adjacent vertices
    for v in adj[u]:
        if isCyclicUtil(adj, v, visited, recStack):
            return True

    # Remove the node from the recursion stack before returning
    recStack[u] = False
    return False


# Function to build adjacency list from edge list
def constructadj(V, edges):
    """
    Constructs an adjacency list from a list of edges.
    
    Args:
        V (int): The number of vertices.
        edges (list of lists): A list of directed edges.
        
    Returns:
        list: The adjacency list representation of the graph.
    """
    adj = [[] for _ in range(V)]  # Create a list for each vertex
    for u, v in edges:
        adj[u].append(v)  # Add directed edge from u to v
    return adj


# Main function to detect cycle in the directed graph
def isCyclic(V, edges):
    """
    Detects if a cycle exists in a directed graph.
    
    Args:
        V (int): The number of vertices.
        edges (list of lists): A list of directed edges.
        
    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    """
    adj = constructadj(V, edges)
    visited = [False] * V      # To track visited vertices
    recStack = [False] * V     # To track vertices in the current DFS path

    # Try DFS from each vertex, especially for disconnected graphs
    for i in range(V):
        if not visited[i] and isCyclicUtil(adj, i, visited, recStack):
            return True  # Cycle found
    return False  # No cycle found


# Example usage
if __name__ == "__main__":
    # Example 1: Graph with a cycle
    V1 = 4
    edges1 = [[0, 1], [1, 2], [2, 0], [2, 3]]
    print(f"Graph 1 contains a cycle: {isCyclic(V1, edges1)}")  # Expected: True

    # Example 2: Graph without a cycle
    V2 = 4
    edges2 = [[0, 1], [0, 2], [1, 2], [2, 3]]
    print(f"Graph 2 contains a cycle: {isCyclic(V2, edges2)}")  # Expected: False
