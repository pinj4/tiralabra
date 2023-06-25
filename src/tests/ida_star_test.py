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
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        i = ida_star.IdaStar(graph, 8, 20, map2.map_width)
        result, path = i.ida_star()
        self.assertEqual((result, path), (inf, []))
    
    def test_finds_the_right_path(self):
        map1 = map_file.Map("map_1.map")
        graph = map1.get_graph()
        i = ida_star.IdaStar(graph, 5, 15, map1.map_width)
        result, path = i.ida_star()
        self.assertEqual([5, 10, 15], path)