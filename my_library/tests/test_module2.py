import unittest
from my_library.module2 import multiply, divide

class TestModule2(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertRaises(ValueError, divide, 6, 0)

if __name__ == '__main__':
    unittest.main()
 
