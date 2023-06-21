import unittest
from math import inf
import map_file
import dijkstra

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    def test_shortest_route_correct(self):
        map1 = map_file.Map("map_1.map")
        graph = map1.get_graph()
        n = map1.map_width
        d = dijkstra.Dijkstra(graph, n, 5, 15)
        result = d.dijkstra()
        self.assertEqual(result, 2.8284271247461903)
    
    def test_finds_no_route(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        n = map2.map_width
        d = dijkstra.Dijkstra(graph, n, 8, 20)
        result = d.dijkstra()
        self.assertEqual(result, inf)

