import unittest
from country_area_for_earth_func import country_area_for_earth as cafe

class unit_test_country_area_for_earth(unittest.TestCase):
    def test_one(self):
        actual = cafe(("USA", 9372610))
        expected = "USA is 6.29% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_two(self):
        actual = cafe(("Iran", 1648195))
        expected = "Iran is 1.11% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_three(self):
        actual = cafe(("Antartica", 14200000))
        expected = "Antartica is 9.53% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_four(self):
        actual = cafe(("Canada", 9984670))
        expected = "Canada is 6.7% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_five(self):
        actual = cafe(("Liechtenstein", 160))
        expected = "Liechtenstein is 0.0% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_six(self):
        actual = cafe(("Faroe Islands", 1393))
        expected = "Faroe Islands is 0.0% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_seven(self):
        actual = cafe(("Svalbard", 62045))
        expected = "Svalbard is 0.04% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_eight(self):
        actual = cafe(("Philippines", 300000))
        expected = "Philippines is 0.2% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_nine(self):
        actual = cafe(("Malaysia", 329847))
        expected = "Malaysia is 0.22% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_ten(self):
        actual = cafe(("Japan", 377915))
        expected = "Japan is 0.25% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    def test_eleven(self):
        actual = cafe(("South Korea", 100432))
        expected = "South Korea is 0.07% of the total world's landmass."
        self.assertEqual(actual, expected)
    
    

if __name__ == "__main__":
    unittest.main()