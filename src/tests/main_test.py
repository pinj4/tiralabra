import io
import sys
import unittest
from unittest import mock
from main import main
import dijkstra
import ida_star
import map_file
import time

class TestGraph(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch('main.input', return_value = "q")
    def test_input_q_breaks_loop_at_the_start(self, input):
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn(output.getvalue(), "goodbye\n")
    

    @mock.patch('main.input', create = True)
    def test_input_q_breaks_loop_when_choosing_the_start_node(self, input):
        input.side_effect = ["1", "2", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("goodbye", output.getvalue())
    
    @mock.patch('main.input', create = True)
    def test_input_q_breaks_loop_when_choosing_the_goal_row(self, input):
        input.side_effect = ["1", "2", "2", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("goodbye", output.getvalue())
    
    @mock.patch('main.input', create = True)
    def test_input_q_breaks_loop_when_choosing_the_goal_node(self, input):
        input.side_effect = ["1", "2", "2", "3", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("goodbye", output.getvalue())
    
    
    @mock.patch('main.input', create=True)
    def test_gets_the_right_map(self, input):
        input.side_effect = ["1", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("4\n@@@@\n@...\n@...\n@...\n", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_doesnt_get_a_file_that_doesnt_exists(self, input):
        input.side_effect = ["10", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("choose a number between 1-5\n", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_start_row_out_of_range_works(self, input):
        input.side_effect = ["1", "10", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("row is out of range", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_goal_row_out_of_range_works(self, input):
        input.side_effect = ["1", "2", "2", "10", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("row is out of range", output.getvalue())

    @mock.patch('main.input', create=True)
    def test_start_node_unavailable(self, input):
        input.side_effect = ["1", "2", "0", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("node is unavailable", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_goal_node_unavailable(self, input):
        input.side_effect = ["1", "2", "2", "4", "1", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("node is unavailable", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_no_available_nodes_star_node(self, input):
        input.side_effect = ["1", "1", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("no available nodes", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_no_available_nodes_goal_node(self, input):
        input.side_effect = ["1", "2", "2", "1", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("no available nodes", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_start_and_end_nodes_cant_be_same(self, input):
        input.side_effect = ["2", "2", "3", "2", "3", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Choose different points", output.getvalue())
    

    @mock.patch('main.input', create=True)
    def test_returns_correct_shortest_routes(self, input):
        input.side_effect = ["2", "2", "2", "7", "7", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("shortest route  7.657", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_found_a_shorter_route(self, input):
        input.side_effect = ["2", "2", "2", "7", "7", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Dijkstra found a shorter route than IDA*\n", output.getvalue())

        
    @mock.patch('main.input', create=True)
    def test_no_route_doesnt_compare_routes(self, input):
        input.side_effect = ["2", "2", "2", "3", "7", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertNotIn(f"Both algorithms found equally short routes\n" and
                            "Dijkstra found a shorter route than IDA*\n" and
                            "IDA* found a shorter route than Dijsktra\n", output.getvalue())
    
    @mock.patch('main.input', create=True)
    def test_found_equal_routes(self, input):
        input.side_effect = ["2", "2", "2", "7", "4", "q"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("Both algorithms found equally short routes\n", output.getvalue())

