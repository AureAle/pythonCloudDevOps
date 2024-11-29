# tests/test_get_nth_letter.py

import unittest
from words.get_nth_letter import get_nth_letter

class TestGetNthLetter(unittest.TestCase):
# TODO: implement list of positions
    def setUp(self):
        # Setup some sample data for tests
        self.words = ["yoda", "best", "has"] 
        
    def test_get_nth_letter(self):
        # Test case: with n=0 n=1 n=2
        result = get_nth_letter(self.words)
        self.assertEqual(result, "yes") 
    def test_get_nth_letter(self):
        # Test case: with n=0 n=1 n=1
        result = get_nth_letter(self.words)
        self.assertEqual(result, "yea")  

if __name__ == "__main__":
    unittest.main()
