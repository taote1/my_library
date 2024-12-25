import unittest
from my_library.module1 import add, subtract

class TestModule1(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, 3), -1)

if __name__ == '__main__':
    unittest.main()
 
