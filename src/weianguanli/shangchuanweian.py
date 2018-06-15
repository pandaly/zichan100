#-*-coding=UTF-8 -*-
'''
Created on 2017年4月11日

@author: HP
'''
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from public import login
from public import upload

class ShangChuanWeiAn(unittest.TestCase):   
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get('http://101.201.41.60:60/platform/web/sys/login')
        print("111")
      
    def test_denglu(self):
        '''登录主界面'''
        login.login(self,"lixingyu","123456")
        self.seach_dengluxinxi=WebDriverWait(self.driver,5,1).until\
        (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.demo-block")),message='时间超时').text
        print(self.seach_dengluxinxi)
        
    def test_weianguanli(self):
        '''进入委案管理页面
        #页面通过CSS选择器难以定位，所以获取所有DIV标签，先通过输出的文本判断是全部获得了div元素，再加个参数n，获取系统管理所在的div标签索引，得到一个div元素''' 
        self.caidanlists=self.driver.find_elements_by_css_selector('div[class="el-submenu__title"]')
        print("进入委案管理页面")
        print('div元素个数为'+str(len(self.caidanlists)))
        i=0
        for itema in self.caidanlists:
            print(itema.text+'index'+str(i))
            i=i+1
        ActionChains(self.driver).click(self.caidanlists[1]).perform()
  
    def test_shangchuanweian(self):
        '''进入上传委案页面'''
        self.shangchuanweian=self.driver.find_elements_by_css_selector('li[class="el-submenu is-opened"]>ul>li') 
        print('委案管理li元素个数为'+str(len(self.shangchuanweian)))
        a=0
        for itemc in self.shangchuanweian:
            print(itemc.text+'index'+str(a))
            a=a+1
        ActionChains(self.driver).click(self.shangchuanweian[2]).perform()   
    def test_shangchuan(self):
        upload.gongsichanpin(self,'test','test')
        upload.upload(self,r'E:\bbb.xlsx')

    def suite(self):
        loader=unittest.TestLoader()  
        suite=loader.discover(r'F:\PythonProject\test1')  
        return suite      
if __name__=='__main__':
    
    #unittest.main(defaultTest='suite',verbosity=2)
    

     
    suite=unittest.TestSuite()
    suite.addTest(ShangChuanWeiAn('test_denglu'))
    suite.addTest(ShangChuanWeiAn('test_weianguanli'))
    suite.addTest(ShangChuanWeiAn('test_shangchuanweian'))
    suite.addTest(ShangChuanWeiAn('test_shangchuan'))
    #suite.addTest(ShangChuanWeiAn('test_chaxun_chanpinleixing'))
    #suite.addTest(ShangChuanWeiAn('test_xinzeng'))
    runner=unittest.TextTestRunner()
    runner.run(suite)

