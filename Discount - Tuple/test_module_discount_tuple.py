import unittest
from discount_tuple_func import discount_tuple

class unit_test_discount_tuple(unittest.TestCase):
    def test_one(self):
        actual = discount_tuple((89, 20))
        expected = 71.2
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = discount_tuple((100, 75))
        expected = 25
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = discount_tuple((2376, 85))
        expected = 356.40
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = discount_tuple((564378, 27))
        expected = 411995.94
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = discount_tuple((92834, 29))
        expected = 65912.14
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()