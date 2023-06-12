import unittest
import map_file
import dijkstra

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.map = map_file.Map("map_4.map")
        graph = self.map.get_graph()
        n = self.map.map_width
        self.dijkstra = dijkstra.Dijkstra(graph,n)
    
    def test_shortest_route_correct(self):
        result = self.dijkstra.dijkstra()
        self.assertEqual(result, 2.8284271247461903)