#coding=utf-8
import unittest
#通过discover匹配文件
suit = unittest.defaultTestLoader.discover("./test_case","test_*.py")#当前目录，匹配的文件名，以test开头的py文件
#运行测试
runner=unittest.TextTestRunner()
runner.run(suit)

