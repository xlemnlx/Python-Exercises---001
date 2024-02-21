import unittest
from interview_grading_func import interview_grading as ig

class unit_test_interview_grading(unittest.TestCase):
    def test_one(self):
        actual = ig(([2, 3, 8, 6, 5, 12, 10, 18], 64))
        expected = "qualified"
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = ig(([5, 5, 10, 10, 25, 15, 20, 20], 120))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = ig(([5, 5, 10, 10, 15, 15, 20], 120))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = ig(([5, 5, 10, 10, 15, 15, 20, 20], 130))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = ig(([5, 5, 10, 10, 15, 20, 50], 160))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    def test_six(self):
        actual = ig(([5, 5, 10, 10, 15, 15, 40], 120))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    def test_seven(self):
        actual = ig(([10, 10, 15, 15, 20, 20], 150))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    def test_eight(self):
        actual = ig(([5, 5, 10, 20, 15, 15, 20, 20], 140))
        expected = "disqualified"
        self.assertEqual(actual, expected)
    
    

if __name__ == "__main__":
    unittest.main()