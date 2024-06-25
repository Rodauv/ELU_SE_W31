"""This module is automating the testing of the files committed to the repository"""

import unittest
from shopping_cart import calculatetotal

class TestShoppingCart(unittest.TestCase):

    def test_calculatetotal(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        total = calculatetotal(cart)
        self.assertEqual(total, 25.47)

if __name__ == '__main__':
    unittest.main()
