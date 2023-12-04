import unittest
import math
import os
import sys 
sys.path.insert(1, os.path.join(sys.path[0], "..")) 
from rectangle import *
class RectangleTestCase(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertEqual(area(10, 10), 10 * 10)
        self.assertEqual(area(3, 4), 3 * 4)
        self.assertEqual(area(4, 3), 4 * 3)
        self.assertAlmostEqual(area(4.5, 3.5), 4.5 * 3.5, 2)
    
    def test_area_zero_value(self):
        self.assertRaises(ValueError, area, 10, 0)
        self.assertRaises(ValueError, area, 0, 10)

    def test_area_negative_value(self):
        self.assertRaises(ValueError, area, -1, 2)
        self.assertRaises(ValueError, area, 2, -3)
        self.assertRaises(ValueError, area, -3, 4)
    
    def test_area_types(self):
        self.assertRaises(TypeError, area, 'abc', 12)
        self.assertRaises(TypeError, area, [123, 122], 'sad')
        self.assertRaises(TypeError, area, True, 1)
    
    def test_perimeter_positive_value(self):
        self.assertEqual(perimeter(10, 10), 2*(10 + 10))
        self.assertEqual(perimeter(3, 4), 2*(3 + 4))
        self.assertEqual(perimeter(4, 3), 2*(4 + 3))
        self.assertAlmostEqual(perimeter(4.5, 3.5), 2*(4.5 + 3.5), 2)
    
    def test_perimeter_zero_value(self):
        self.assertRaises(ValueError, perimeter, 10, 0)
        self.assertRaises(ValueError, perimeter, 0, 10)

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, perimeter, -1, 2)
        self.assertRaises(ValueError, perimeter, 2, -3)
        self.assertRaises(ValueError, perimeter, -3, 4)
    
    def test_perimeter_types(self):
        self.assertRaises(TypeError, perimeter, 'abc', 12)
        self.assertRaises(TypeError, perimeter, [123, 122], 'sad')
        self.assertRaises(TypeError, perimeter, True, 1)
    


if __name__ == '__main__':
    unittest.main()