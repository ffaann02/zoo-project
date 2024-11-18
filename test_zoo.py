import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    def test_negative_age(self):
        # C1b1: age = -1, ticket price = 0
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_child_age(self):
        # C1b2: age = 12, ticket price = 50
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teen_age(self):
        # C1b3: age = 13, ticket price = 100
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_age(self):
        # C1b4: age = 60, ticket price = 150
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elder_age(self):
        # C1b5: age = 61, ticket price = 100
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()
