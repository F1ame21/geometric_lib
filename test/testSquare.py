import unittest
import math
import os
import sys 
sys.path.insert(1, os.path.join(sys.path[0], "..")) 
from square import *
class RectangleTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertEqual(area(10), 10 * 10)
        self.assertEqual(area(5), 5 * 5)
        self.assertAlmostEqual(area(1.4), 1.4 * 1.4, 2)
    
    def test_area_zero_value(self):
        self.assertRaises(ValueError, area, 0)

    def test_area_negative_value(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -3)
    
    def test_area_types(self):
        self.assertRaises(TypeError, area, 'abc')
        self.assertRaises(TypeError, area, [123, 122])
        self.assertRaises(TypeError, area, True)
    
    def test_perimeter_positive_value(self):
        self.assertEqual(perimeter(10), 4 * 10)
        self.assertEqual(perimeter(5), 4 * 5)
        self.assertAlmostEqual(perimeter(1.4), 4 * 1.4, 2)


    def test_perimeter_zero_value(self):
        self.assertRaises(ValueError, perimeter, 0)

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, perimeter, -1)
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -3)
    
    def test_perimeter_types(self):
        self.assertRaises(TypeError, perimeter, 'abc')
        self.assertRaises(TypeError, perimeter, [123, 122])
        self.assertRaises(TypeError, perimeter, True)
        
    


if __name__ == '__main__':
    unittest.main()