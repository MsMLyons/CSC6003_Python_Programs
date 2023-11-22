""" 
File: test_lyonsm_module_4.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 4
Date Created: 2023-11-20
Date Updated: 2023-11-21

Description: 

This unit test tests the functionality of the classes and methods
in the assignment for module 4. 
"""

import unittest
from unittest.mock import patch
from lyonsm_module_4 import Rectangle, Parallelepiped

class TestRectangle(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 10])
    def test_perimeter(self, mock_input):  
        rect = Rectangle()  
        self.assertEqual(rect.perimeter(), 30)  

    @patch('builtins.input', side_effect=[5, 10])
    def test_area(self, mock_input): 
        rect = Rectangle()  
        self.assertEqual(rect.area(), 50)  

class TestParallelepiped(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 10, 4])
    def test_volume(self, mock_input):  
        parallelepiped = Parallelepiped()  
        self.assertEqual(parallelepiped.volume(), 200)  

if __name__ == "__main__":
    unittest.main()