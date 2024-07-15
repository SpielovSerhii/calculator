import unittest
from calculator import add, subtract, multiply, divide

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 12), 17)
        self.assertEqual(add(1, 4), 5)
        self.assertEqual(add(-10, -20), -30)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(4, -10), 14)
        self.assertEqual(subtract(-10, -2), -8)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-1, 10), -10)
        self.assertEqual(multiply(-10, -2), 20)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(100, 2), 50)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(0, 1), 0)
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main