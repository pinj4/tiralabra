import unittest
import map_file

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.map = map_file.Map("map_1.map")
    

    def test_create_map_doesnt_work_with_wrong_file_name(self):
        m = map_file.Map("wrong_file.map")
        result = m.create_map()
        self.assertEqual(result, "wrong file")
    
    def test_create_map_works_with_right_file_name(self):
        result = self.map.create_map()
        self.assertEqual(result, "Done")