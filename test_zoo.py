import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
# Price_ticket 50 ------------------------------------------------------------ 
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

# Price_ticket 100 students ---------------------------------------------------
    def test_students_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    def test_students_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

# Price_ticket 150 -------------------------------------------------------------
    def test_adults_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_adults_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)  

# Price_ticket 100 seniors -----------------------------------------------------   
    def test_seniors_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

# Price invalid when age < 0 --------------------------------------------------
    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid")
    
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()