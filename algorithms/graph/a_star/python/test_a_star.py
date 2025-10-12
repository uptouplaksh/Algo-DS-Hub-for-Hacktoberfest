""" Unit tests for the A* search algorithm. """

import unittest
from a_star import a_star


class TestAStarSearch(unittest.TestCase):
    """comprehensive unit tests for A* search algorithm"""
    
    def test_path_exists_simple_graph(self):
        """
        test A* on a simple graph where a path exists
        
        graph structure:
        A --1--> B --1--> C --1--> D
        |        |        |
        3        2        1
        |        |        |
        +--------+--------+
        
        expected: A* should find the shortest path A → B → C → D
        """
        # Define graph (adjacency list with costs)
        graph = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'C': 1, 'D': 3},
            'C': {'A': 3, 'B': 1, 'D': 1},
            'D': {'B': 3, 'C': 1}
        }
        
        # Heuristic: estimated distance to goal D
        def heuristic(node, goal):
            h_values = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
            return h_values[node]
        
        # Run A* search from A to D
        path = a_star('A', 'D', graph, heuristic)
        
        # Assertions
        self.assertIsNotNone(path, "Path should exist from A to D")
        self.assertEqual(path[0], 'A', "Path should start at A")
        self.assertEqual(path[-1], 'D', "Path should end at D")
        # Expected optimal path: A → B → C → D
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
    
    def test_unreachable_goal(self):
        """
        test A* when goal is unreachable (disconnected graph)
        
        graph structure:
        X <---> Y    Z (isolated)
        
        expected: A* should return None when trying to reach Z from X
        """
        # Disconnected graph
        graph = {
            'X': {'Y': 2},
            'Y': {'X': 2},
            'Z': {}  # Z is isolated, unreachable from X or Y
        }
        
        # Heuristic function
        def heuristic(node, goal):
            h_values = {'X': 5, 'Y': 3, 'Z': 0}
            return h_values[node]
        
        # try to find path from X to Z
        path = a_star('X', 'Z', graph, heuristic)
        
        # should return None since Z is unreachable
        self.assertIsNone(path, "Path should be None when goal is unreachable")
    
    def test_start_equals_goal(self):
        """
        test when start node is the same as goal node.
        
        expected: should return a path containing just the start node
        """
        graph = {
            'A': {'B': 1},
            'B': {'A': 1}
        }
        
        def heuristic(node, goal):
            return 0  # Already at goal
        
        path = a_star('A', 'A', graph, heuristic)
        
        # Should return path with just the start node
        self.assertIsNotNone(path)
        self.assertEqual(path, ['A'])
    
    def test_multiple_routes_finds_shortest(self):
        """
        test that A* finds the shortest path when multiple routes exist.
        
        graph:
        S --2--> A --4--> C --5--> G
        |        |        |
        5        2        1
        |        |        |
        +------> B -------+
        
        expected: should find optimal path S → A → B → C → G
        """
        graph = {
            'S': {'A': 2, 'B': 5},
            'A': {'S': 2, 'B': 2, 'C': 4},
            'B': {'S': 5, 'A': 2, 'C': 1, 'D': 7},
            'C': {'A': 4, 'B': 1, 'D': 3, 'G': 5},
            'D': {'B': 7, 'C': 3, 'G': 2},
            'G': {}
        }
        
        def heuristic(node, goal):
            # straight line distance estimates
            h_values = {'S': 7, 'A': 6, 'B': 5, 'C': 2, 'D': 1, 'G': 0}
            return h_values[node]
        
        path = a_star('S', 'G', graph, heuristic)
        
        # Verify path exists and is optimal
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 'S')
        self.assertEqual(path[-1], 'G')
        # A* should find the shortest path
        self.assertEqual(path,['S','A','B','C','G'])


if __name__ == '__main__':
    unittest.main()
