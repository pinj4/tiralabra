import io
import sys
import unittest
from unittest import mock
from main import main
import dijkstra
import ida_star

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch('main.input', return_value = "q")
    def test_input_q_breaks_loop(self, input):
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "goodbye\n")
    
    @mock.patch('main.input', return_value = "1")
    def test_gets_the_right_map(self, input):
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("4\n@@@@\n@...\n@...\n@...\n", output.getvalue())
    
    @mock.patch('main.input', return_value = "10")
    def test_doesnt_get_a_file_that_doesnt_exists(self, input):
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "choose a number between 1-4\n")
    
    @mock.patch('main.input', create=True)
    def test_start_row_out_of_range_works(self, input):
        input.side_effect = ["1", "10"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("row is out of range", output.getvalue())

    @mock.patch('main.input', create=True)
    def test_node_unavailable(self, input):
        input.side_effect = ["1", "2", "0"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("node is unavailable", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_no_available_nodes(self, input):
        input.side_effect = ["1", "1"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("no available nodes", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_start_and_end_nodes_cant_be_same(self, input):
        input.side_effect = ["1", "2", "6", "2", "6"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Choose different points", output.getvalue())
        

