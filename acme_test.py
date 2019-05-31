#!/usr/bin/env python
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

### Part 5 - Measure twice, Test once

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product values."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)
        self.assertEqual(prod.name, 'Test Product')

    def test_stealability(self):
        not_so = Product(price=1, weight=10)
        self.assertEqual(not_so.stealability(), "Not so stealable...")
        kinda = Product(price=6, weight=10)
        self.assertEqual(kinda.stealability(), "Kinda stealable.")
        very = Product(price=20, weight=10)
        self.assertEqual(very.stealability(), "Very stealable!")

    def test_explode(self):
        fizzle = Product(weight=5, flammability=1)
        self.assertEqual(fizzle.explode(), "...fizzle.")
        boom = Product(weight=20, flammability=1)
        self.assertEqual(boom.explode(), "...boom!")
        baboom = Product(weight=30, flammability=2)
        self.assertEqual(baboom.explode(), "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products()
        for prod in products:
            self.assertIn(prod.name.split()[0], ADJECTIVES)
            self.assertIn(prod.name.split()[1], NOUNS)

if __name__ == '__main__':
    unittest.main()
