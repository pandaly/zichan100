#-*-coding=UTF-8 -*-
'''
Created on 2017年3月23日

@author: HP
'''
from selenium import webdriver
import unittest,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from time import sleep
from warnings import catch_warnings
import re
from selenium.common.exceptions import NoSuchElementException,\
    NoAlertPresentException
import HTMLTestRunner    
from test.test_decimal import file
import  sys
sys.path.append(r'E:/Users/HP/PycharmProjects/ZiChan100/src')

from public import login
from public.autowebdriver import AutoWebdriver
class AnJian(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()
        cls.driver.get('http://101.201.41.60:60/platform/web/site/index')
        print("111")
        
    def test_denglu(self):
        login.login(self,"lixingyu","123456")
        self.seach_dengluxinxi=WebDriverWait(self.driver,5,1).until\
        (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.demo-block")),message='时间超时').text
        print(self.seach_dengluxinxi)
        
    def test_anjianguanli(self):
        #页面通过CSS选择器难以定位，所以获取所有DIV标签，先通过输出的文本判断是全部获得了div元素，再加个参数n，获取系统管理所在的div标签索引，得到一个div元素
        self.anjianguanli=self.driver.find_elements_by_css_selector('div[class|="el"]')
        #xitongguanli1=self.driver.find_element_by_link_text("系统管理")
        #xitongguanli1.click()
        print("cccga")
       
#         n=0
#         for i in self.xitongguanli:
#             
#             print(i.text+'\n')
#             #if(i.text.encode("utf-8")=="系统管理".encode("utf-8")):
#             #str=i.text.decode("utf-8")
#             #if(str==u"系统管理".decode("utf-8")):
#             if(n==2):
#                 i.click()
#             print(n)
#             n=n+1
#         print(len(self.xitongguanli))
#        self.xitongguanli[3].click()
'''    def test_zhuanghuguanli(self):
        print('ddddddddddd')
        #self.acountmanage=self.driver.find_element_by_css_selector('li[class$=active]')
        #self.xitongguanli=self.driver.find_elements_by_css_selector('div[class|="el"]')
        #self.acountmanage=self.driver.find_elements_by_css_selector('ul[class|="el"]')
        #self.acountmanage=self.driver.find_elements_by_css_selector('div[class="el-submenu__title"]')
        #定位帐户管理代码
        self.acountmanage=self.driver.find_elements_by_css_selector('li[class="el-menu-item"]')
#         k=0   
#         for j in self.acountmanage:
#             print(j.text+'++++'+str(k)+'zhanghuguanli===')
#             if(k==0):
#                 j.click()
#             k=k+1
#         print('----------11111-----------')
#         print(len(self.acountmanage))
        self.acountmanage[0].click()
    def test_chaxun(self):
#         try:
#             file=open(r'E:\zhanghuguanli.txtA','r')
#             values=file.readlines()
#             file.close()
#         except IOError as e:
#             print (e)
#        file = open(r'E:\zhanghuguanli.txt', 'r', encoding='utf-8')
        file=open(r'E:\zhanghuguanli.txt','r')
        values=file.readlines()
        file.close()
#         finally:
#             print ('hhhe')
        print('可以运行')
        for line in values:  
            name=line.strip('\n')
            self.zhanghuchaxun_text=self.driver.find_element_by_css_selector('input[type="text"]')#('input[placeholder="请输入内容"]')
            self.zhanghuchaxun_text.clear()
            self.zhanghuchaxun_text.send_keys(name)
            self.zhanghuchaxun_button=self.driver.find_element_by_css_selector('button[class="el-button el-button--success el-button--mini"]')
            self.zhanghuchaxun_button.click()
            sleep(2)
            self.zhanghuchaxun_table=self.driver.find_element_by_css_selector('div[class="el-table__body-wrapper"]>table>tbody>tr:first-child>td:nth-child(4)')
            print(name+'---'+self.zhanghuchaxun_table.text)
            expected_rex=re.compile('.*'+name+'.*')
            self.assertRegex(self.zhanghuchaxun_table.text,expected_rex)
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
     
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
      
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True    
'''
        
# if __name__=='__main__':
#     #unittest.main()
#     suite=unittest.TestSuite()
#     suite.addTest(AnJian('test_denglu'))
#     suite.addTest(AnJian('test_zhanghu'))
#     suite.addTest(AnJian('test_zhuanghuguanli'))
#     suite.addTest(AnJian('test_chaxun'))
#     runner=unittest.TextTestRunner()
#     runner.run(suite)
    
    
#      file_report=r'E:\result.html'
#      fp=open(file_report,'wb')
#      runnera=HTMLTestRunner.HTMLTestRunner(
#          stream=fp,
#          title=u'测试报告',
#          description=u'用例执行情况：',
#          )
#      runnera.run(suite)
#     fp.close()
