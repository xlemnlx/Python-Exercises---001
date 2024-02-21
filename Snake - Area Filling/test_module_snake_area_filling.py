import unittest
from snake_area_filling_func import snake_area_filling as saf

class unit_test_snake_area_filling(unittest.TestCase):
    def test_one(self):
        actual = saf(6)
        expected = 5
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = saf(24)
        expected = 9
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = saf(8)
        expected = 6
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = saf(18)
        expected = 8
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = saf(555)
        expected = 18
        self.assertEqual(actual, expected)
    
    def test_six(self):
        actual = saf(2)
        expected = 2
        self.assertEqual(actual, expected)
    
    def test_seven(self):
        actual = saf(1)
        expected = 0
        self.assertEqual(actual, expected)
    
    def test_eight(self):
        actual = saf(900)
        expected = 19
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()