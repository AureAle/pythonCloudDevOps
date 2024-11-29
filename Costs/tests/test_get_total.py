# tests/test_get_total.py

import unittest
from costs.get_total import get_total

class TestGetTotal(unittest.TestCase):

    def setUp(self):
        # Setup some sample data for tests
        self.costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        
    def test_get_total_with_tax(self):
        # Test case: Buy socks and shoes with 9% tax
        result = get_total(self.costs, ['socks', 'shoes'], 0.09)
        self.assertEqual(result, 70.85)  # Expected output after tax
    
    def test_get_total_with_no_tax(self):
        # Test case: Buy socks and shoes with 0% tax
        result = get_total(self.costs, ['socks', 'shoes'], 0.0)
        self.assertEqual(result, 65.00)  # Expected output with no tax
    
    def test_get_total_item_not_in_cost(self):
        # Test case: Buy an item not in the cost dictionary
        result = get_total(self.costs, ['hat'], 0.09)
        self.assertEqual(result, 0.00) 

if __name__ == "__main__":
    unittest.main()
