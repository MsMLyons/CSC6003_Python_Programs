import unittest
from unittest.mock import patch
from rectangle import Rectangle, Parallelepiped

class TestRectangle(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 10])
    def test_perimeter(self, mock_input):  # include the extra argument here
        rect = Rectangle()  # create an instance with mock user input
        self.assertEqual(rect.perimeter(), 30)  # check that perimeter is calculated correctly

    @patch('builtins.input', side_effect=[5, 10])
    def test_area(self, mock_input): # include the extra argument here
        rect = Rectangle()  # create an instance with mock user input
        self.assertEqual(rect.area(), 50)  # check that area is calculated correctly

class TestParallelepiped(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 10, 4])
    def test_volume(self, mock_input):  # include the extra argument here
        parallelepiped = Parallelepiped()  # create an instance with mock user input
        self.assertEqual(parallelepiped.volume(), 200)  # check that volume is calculated correctly

if __name__ == "__main__":
    unittest.main()