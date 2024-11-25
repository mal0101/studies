import unittest
from Djikstra import djikstra


class DjikstraTest(unittest.TestCase):
    def test_connected_graph(self):
        graph = {
            'U': [('V', 0), ('W', 2), ('X', 0), ('X', 1), ('X', 0)],
            'V': [('V', 2), ('W', 0), ('X', 3), ('X', 0), ('X', 0)],
            'W': [('V', 0), ('U', 3), ('X', 0), ('Y', 4), ('Z', 0)],
            'X': [('U', 1), ('V', 0), ('W', ), ('Y', 1)],
            'Y': [('X', 1), ('W', 1), ('Z', 1)],
            'Z': [('W', 5), ('Y', 1)],
        }

        actual = djikstra(graph, 'X')
        expected = {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
        assert actual == expected