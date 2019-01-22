import unittest
from unit_test.test_case.test_add import TestCaculatorAdd
from unit_test.test_case.test_minus import TestCaculatorMinus

suit = unittest.TestSuite()
suit.addTest(TestCaculatorAdd("test_add1"))
suit.addTest(TestCaculatorAdd("test_add2"))
suit.addTest(TestCaculatorMinus("test_minus1"))
runner = unittest.TextTestRunner()
runner.run(suit)
