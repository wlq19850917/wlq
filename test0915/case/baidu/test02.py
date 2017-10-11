#coding:utf-8
import HTMLTestRunner
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start!")
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print("end!")
    def test02(self):
        u'使用断言assertEqual'
        a=1
        b=1
        self.assertEqual(a,b)
        print(a)

    def test03(self):
        u'使用assertIn'
        a='hello'
        b='hello world'
        self.assertIn(a,b)
        print("执行测试用例03")

    def test01(self):
        u'使用assertTrue'
        a = True
        self.assertTrue(a)
        print("执行测试用例01")

    def test04(self):
        u'断言结果错误'
        a = "我在测试"
        b =5
        self.assertEqual(a,b,msc="失败原因： %s != %s"%(a,b))
        print("add方法")




