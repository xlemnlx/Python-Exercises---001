import unittest
from uncensored_string_func import uncensored_string as us

# test cases:
class unit_test_uncensored_string(unittest.TestCase):
    def test_normal(self):
        actual = us(("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
        expected = "Where did my vowels go?"
        self.assertEqual(actual, expected) # Function works under normal circumstances.
    
    def test_fix_by_default(self):
        actual = us(("abcd", ""))
        expected = "abcd"
        self.assertEqual(actual, expected) # Function works even if there's nothing to fix.
        
    def test_fix_end(self):
        actual = us(('Ch**s*, Gr*mm*t -- ch**s*', 'eeeoieee'))
        expected = "Cheese, Grommit -- cheese"
        self.assertEqual(actual, expected) # Function also able to fix character at the end.
    
    def test_fix_start(self):
        actual = us(('*l*ph*nt', 'Eea'))
        expected = "Elephant"
        self.assertEqual(actual, expected) # Function also able to fix character at the start.

if __name__ == "__main__":
    unittest.main()