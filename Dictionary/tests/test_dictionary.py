# tests/test_dictionary.py

import unittest
from dictionary.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_newentry(self):
        self.dictionary.newentry("Apple", "A fruit that grows on trees.")
        self.assertEqual(self.dictionary.look("Apple"), "A fruit that grows on trees.")

    def test_look(self):
        self.assertEqual(self.dictionary.look("Nonexistent"), "Can't find Nonexistent in the dictionary.")

    def test_list_entries(self):
        self.dictionary.newentry("Apple", "A fruit that grows on trees.")
        self.assertIn("Apple: A fruit that grows on trees.", self.dictionary.list_entries())

if __name__ == "__main__":
    unittest.main()
