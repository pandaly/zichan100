# -*- coding: utf-8 -*-
'''
Created on 2017年4月1日

@author: HP
'''
from selenium import webdriver
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from public import login
from time import sleep

class ShouYe():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://101.201.41.60:60/platform/web/site/index')
        print("111")
        sleep(1)
        login.login(self,"lixingyu","123456")
        self.seach_dengluxinxi=WebDriverWait(self.driver,5,1).until\
        (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.demo-block")),message='时间超时').text
        print(self.seach_dengluxinxi)
        

#     if __name__=='__main__':
#         unittest.main()