import unittest
from string_reversal_func import string_reversal as sr

class unit_test_string_reversal(unittest.TestCase):
    def test_one(self):
        actual = sr("0uin{yR6j6{8D83")
        expected = "0DjR{yn6i6{8u83"
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = sr("8{,T}_8yB6ltgR3")
        expected = "8{,R}_8gt6lByT3"
        self.assertEqual(actual, expected)
        
    def test_three(self):
        actual = sr("Tlqr-c=l5v2nG1K")
        expected = "KGnv-l=c5r2ql1T"
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = sr("%8R[e6_7LuGH_2_")
        expected = "%8H[G6_7uLeR_2_"
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = sr("O4%WZ`WYvsFyq25")
        expected = "q4%yF`svYWZWO25"
        self.assertEqual(actual, expected)
    
    def test_six(self):
        actual = sr("xxsK]b6NQ5054-$")
        expected = "QNbK]s6xx5054-$"
        self.assertEqual(actual, expected)
    
    def test_seven(self):
        actual = sr("c8sb$:Zr@9n'5$9")
        expected = "n8rZ$:bs@9c'5$9"
        self.assertEqual(actual, expected)
    
    def test_eight(self):
        actual = sr("6h1HS7&{uvqaiAM")
        expected = "6M1Ai7&{aqvuSHh"
        self.assertEqual(actual, expected)
    
    def test_nine(self):
        actual = sr("Oys?<71sND91.(L")
        expected = "LDN?<71ssy91.(O"
        self.assertEqual(actual, expected)
    
    
        
if __name__ == "__main__":
    unittest.main()
