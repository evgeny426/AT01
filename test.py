import unittest
from main import remainder

class TestRemainder(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(remainder(10, 2), 0)
        self.assertEqual(remainder(6, 4), 2)
        self.assertEqual(remainder(70, 3), 1)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, remainder, 6, 0)


if __name__ == '__main__':
   unittest.main()