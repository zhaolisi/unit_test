import unittest
from .count import Caculator

class TestCaculatorMinus(unittest.TestCase):
    def setUp(self):
        self.d=Caculator()
    def test_minus1(self):
        result = self.d.minus(5,2)
        self.assertEqual(result,3)
    def test_minus2(self):
        result = self.d.minus(15,15)
        self.assertEqual(result,0)
    def tearDown(self):
        print ("TEST PASS")

if __name__ == '__main__':
    unittest.main()