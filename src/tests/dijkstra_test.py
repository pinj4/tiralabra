import unittest
from math import inf
import map_file
import dijkstra

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_finds_no_route(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        n = map2.map_width
        d = dijkstra.Dijkstra(graph, n, 8, 20)
        result = d.dijkstra()
        self.assertEqual(result, inf)
    
    def test_doesnt_get_a_full_path_if_there_isnt_one(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        n = map2.map_width
        d = dijkstra.Dijkstra(graph, n, 8, 20)
        d.dijkstra()
        path = d.get_path()
        self.assertEqual([8], path)
    
    ## shortest routes
    def test_shortest_route_correct_map1(self):
        map1 = map_file.Map("map_1.map")
        graph = map1.get_graph()
        n = map1.map_width
        d = dijkstra.Dijkstra(graph, n, 5, 15)
        result = d.dijkstra()
        self.assertEqual(result, 2.8284271247461903)

    def test_shortest_route_correct_map2(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        n = map2.map_width
        d = dijkstra.Dijkstra(graph, n, 9, 63)
        result = d.dijkstra()
        self.assertEqual(result, 9.071067811865476)
    
    def test_shortest_route_correct_map3(self):
        map3 = map_file.Map("map_3.map")
        graph = map3.get_graph()
        n = map3.map_width
        d = dijkstra.Dijkstra(graph, n, 0, 255)
        result = d.dijkstra()
        self.assertEqual(result, 22.384776310850242)
    
    def test_shortest_route_correct_map4(self):
        map4 = map_file.Map("map_4.map")
        graph = map4.get_graph()
        n = map4.map_width
        d = dijkstra.Dijkstra(graph, n, 0, 1023)
        result = d.dijkstra()
        self.assertEqual(result, 45.59797974644665)
    
    def test_shortest_route_correct_map5(self):
        map5 = map_file.Map("map_5.map")
        graph = map5.get_graph()
        n = map5.map_width
        d = dijkstra.Dijkstra(graph, n, 0, 4095)
        result = d.dijkstra()
        self.assertEqual(result, 90.2670273047587)
    
    ##right paths
    def test_gets_the_right_path_map1(self):
        map1 = map_file.Map("map_1.map")
        graph = map1.get_graph()
        n = map1.map_width
        d = dijkstra.Dijkstra(graph, n, 5, 15)
        d.dijkstra()
        path = d.get_path()
        self.assertEqual([5, 10, 15], path)

    def test_gets_the_right_path_map2(self):
        map2 = map_file.Map("map_2.map")
        graph = map2.get_graph()
        n = map2.map_width
        d = dijkstra.Dijkstra(graph, n, 9, 63)
        d.dijkstra()
        path = d.get_path()
        self.assertEqual([9, 18, 26, 35, 44, 53, 54, 63], path)

    def test_gets_the_right_path_map3(self):
        map3 = map_file.Map("map_3.map")
        graph = map3.get_graph()
        n = map3.map_width
        d = dijkstra.Dijkstra(graph, n, 0, 255)
        d.dijkstra()
        path = d.get_path()
        self.assertEqual([0, 1, 18, 35, 52, 69, 86, 103, 120, 137,
                        154, 171, 187, 204, 205, 222, 238, 255], path)
    
    def test_gets_the_right_path_map4(self):
        map4 = map_file.Map("map_4.map")
        graph = map4.get_graph()
        n = map4.map_width
        d = dijkstra.Dijkstra(graph, n, 0, 1023)
        d.dijkstra()
        path = d.get_path()
        self.assertEqual([0, 33, 66, 98, 131, 163, 196, 228, 261, 294,
                        327, 360, 393, 426, 459, 492, 525, 558, 591,
                        592, 625, 658, 691, 724, 757, 790, 823, 824,
                        857, 858, 891, 924, 957, 990, 1023], path)
    
    def test_gets_the_right_path_map5(self):
        map5 = map_file.Map("map_5.map")
        graph = map5.get_graph()
        n = map5.map_width
        d = dijkstra.Dijkstra(graph, n, 0, 4095)
        d.dijkstra()
        path = d.get_path()
        self.assertEqual( [0, 65, 130, 195, 260, 261, 326, 391, 456,
                        521, 586, 651, 716, 781, 846, 911, 976, 1041,
                        1106, 1171, 1236, 1301, 1366, 1431, 1496, 1561,
                        1626, 1691, 1756, 1821, 1886, 1951, 2016, 2081,
                        2146, 2211, 2276, 2341, 2406, 2407, 2472, 2537,
                        2602, 2667, 2731, 2796, 2861, 2926, 2991, 3056,
                        3121, 3186, 3251, 3316, 3381, 3445, 3510, 3575,
                        3640, 3705, 3770, 3835, 3900, 3965, 4030, 4095], path)

