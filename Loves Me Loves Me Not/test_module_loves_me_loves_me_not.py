import unittest
from love_me_loves_me_not_func import love_me_loves_me_not as LMLMN

class unit_test_loves_me_loves_me_not(unittest.TestCase):
    def test_one(self):
        actual = LMLMN(2)
        expected = "Loves me, LOVES ME NOT"
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = LMLMN(6)
        expected = "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = LMLMN(1)
        expected = "LOVES ME"
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = LMLMN(7)
        expected = "Loves me, Loves me not, Loves me, Loves me not, Loves me, Loves me not, LOVES ME"
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = LMLMN(5)
        expected = "Loves me, Loves me not, Loves me, Loves me not, LOVES ME"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()