import unittest
import math
import os
import sys 
sys.path.insert(1, os.path.join(sys.path[0], "..")) 
from circle import *
class RectangleTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertAlmostEqual(area(10), math.pi * 10 * 10, 2)
        self.assertAlmostEqual(area(5), math.pi * 5 * 5, 2)
        self.assertAlmostEqual(area(1), math.pi * 1 * 1, 2)
    
    def test_area_zero_radius(self):
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
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10, 2)
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5, 2)
        self.assertAlmostEqual(perimeter(1), 2 * math.pi * 1, 2)

    def test_perimeter_zero_radius(self):
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