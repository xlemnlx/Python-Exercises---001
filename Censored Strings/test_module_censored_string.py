import unittest
from censored_string_func import censored_string

class unit_test_censored_string(unittest.TestCase):
    def test_one(self):
        actual = censored_string(("The cow jumped over the moon.", ["cow", "over"], "*"))
        expected = "The *** jumped **** the moon."
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = censored_string(("Why did the chicken cross the road ?", ["Did", "chicken", "road"], "*"))
        expected = "Why *** the ******* cross the **** ?"
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = censored_string(("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!"))
        expected = "!!! do my cats !!!! !!!!!! grass?"
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = censored_string(("How do I stop myself from using python!?", ["do", "stop", "using"], "-"))
        expected = "How -- I ---- myself from ----- python!?"
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = censored_string(("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~"))
        expected = "If ~~~~~~~~~~~~~~~~~~~~ are ~~~~~~~~~~~~ fun ~~~~ use."
        self.assertEqual(actual, expected)
    
    def test_six(self):
        actual = censored_string(("I'm dyslexic, but that deos'tn matter!", ["that", "matter!"], "?"))
        expected = "I'm dyslexic, but ???? deos'tn ???????"
        self.assertEqual(actual, expected)
    
    def test_seven(self):
        actual = censored_string(("I should be doing work but I am doing this instead.", ["should", "but", "this"], "*"))
        expected = "I ****** be doing work *** I am doing **** instead."
        self.assertEqual(actual, expected)
    
    

if __name__ == "__main__":
    unittest.main()