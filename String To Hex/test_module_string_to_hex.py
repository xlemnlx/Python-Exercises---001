import unittest
from string_to_hex_func import string_to_hex as sth

class unit_test_string_to_hex(unittest.TestCase):
    def test_one(self):
        actual = sth("Big Boi")
        expected = "42 69 67 20 42 6f 69"
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = sth("Marty Poppinson")
        expected = "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = sth("abcdefghi")
        expected = "61 62 63 64 65 66 67 68 69"
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = sth("oh dear")
        expected = "6f 68 20 64 65 61 72"
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = sth("i hate C#")
        expected = "69 20 68 61 74 65 20 43 23"
        self.assertEqual(actual, expected)
    
    def test_six(self):
        actual = sth("i love C++  ➞ not really")
        expected = "69 20 6c 6f 76 65 20 43 2b 2b 20 20 279e 20 6e 6f 74 20 72 65 61 6c 6c 79"
        self.assertEqual(actual, expected)
    
if __name__ == "__main__":
    unittest.main()