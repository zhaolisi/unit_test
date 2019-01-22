#coding=utf-8
import unittest
from .count import Caculator

class TestCaculatorAdd(unittest.TestCase):
    def setUp(self):
        self.e = Caculator()
    def test_sub1(self):
        result = self.e.add(3,5)
        self.assertEqual(result,8)
    @unittest.skip("说明为什么要跳过用例")
    def test_sub2(self):
        result = self.e.add(3.2,3.5)
        self.assertEqual(result,6.7)
    def tearDown(self):
        print ("TEST PASS")



if __name__ == '__main__':
    unittest.main()
