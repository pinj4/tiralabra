import unittest
from math import inf
import map_file
import ida_star

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    def test_finds_shortest_route(self):
        map1 = map_file.Map("map_1.map")
        graph = map1.get_graph()
        i = ida_star.IdaStar(graph, 5, 15, map1.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, 2.8284271247461903)
    
    def test_finds_no_route(self):
        map3 = map_file.Map("map_3.map")
        graph = map3.get_graph()
        i = ida_star.IdaStar(graph, 0, 1023, map3.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, inf)