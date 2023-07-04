import unittest
from math import inf
import time
import map_file
import ida_star

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_finds_no_route(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        i = ida_star.IdaStar(graph, 8, 20, map2.map_width)
        result, path = i.ida_star()
        self.assertEqual((result, path), (inf, []))
    
    ## shortest routes & paths
    def test_finds_shortest_route_map1(self):
        map1 = map_file.Map("map_1.map")
        graph = map1.get_graph()
        i = ida_star.IdaStar(graph, 5, 15, map1.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, 2.8284271247461903)
        self.assertEqual([5, 10, 15], path)


    def test_shortest_route_correct_map2(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        i = ida_star.IdaStar(graph, 9, 63, map2.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, 9.071067811865476)
        self.assertEqual([9, 18, 27, 35, 44, 53, 54, 63], path)
    
    def test_shortest_route_correct_map3(self):
        map3 = map_file.Map("map_3.map")
        graph = map3.get_graph()
        i = ida_star.IdaStar(graph, 0, 255, map3.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, 22.384776310850242)
        self.assertEqual([0, 1, 18, 35, 52, 69, 86, 103, 120, 137,
                        154, 171, 187, 204, 205, 222, 238, 255], path)
    
    def test_shortest_route_correct_map4(self):
        map4 = map_file.Map("map_4.map")
        graph = map4.get_graph()
        i = ida_star.IdaStar(graph, 0, 1023, map4.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, 45.59797974644665)
        self.assertEqual([0, 33, 66, 98, 131, 163, 196, 228, 261, 294, 327,
                        360, 393, 426, 459, 492, 525, 558, 591, 592, 625,
                        658, 691, 724, 757, 790, 823, 856, 857, 858, 891,
                        924, 957, 990, 1023], path)
    
    def test_shortest_route_correct_map5(self):
        map5 = map_file.Map("map_5.map")
        graph = map5.get_graph()
        i = ida_star.IdaStar(graph, 0, 4095, map5.map_width)
        result, path = i.ida_star()
        self.assertEqual(result, 90.2670273047587)
        self.assertEqual( [0, 65, 130, 195, 260, 261, 326, 391, 456, 521, 586,
                        651, 716, 781, 846, 911, 976, 1041, 1106, 1171, 1236,
                        1301, 1366, 1431, 1495, 1560, 1625, 1690, 1755, 1820,
                        1885, 1950, 2015, 2080, 2145, 2210, 2275, 2340, 2405,
                        2470, 2535, 2600, 2665, 2730, 2795, 2860, 2925, 2990,
                        3055, 3120, 3185, 3250, 3315, 3316, 3381, 3445, 3510,
                        3575, 3640, 3705, 3770, 3835, 3900, 3965, 4030, 4095], path)
    