import unittest
from calculations import *
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addnumbers(2, 3), 5) 
        # Test that 2 + 3 equals 5
        self.assertEqual(addnumbers(), 0)
        self.assertEqual(addnumbers(5),0)
    def test_subtraction(self):
        self.assertEqual(subtractingnumbers(5, 6), -1) 
        self.assertEqual(subtractingnumbers(3), 3)
        self.assertEqual(subtractingnumbers(7, 3), 4)
        self.assertEqual(subtractingnumbers(), 0)
    def test_multiplication(self):
        self.assertEqual(multiplynumbers(3, 2), 6) 
        self.assertEqual(multiplynumbers(5), 5)
        self.assertEqual(multiplynumbers(), 1)
    def test_divide(self):
        self.assertEqual(dividenumbers(7, 2), 3.5) 
        self.assertAlmostEqual(dividenumbers(7,3), 2.33, places=2)
        self.assertIsNone(dividenumbers(10, 0))
    def test_divide(self):
            self.assertIsNone(dividenumbers(10,'a'))
            self.assertIsNone(dividenumbers('a',10))
    def test_unexpected_exception(self):
        with self.assertRaises(Exception):
            dividenumbers()


if __name__ == "__main__":
    unittest.main()