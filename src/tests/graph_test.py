import unittest
import graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = graph.Graph(4)
    

    def test_matrix_dimensions_are_correct(self):
        result = self.graph.matrix
        matrix = [['x', 'x', 'x', 'x'],['x', 'x', 'x', 'x'],['x', 'x', 'x', 'x'],['x', 'x', 'x', 'x']]
        self.assertEqual(result, matrix)
    
    def test_graph_dimensions_are_correct(self):
        result = self.graph.graph
        graph = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.assertEqual(result, graph)
    
    def test_graph_weeights_sets_up_right(self):
        result = self.graph.weights
        weights = {
            0:1000000000, 1:1000000000, 2:1000000000, 3:1000000000, 4:1000000000, 5:1000000000, 6:1000000000, 7:1000000000, 
            8:1000000000, 9:1000000000, 10:1000000000, 11:1000000000, 12:1000000000, 13:1000000000, 14:1000000000, 15:1000000000,
            16:1000000000
            }
        self.assertEqual(result, weights)
    
    def test_graph_add_edge_works(self):
        self.graph.weights[1] = 3
        self.graph.weights[2] = 4
        self.graph.add_edge(1, 2, 1, 1)
        graph = [[],[(2,4)],[(1,3)],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        result = self.graph.graph
        self.assertEqual(result, graph)
    
    def test_graph_add_edge_doesnt_work_with_negatives(self):
        self.graph.weights[-1] = 3
        self.graph.weights[-2] = 4
        self.graph.add_edge(-1, -2, 1, 1)
        graph = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        result = self.graph.graph
        self.assertEqual(result, graph)
    
    def test_graph_add_edge_doesnt_work_with_x_nodes(self):
        self.graph.weights[1] = 3
        self.graph.weights[2] = 4
        self.graph.add_edge(1, 2, "x", "x")
        graph = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        result = self.graph.graph
        self.assertEqual(result, graph)
    
    




