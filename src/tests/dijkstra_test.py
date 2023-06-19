import unittest
from math import inf
import map_file
import dijkstra

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    def test_shortest_route_correct(self):
        map3 = map_file.Map("map_3.map")
        graph = map3.get_graph()
        n = map3.map_width
        d = dijkstra.Dijkstra(graph, n, 5, 15)
        result = d.dijkstra()
        self.assertEqual(result, 2.8284271247461903)
    
    def test_finds_no_route(self):
        map4 = map_file.Map("map_4.map")
        graph = map4.get_graph()
        n = map4.map_width
        d = dijkstra.Dijkstra(graph, n, 8, 20)
        result = d.dijkstra()
        self.assertEqual(result, inf)

