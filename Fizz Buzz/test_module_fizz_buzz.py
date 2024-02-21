import unittest
from fizzbuzz_func import fizzbuzz

class unit_test_fizzbuzz(unittest.TestCase):
    def test_fizz(self):
        actual = fizzbuzz(3)
        expected = "Fizz"
        self.assertEqual(actual, expected)
    
    def test_buzz(self):
        actual = fizzbuzz(5)
        expected = "Buzz"
        self.assertEqual(actual, expected)
    
    def test_fizzbuzz(self):
        actual = fizzbuzz(15)
        expected = "FizzBuzz"
        self.assertEqual(actual, expected)
    
    def test_none(self):
        actual = fizzbuzz(4)
        expected = "4"
        self.assertEqual(actual, expected)
    
    

if __name__ == "__main__":
    unittest.main()