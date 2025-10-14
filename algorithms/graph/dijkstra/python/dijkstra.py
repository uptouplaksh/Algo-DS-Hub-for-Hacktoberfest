import heapq

def dijkstra(graph, start):
    """
    Enhanced Dijkstra's algorithm to return both shortest distances and paths.

    Parameters:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      Example: {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, ...}
        start (str): The starting node.

    Returns:
        distances (dict): Shortest distance from start to each node.
        previous_nodes (dict): Map of each node to its previous node in the shortest path.
    """
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    # Min-heap priority queue
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip outdated entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def reconstruct_path(previous_nodes, start, target):
    """
    Reconstructs the shortest path from start to target using previous_nodes.
    """
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    if path[0] == start:
        return path
    return []  # Return empty list if no path exists


# Example Usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }

    start_node = 'A'
    target_node = 'D'

    distances, previous_nodes = dijkstra(graph, start_node)
    shortest_path = reconstruct_path(previous_nodes, start_node, target_node)

    print("Shortest distances:", distances)
    print(f"Shortest path from {start_node} to {target_node}: {' -> '.join(shortest_path)}")
