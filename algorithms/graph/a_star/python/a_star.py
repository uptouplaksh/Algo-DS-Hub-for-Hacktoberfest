"""
A* (A-Star) Search Algorithm Implementation in Python

Time Complexity:
- Worst Case: O(E log V) due to priority queue operations.
- With a good heuristic: much faster in practice.

Space Complexity:
- O(V) where V = number of vertices (for storing scores and open set).
"""

import heapq


def a_star(start, goal, graph, heuristic):
    """
    A* Search Algorithm

    :param start: Starting node
    :param goal: Goal node
    :param graph: Adjacency list with edge costs
                  Example: {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, ...}
    :param heuristic: Function estimating cost from a node to the goal
    :return: Shortest path as a list of nodes, or None if no path exists
    """
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), start))  # (f_score, node)

    came_from = {}  # Path reconstruction map

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        # Get node with lowest f-score efficiently
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                # Push new state into the heap
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


def reconstruct_path(came_from, current):
    """ Reconstruct path from start to goal """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


# -------------------------------
# Example 1: Simple Graph
# -------------------------------
if __name__ == "__main__":
    print("Example 1: Simple Graph")
    graph1 = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'C': 1, 'D': 3},
        'C': {'A': 3, 'B': 1, 'D': 1},
        'D': {'B': 3, 'C': 1}
    }

    def heuristic1(node, goal):
        h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
        return h[node]

    path1 = a_star('A', 'D', graph1, heuristic1)
    print(f"Shortest path A → D: {path1}\n")

    # -------------------------------
    # Example 2: Weighted Graph with multiple routes
    # -------------------------------
    print("Example 2: Weighted Graph with multiple routes")
    graph2 = {
        'S': {'A': 2, 'B': 5},
        'A': {'S': 2, 'B': 2, 'C': 4},
        'B': {'S': 5, 'A': 2, 'C': 1, 'D': 7},
        'C': {'A': 4, 'B': 1, 'D': 3, 'G': 5},
        'D': {'B': 7, 'C': 3, 'G': 2},
        'G': {}
    }

    def heuristic2(node, goal):
        # Example heuristic (straight-line guesses)
        h = {'S': 7, 'A': 6, 'B': 5, 'C': 2, 'D': 1, 'G': 0}
        return h[node]

    path2 = a_star('S', 'G', graph2, heuristic2)
    print(f"Shortest path S → G: {path2}\n")

    # -------------------------------
    # Example 3: No Path Available
    # -------------------------------
    print("Example 3: No Path Available")
    graph3 = {
        'X': {'Y': 2},
        'Y': {'X': 2},
        'Z': {}  # Isolated node, unreachable
    }

    def heuristic3(node, goal):
        h = {'X': 5, 'Y': 3, 'Z': 0}
        return h[node]

    path3 = a_star('X', 'Z', graph3, heuristic3)
    print(f"Shortest path X → Z: {path3}")  # Expected: None
