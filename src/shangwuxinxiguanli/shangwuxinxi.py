#-*-coding=UTF-8 -*-
'''
Created on 2017年4月1日

@author: HP
'''
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from warnings import catch_warnings
from public  import shouye
import re
from selenium.common.exceptions import NoSuchElementException,\
    NoAlertPresentException   
from test.test_decimal import file
from test.test_tools.test_unparse import try_except_finally
from selenium.webdriver.common.action_chains import ActionChains

class ShangWuXinXi(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        driver = cls.driver
#         cls.driver=webdriver.Chrome()
#         cls.driver.implicitly_wait(20)
#         cls.driver.maximize_window()
#         cls.driver.get('http://101.201.41.60:60/platform/web/site/index')
#         #cls.driver.get('http://www.baidu.com')
#         title=cls.driver.title
#         print(title)
        
#     def test_denglu(self):
#         login.login(self,'lixingyu','123456')
#         self.seach_dengluxinxi=WebDriverWait(self.driver,5,1).until\
#         (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.demo-block")),message='时间超时').text
#         print(self.seach_dengluxinxi)  
    #进入商务管理页面
    def test_shangwuxinxi(self):
        #页面通过CSS选择器难以定位，所以获取所有DIV标签，先通过输出的文本判断是全部获得了div元素，再加个参数n，获取系统管理所在的div标签索引，得到一个div元素
#        self.driver = self.driver
        self.shangwuguanli=self.driver.find_elements_by_css_selector('div[class="el-submenu__title"]')
        print("进入商务信息管理页面")
        print('div元素个数为'+str(len(self.shangwuguanli)))
        i=0
        for itema in self.shangwuguanli:
            print(itema.text+'index'+str(i))
            i=i+1
        ActionChains(self.driver).click(self.shangwuguanli[2]).perform()
#     if __name__=='__main__':
#         unittest.main()
