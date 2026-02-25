import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5.0)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()