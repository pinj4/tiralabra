import io
import sys
import unittest
from unittest import mock
from main import main

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
    
    @mock.patch('main.input', return_value = "3")
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
        self.assertEqual(output.getvalue(), "choose a number between 1-6\n")
    
    @mock.patch('main.input', create=True)
    def test_start_row_out_of_range_works(self, input):
        input.side_effect = ["4", "10"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("that row is out of range", output.getvalue())

    @mock.patch('main.input', create=True)
    def test_start_node_unavailable(self, input):
        input.side_effect = ["4", "1", "0"]
        output = io.StringIO()
        sys.stdout = output
        main()
        sys.stdout = sys.__stdout__
        self.assertIn("that node is unavailable", output.getvalue())



