#coding:utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
class Test(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get("http://www.loveqiche.com/user/login")
    # def login(self,username,psw):
    #     self.driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[3]/div[3]/div/div/div[1]/form/div[1]/a[2]").click()
    #     self.driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[3]/div[3]/div/div/div[1]/form/div[3]/div[1]/input").send_keys(username)
    #     self.driver.find_element_by_xpath(".//*[@id='ng-app']/body/div[3]/div[3]/div/div/div[1]/form/div[3]/div[2]/input").send_keys(psw)
        

    def setUp(self):
        print("start")

    def test01(self):
        print("执行测试用例01")
    def test03(self):
        print("执行测试用例03")
    def test02(self):
        print("执行测试用例02")
    def testMinus(self):
        result = 6-5
        hope = 1
        self.assertEqual(result,hope)





