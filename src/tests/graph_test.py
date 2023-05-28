import unittest
import graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = graph.Graph(4)
    

    def test_matrix_dimensions_are_correct(self):
        result = self.graph.matrix
        matrix = [['x', 'x', 'x', 'x'],['x', 'x', 'x', 'x'],['x', 'x', 'x', 'x'],['x', 'x', 'x', 'x']]
        self.assertEqual(result, matrix)

