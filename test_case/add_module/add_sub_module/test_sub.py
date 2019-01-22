#coding=utf-8
import unittest
from .count import Caculator

class TestCaculatorAdd(unittest.TestCase):
    def setUp(self):
        self.c = Caculator()
    @unittest.skip("说明为什么要跳过用例")
    def test_add1(self):
        result = self.c.add(3,5)
        self.assertEqual(result,8)
    def test_add2(self):
        result = self.c.add(3.2,3.5)
        self.assertEqual(result,6.7)
    def tearDown(self):
        print ("TEST PASS")



if __name__ == '__main__':
    unittest.main()
