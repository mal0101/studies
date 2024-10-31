# test_bellmanFord.py

import unittest
from FordBellman import bellmanFord  # Adjust if your function is in a different file

class BellmanFordTest(unittest.TestCase):

    def test_basic_graph(self):
        graph = {
            'A': {'B': 4, 'C': 2},
            'B': {'C': 3, 'D': 2, 'E': 3},
            'C': {'B': 1, 'D': 4, 'E': 5},
            'D': {'E': -1},
            'E': {}
        }
        source = 'A'
        expected_distances = {'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 4}
        expected_predecessors = {'A': None, 'B': 'C', 'C': 'A', 'D': 'B', 'E': 'D'}

        distances, predecessors = bellmanFord(graph, source)
        
        self.assertEqual(distances, expected_distances)
        self.assertEqual(predecessors, expected_predecessors)

    def test_negative_cycle(self):
        graph = {
            'A': {'B': 1},
            'B': {'C': -1},
            'C': {'A': -1}
        }
        source = 'A'
        
        with self.assertRaises(AssertionError):  # Expecting an assertion error for negative cycle
            bellmanFord(graph, source)

    def test_disconnected_graph(self):
        graph = {
            'A': {'B': 4},
            'B': {},
            'C': {'D': 3},
            'D': {}
        }
        source = 'A'
        expected_distances = {'A': 0, 'B': 4, 'C': float('inf'), 'D': float('inf')}
        expected_predecessors = {'A': None, 'B': 'A', 'C': None, 'D': None}

        distances, predecessors = bellmanFord(graph, source)
        
        self.assertEqual(distances, expected_distances)
        self.assertEqual(predecessors, expected_predecessors)

if __name__ == '__main__':
    unittest.main()
